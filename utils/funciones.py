
import pandas as pd

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
    premium = ['MERCEDES-BENZ','BMW','AUDI','JAGUAR','LEXUS','INFINITI',
        'PORSCHE','LOTUS','MERCEDES','MERCEDESBENZ','MASERATI','FERRARI',
        'BENTLEY','LAMBORGHINI','TESLA']
    mid_premium =['VOLKSWAGEN','VOLVO','SUBARU','TOYOTA','LAND-ROVER',
        'DS','MINI','ALFA ROMEO','HONDA','ABARTH','DFSK','CUPRA']
    Standard = ['SEAT', 'CITROEN', 'FORD','PEUGEOT','NISSAN','JEEP',
        'SKODA','MAZDA', 'MITSUBISHI', 'RENAULT', 'KIA','HYUNDAI',
        'SAAB','CHRYSLER','CADILLAC','SUZUKI','SMART','SSANGYONG',
        'ROVER','LANCIA','IVECO','DODGE','GALLOPER','ISUZU','MG',
        'SANTANA','CADILLAC','AUSTIN','LDV','PIAGGIO','PONTIAC',
        'IVECO-PEGASO','UMM','MAXUS','DRAUTOMOBILES','IVECOPEGASO']
    low_cost = ['DACIA','FIAT','OPEL','CHEVROLET','DAEWOO','MAHINDRA','TATA',
        'InvictaElectric','DAIHATSU']
    if x.upper().replace(' ','') in premium:
        cluster = 'Premium'
    elif x.upper().replace(' ','') in mid_premium:
        cluster = 'Mid_Premium'
    elif x.upper().replace(' ','') in Standard:
        cluster = 'Standard'
    elif x.upper().replace(' ','') in low_cost:
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
    coupe_grande = ['claseclk','claseslk','elise','z4','boxster','mustang',
        'Cayman','camaro','r8']
    coupe_pequeno = ['scirocco','tt','coupe','eos','z3','gt86']
    sedan_grande =['a4','passat','serie5','insignia','mondeo','clasee','a6',
            'a5','508','octavia','laguna','c5','serie4','407','avensis',
            'vectra','espace','mazda6','superb','s60','alteaxl','accord',
            'talisman','c5aircross','sharan','9-3','406','v60','galaxy',
            'giulia','cc','clasecls','prius','407sw','passatcc','clases',
            'volt','clasegle','a7','primera','v50','arteon','s90','optima',
            's5','q50','156','ds5','s80','ghibli','607','xantia','rs6']
    sedan_pequeno = ['serie3','clasec','clasecla','c-elysee','toledo',
    'i40','v40','cordoba','leaf','ioniq','s40','logan','cruze','proceed','cla',
    'golfsportsvan','s3','jetta','clasecl','lancer','celica','impreza','200']
    suv_grande = ['qashqai','touran','3008','scenic','sportage','tucson',
    '5008','c-max','cmax','zafira','q3','grandc4picasso','grandscenic','x3',
    'x-trail','c4picasso','q5','rangeroverevoque','ateca','xc60','cr-v','crv',
    'xsarapicasso','kadjar','carens','cx-5','cx5','alhambra','claseglc',
    's-max','clasem','verso','altea','grandlandx','x5','crosslandx','rodius',
    'xc90','outlander','niro','duster','asx','sorento','grandc-max',
    'grandcmax','carnival','f-pace','tarraco','captiva','korando','montero',
    'freelander','xe','voyager','807','grandvoyager','gla','q7','defender',
    'claseglecoupe','stelvio','discovery','claseg','antara','l200','claser',
    'ds7crossback','claseglk','mazda5','quasqai+2','ranger','terranoii',
    'terrano','koleos','grandvitara','q8','omega','rexton','murano',
    'v90crosscountry','gle']
    suv_pequeno = ['x1','tiguan','2008','kuga','arona','juke','clasegla',
    'captur','countryman','c4cactus','rav4','c-hr','chr','ecosport','panda',
    'mokkax','serie2grantourer','stonic','q2','renegade','t-roc','troc',
    'ix35','xceed','mokka','vitara','corollaverso','t-cross','tcross''lodgy',
    'x2','xc40','fusion','cx-3','cx3','jimny','ds3crossback']
    compacto_grande = ['golf','focus','a3','megane','astra','leon','308','c4',
    'auris','i30','civic','307','ceed','corolla','xsara','kona','mazda3',
    '307sw','serie2','meriva','v40','clubman','147','compact','i3','500l',
    'stilo','accent','escort','ds4','q30','kadett','ds3']
    compacto_pequeno = ['ibiza','serie1','mini','corsa','clio','polo','fiesta',
    'clasea','500','c3','208','claseb','yaris','a1','207','tipo','micra','206',
    'fabia','fortwo','c3aircross','sandero','i20','aygo','punto',
    'serie2activetourer','500c','picanto','zoe','i10','c1','rio','giulietta',
    'adam','beetle','c2','e-208','ka+','ka','aveo','saxo','twingo','306',
    'note','tigra','aveo','newbeetle','mazda2','108','jazz','clioiii',
    'matiz','106','getz','205']
    furgon_trabajo = ['berlingo','partner','caddy','transit','transporter',
    'jumper','vivaro','boxer','combo','trafic','sprinter','master','multivan',
    'kangoofurgon','expert','doblo','fiorino','daily','kangoo','citan',
    'rifter','crafter','talento','bipper']
    furgon_pasajero = ['vito','kangoocombi','caravelle','viano','nv200']
    if x.lower().replace(' ','') in coupe_grande:
        cluster = 'coupe_grande'
    elif x.lower().replace(' ','') in coupe_pequeno:
        cluster = 'coupe_pequeno'
    elif x.lower().replace(' ','') in sedan_grande:
        cluster = 'sedan_grande'
    elif x.lower().replace(' ','') in sedan_pequeno:
        cluster = 'sedan_pequeno'
    elif x.lower().replace(' ','') in suv_grande:
        cluster = 'suv_grande'
    elif x.lower().replace(' ','') in suv_pequeno:
        cluster = 'suv_pequeno'
    elif x.lower().replace(' ','') in compacto_grande:
        cluster = 'compacto_grande'
    elif x.lower().replace(' ','') in compacto_pequeno:
        cluster = 'compacto_pequeno'
    elif x.lower().replace(' ','') in furgon_trabajo:
        cluster = 'furgon_trabajo'
    elif x.lower().replace(' ','') in furgon_pasajero:
        cluster = 'furgon_pasajero'
    else:
        cluster = 'otro'
    return cluster
def add_delete_columns(df, nom_column_1, transformacion_1, nom_column_2, transformacion_2, del_col_1):
    df['Cluster_'+nom_column_1]=df[nom_column_1].apply(transformacion_1)
    df['Cluster_'+nom_column_2]=df[nom_column_2].apply(transformacion_2)
    if del_col_1 in df.columns:
        df.drop(columns=[nom_column_1,nom_column_2,del_col_1],inplace=True)
    else:
        df.drop(columns=[nom_column_1,nom_column_2],inplace=True)
    return df
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
            outliers = df_num[
                (df_num[i] < lim_inf) | (df_num[i] > lim_sup )].shape[0]
            dic[i] = [outliers,lim_inf,lim_sup]
    dic.index = ['num_outliers','valor_min','valor_max']
    return dic
