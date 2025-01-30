import pandas as pd
import numpy as np
datos = pd.read_csv('./heartfailure.csv', encoding='latin-1')
df = pd.DataFrame(datos)
#print(df.head())

#Estadisticas Basicas
#print(df.describe())

#Listar todos los nombres de las columnas
#print(df.columns)

#Mostrar las 5 primeras filas de la ultima columna
#print(df.iloc[:, -1].head())

#Mostrar las 5 primeras filas de las primeras 3 columnas
print(df.iloc[:, :5].head())
print('\n'*3)
#Mostrar las 6 primeras filas de las columnas 3 a 6 
print(df.iloc[:6, 3:6])
print('\n'*3)
# Eliminar registros que superen los 60 años
#df = df[df['age'] <= 60]
# Mostrar la edad más alta y más baja
max_age = df['age'].max()
min_age = df['age'].min()
print(f'Edad más alta: {max_age}')
print(f'Edad más baja: {min_age}')