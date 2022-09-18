# se cargan las librerias
import pandas as pd
import pickle


from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split

# machine learning

from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import (GridSearchCV)
from sklearn.compose import ColumnTransformer
from utils import funciones as fn

# se cargan los datos en bruto
ruta_data_raw = f'./data/raw/df_venta_coches.csv'
df = pd.read_csv(ruta_data_raw,index_col=0)

# los datos en bruto se separan en train y test para entrenar solo con los train
Train, Test = train_test_split(df, test_size=0.2, random_state=1234)
Train = Train.reset_index(drop=True) # se resetean los indices de los nuevos df que se han creado
Test = Test.reset_index(drop=True) # se resetean los indices de los nuevos df que se han creado

# el data set utilizado no es exactamente la salida del EDA por loq ue le filtramos los outlaiers
filtro_outliers = (
    Train.Precio < 41500) & (
        Train.Potencia < 236.98) & (
            Train.Kilometros < 377504) & (
                Train.Anyo > 1990)
Train = Train[filtro_outliers]


# se hace la clasificación de Marcas y Modelos para luego poder meter los datos al modelo
fn.add_delete_columns(Train, 'Marca',fn.cluster_marcas,'Modelo',fn.cluster_modelo,'dealer')

# Se separa la variable target del resto de datos
X = Train.drop(columns=['Precio']).reset_index(drop=True)
y = Train['Precio'].reset_index(drop=True)

# se crea la transformación de las columnas
var_numericas = list(X.select_dtypes(exclude=['object','boolean']))
#the textual transformation pipeline
var_cat = list(X.select_dtypes(exclude=['int64','float64']))
#setting the order of the two pipelines
pipeline_train = ColumnTransformer([
        ("numeric", StandardScaler() , var_numericas),
        ("text", OneHotEncoder(), var_cat),
    ])

# se entrena el pipeline con los datos de entrada
pipeline_train.fit(X)
X_trans=pipeline_train.transform(X).toarray()
X_escalado = pd.DataFrame(X_trans, columns=pipeline_train.get_feature_names_out())


# se genera la red de parametros del modelo
grid_XGBoost = {
    'n_estimators': [200, 400, 600, 800],
    'max_depth': [None, 60, 90],
    'eta': [0.05, 0.1, 0.01, 0.2],
    'gamma': [0, 2, 4, 6],
} # parametros para XGBoost

# se entrena el modelo
gridsearch = GridSearchCV(estimator=XGBRegressor(),param_grid=grid_XGBoost,n_jobs=-1,scoring='neg_mean_squared_error')
my_model = gridsearch.fit(X_escalado, y)

# se guarda el modelo entrenado
pickle.dump(my_model, open('./model/my_model.pkl', 'wb'))