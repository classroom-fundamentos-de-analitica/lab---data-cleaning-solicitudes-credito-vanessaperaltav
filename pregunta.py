"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime
def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    df.dropna(axis=0, inplace=True)
    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.str.replace(',','') 
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))  
    df.comuna_ciudadano = df.comuna_ciudadano.apply(float)
    #colString = df.select_dtypes(include=['object']).columns.tolist()
    
    for i in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[i] = df[i].str.lower()
        df[i] = df[i].str.replace('_',' ')
        df[i] = df[i].str.replace('-',' ')
    
    df.drop_duplicates(inplace=True)

    return df
