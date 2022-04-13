import pandas as pd

df = pd.read_csv("dataset.csv", index_col="id") #Consumir DataFrame

df 
df.head() #Traer solo las primeras 5 filas de un Dataframe, se puede especificar el valor en los ()
df.tail() #Traer solo las ultimas 5 filas de un Dataframe, se puede especificar el valor en los ()
df.describe() #Traer estadisticas descriptivas de un Dataframe

##Limpieza de datos##
df.dropna() #Elimina 'Filas' que tienen datos como NaN
df.fillna(0) #Sustituye valores NaN por el valor entregado en los () 
df.fillna({"Cabin": "C0", "Age": 0}) #Sustituye valores NaN de las columnas como "KEY" por el valor entregado como "VALUES"

##Filtrado por columnas##
df["Name"] #Traer una columna del Dataframe.
df[['Name','Age', 'Sex']]  #Traer muchas columnas de un Dataframe.

##Filtrado por filas##
df.iloc[0:3] #Devuelve las tres primeras filas o una sola en vez de llamar al indice 0
df.iloc[[1,3,6]] #Devuelve las filas dependiendo del indice pedido.. No es por rango !!
df.loc[1:4, ["Name", "Sex"]] #Devuelve las filas y columnas pedidas.. No es por rango !!
  
## Validaciones ## 
df[(df["Age"] < 13) & (df["PassengerId"] > 800)] #Validar columas con & o | 
df[(df["Age"] < 13) | (df["PassengerId"] > 800)] #Validar columas con & o | 
df[df["Sex"].str.contains("male")] #Filtrar datos de la columna que contengan en su cadena el string 'male' 


## Manipular datos de las columnas ##
def funcion_transformacion(f):
    import random
    calcular = f * random.randint(69,190) #Multiplica por valores aleatorios entre 1 y 10
    print(calcular)
    return calcular #Retorna el nuevo valor en la nueva columna creada

df["Nueva_Columna"] = df["favorites"].apply(funcion_transformacion) #apply() hace la accion por cada valor de la columna
df


## Manipular matematicamente dos columnas y devolver una diferente ##
def popularidad(fila):
    resultado = fila["followees"]/fila["followers"] #Divide dos columnas
    return resultado 

df["popularidad"] = df.apply(popularidad, axis=1) #apply() la funcion se ejecutara ahora en todo el dataframe y no solo por columna. 
                                                  #'axis=1' es necesario especificarlo para decir que la funcion sera ejecutada por cada fila. 
df

## Agrupación de datos y sacar media o funciones de agregacion manual por columna ##
df.groupby("country").mean() # mean(), calcula la media de todos los valores agrupados
df

df.groupby("country").agg({  
    "followers": "sum",
    "mentions": "mean",
    "retweets": "max"
})

import matplotlib.pyplot as plt

df["followers"].plot()
plt.show()

