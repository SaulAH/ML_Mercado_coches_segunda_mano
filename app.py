# importing necessary libraries and functions
from flask import Flask, request, jsonify, render_template, url_for, redirect
import pickle
import pandas as pd
import numpy as np
from utils import funciones as fn


app = Flask(__name__) #Initialize the flask App
pipeline_test=pickle.load(open('./model/pipeline_train.pkl','rb'))
modelo=pickle.load(open('./model/my_model.pkl','rb'))

def df_inicial(Marca, Modelo, Combustible, Anyo, Kilometros,Potencia,
                Profesional, Comunidad): 
    data = [[Marca,Modelo,Combustible,Anyo,Kilometros,Potencia,
                Profesional,Comunidad]]
    columnas = ['Marca', 'Modelo', 'Combustible','Anyo',
                'Kilometros','Potencia','Vendedor_profesional',
                'Comunidad_Autonoma']
    tabla = pd.DataFrame(data, columns=columnas)  
    return tabla

def transformacion(df,fn_p=fn.add_delete_columns, fn_1=fn.cluster_marcas,fn_2=fn.cluster_modelo,
                    col1='Marca',col2='Modelo',col3='dealer'): 
    return fn_p(df,col1,fn_1,col2,fn_2,col3)

def pipeline_df(df,pipe):
    df_pipe = pipe.transform(df).toarray()
    df_final = pd.DataFrame(df_pipe, columns=pipe.get_feature_names_out())
    return df_final

def prediction(df,model):
    return model.predict(df)
 

@app.route('/')
def input_data(): 
    return render_template('input_manual.html') 

@app.route('/result', methods=["POST","GET"]) 
def input():
    if request.method == 'POST': 
        Marca = str(request.form['Marca'])
        Modelo = str(request.form['Modelo'])
        Combustible = str(request.form['Combustible'])
        Anyo = float(request.form['Anyo'])
        Kilometros = int(request.form['Km'])
        Potencia = float(request.form['cv'])
        Profesional = bool(request.form['Profesional'])
        Comunidad = str(request.form['Comunidad'])
            

        datos_entrada = df_inicial(Marca, Modelo, Combustible, Anyo, Kilometros,Potencia,
                Profesional, Comunidad)
        df_trans = transformacion(datos_entrada)
        df_escalado = pipeline_df(df_trans,pipeline_test)
        prediccion = int(prediction(df_escalado,modelo)[0])
        pred = str(prediccion)+str('€')

        return render_template('result.html', predicted = pred) 

@app.route('/upload', methods = ['POST','GET'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'), index_col=0)
        df.dropna(how='any', axis=0, inplace=True)
        if 'Precio' in df.columns:
            df.drop(columns=['Precio'], inplace=True)
        else:
            pass
        df_1 = df.copy()
        df_trans = transformacion(df_1)
        df_escalado = pipeline_df(df_trans,pipeline_test)
        prediccion = prediction(df_escalado,modelo)
        pred = prediccion
        df['Precio']=pred 
        if 'dealer' in df.columns:
            df.drop(columns=['dealer'], inplace=True)
        else:
            pass       
        
        table = df.to_html(index=False)
        return render_template('upload.html', table = table)
    return render_template('upload.html')


if __name__ == "__main__":
    app.run()