# machine learning
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import (RandomForestRegressor, AdaBoostRegressor,
                             GradientBoostingRegressor, ExtraTreesRegressor)



lista_comunidades = ['Comunidad_de_Madrid','Andalucía','Catalunya',
    'Comunidad_Valenciana','Galicia','Castilla_y_León','País_Vasco']
lista_modelos = [
    LinearRegression(),
    XGBRegressor(),
    KNeighborsRegressor(),
    AdaBoostRegressor(DecisionTreeRegressor()),
    DecisionTreeRegressor(),
    RandomForestRegressor(),
    ExtraTreesRegressor(),
    SVR(),
    GradientBoostingRegressor()
]