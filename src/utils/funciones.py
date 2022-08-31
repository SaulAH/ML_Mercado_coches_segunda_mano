import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os
def cluster_marcas(x):
    '''
    La función devuelve el cluster al que pertenece la marca del vehículo
    en funcion de su status:
        - premium
        - mid-premium
        - standard
        - low cost
    entrada --> Marca del vehículo
    salida --> cluster
    '''
    premium = ['MERCEDES-BENZ','BMW','AUDI','JAGUAR','LEXUS','INFINITI']
    mid_premium =['VOLKSWAGEN','VOLVO','SUBARU','TOYOTA','LAND-ROVER',
        'DS','MINI','ALFA ROMEO','HONDA','ABARTH']
    Standard = ['SEAT', 'CITROEN', 'FORD','PEUGEOT','NISSAN','JEEP',
        'SKODA','MAZDA', 'MITSUBISHI', 'RENAULT', 'KIA','HYUNDAI',
        'SAAB','CHRYSLER','CADILLAC','SUZUKI','SMART','SSANGYONG',
        'ROVER','LANCIA','IVECO']
    low_cost = ['DACIA','FIAT','OPEL','CHEVROLET','DAEWOO']
    if x in premium:
        cluster = 'Premium'
    elif x in mid_premium:
        cluster = 'Mid_Premium'
    elif x in Standard:
        cluster = 'Standard'
    elif x in low_cost:
        cluster = 'Low_Cost'
    else:
        cluster = 'Desconocido'
    return cluster
def cluster_modelo(x):
    '''
    La función devuelve el tipo de modelo que tiene el vehículo:
        - coupe
        - sedan
        - sub
        - compacto
        - furgon
    entrada --> Modelo del vehículo
    salida --> cluster
    '''
    coupe_grande = ['Clase CLK','Clase SLK']
    coupe_pequeno = ['Scirocco','TT']
    sedan_grande =['A4','Passat','Serie 5','Insignia','Mondeo','Clase E','A6',
        'A5','508','Octavia','Laguna','C5','Serie 4','407','Avensis','Vectra',
        'Espace','Mazda6','Superb','S60','Altea XL','Accord','Talisman',
        'C5 Aircross','Sharan']
    sedan_pequeno = ['Serie 3','Clase C','Clase CLA','C-Elysee','Toledo','i40',
        'V40','Cordoba','LEAF']
    sub_grande = ['QASHQAI','Touran','3008','Scenic','Sportage','TUCSON',
        '5008','C-Max','Zafira','Q3','Grand C4 Picasso','Grand Scenic',
        'X3','X-TRAIL','C4 Picasso','Q5','Range Rover Evoque','Ateca','XC60',
        'CR-V','Xsara Picasso','Kadjar','Carens','CX-5','Alhambra','Clase GLC',
        'S-MAX','Clase M','Verso','ALTEA','Grandland X','X5','Crossland X',
        'Rodius','XC90','Outlander','Niro','Duster']
    sub_pequeno = ['X1','Tiguan','2008','Kuga','Arona','JUKE','Clase GLA',
        'Captur','Countryman','C4 Cactus','Rav4','C-HR','EcoSport','Panda',
        'Mokka X','Serie 2 Gran Tourer','Stonic','Q2','Renegade','T-Roc',
        'ix35','XCeed']
    compacto_grande = ['Golf','Focus','A3','Megane','Astra','Leon','308','C4',
        'Auris','i30','Civic','307','ceed','Corolla','Xsara','Kona','Mazda3',
        '307 SW','Serie 2','Meriva']
    compacto_pequeno = ['Ibiza','Serie 1','MINI','Corsa','Clio','Polo',
        'Fiesta','Clase A','500','C3','208','Clase B','Yaris','A1','207',
        'Tipo','Micra','206','Fabia','fortwo','C3 Aircross','Sandero','i20',
        'Aygo','Punto','Serie 2 Active Tourer','500C','Picanto','Zoe',
        'i10','C1','Rio']
    furgon_trabajo = ['Berlingo','Partner','Caddy','Transit','Transporter',
        'Jumper','Vivaro','Boxer','Combo','Trafic','Sprinter','Master']
    furgon_pasajero = ['Vito','Kangoo Combi','Caravelle']
    if x in coupe_grande:
        cluster = 'coupe_grande'
    elif x in coupe_pequeno:
        cluster = 'coupe_pequeno'
    elif x in sedan_grande:
        cluster = 'sedan_grande'
    elif x in sedan_pequeno:
        cluster = 'sedan_pequeno'
    elif x in sub_grande:
        cluster = 'sub_grande'
    elif x in sub_pequeno:
        cluster = 'sub_pequeno'
    elif x in compacto_grande:
        cluster = 'compacto_grande'
    elif x in compacto_pequeno:
        cluster = 'compacto_pequeno'
    elif x in furgon_trabajo:
        cluster = 'furgon_trabajo'
    elif x in furgon_pasajero:
        cluster = 'furgon_pasajero'
    else:
        cluster = 'otro'
    return cluster
def outliers(df):
    ''' 
    La función calcula los outliers de las variables numéricas
    entrada --> df
    salida --> df que indica los maximos, mínimos y nº de outliers
    '''
    df_num = df.select_dtypes(exclude=['object','boolean'])
    dic = pd.DataFrame()
    for i in df_num.columns:
            Q_1 = df_num[i].quantile(0.25)
            Q_3 = df_num[i].quantile(0.75)
            RI = Q_3 - Q_1
            lim_inf = Q_1 - 1.5*RI
            lim_sup = Q_3 + 1.5*RI
            outliers = df_num[(df_num[i] < lim_inf) | (df_num[i] > lim_sup )].shape[0]
            dic[i] = [outliers,lim_inf,lim_sup]
    dic.index = ['num_outliers','valor_min','valor_max']
    return dic
