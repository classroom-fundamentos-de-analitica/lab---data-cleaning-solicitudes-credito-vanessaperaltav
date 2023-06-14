"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df = df.drop('Unnamed: 0', axis = 1)
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)

    df.monto_del_credito = df.monto_del_credito.apply(lambda x: str(x).strip('$').replace(',',''))
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)

    for columna in ['sexo','tipo_de_emprendimiento',
                    'idea_negocio','barrio','línea_credito']:
        df[columna] = df[columna].apply(
                                        lambda s: s.lower().replace('-',' ').replace('_',' ') 
                                        if type(s) == str else s)
    df.dropna(axis=0, inplace = True)
    df.drop_duplicates(inplace=True)

    return df

print(clean_data().sexo.value_counts().to_list())
