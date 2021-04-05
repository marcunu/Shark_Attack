def funcioncita(x):
    return str(x+x)

def elim_vacias(df, new_df, ax, hw):
    
    '''
    This function use a list to delete the columns or rows with no values. 

    Argumetns:
        -df: original dataframe from which to take the data
        -list: list with the name of the columns to delete
        -new_name: new name to de data frame

    '''

    new_df = df.dropna(axis=ax, how=hw)

    return new_df


def elim_columnas(df, lista):

    '''
    This function use a list with the name of the columns you want to delete 

    Argumetns:
        -df: original dataframe from which to take the data
        -list: list with the name of the columns to delete

    '''

    new_name = df.drop(lista, axis=1)

    return new_name



def check_columns(df, column1, column2):

    '''
    This function returns the different values of two apparently equal columns.

    Arguments:
        -df: original dataframe from which to take the data
        -column1: first column for comparison
        -column2: second column for comparison

    '''

    return df[df[column1] != df[column2]]


def valores_iguales(df, column, value):
    '''
    This function returns the values of a column that are equal to the desired value.

    Arguments:
        -df: original dataframe from which to take the data
        -column: column from which to take the data
        -value: desired value for the comparison
    '''

    return df[df[column] == value]


def valores_distintos(df, column, value):
    '''
    This function returns the values of a column that are not equal to the desired value.

    Arguments:
        -df: original dataframe from which to take the data
        -column: column from which to take the data
        -value: desired value for the comparison
    '''

    return df[df[column] != value]

def df_filtered_best(data_frame, columna, n_ind):
    import pandas as pd 
    
    '''
    This function returns the most repeated values in the selected range.

    Arguments:
        -Columna: selected column from which you want to take de values.
        - n_ind: top rank values you want to take.

    ''' 

    mejores = data_frame[columna].value_counts(1)
    top = list(mejores.index[:n_ind])    
    
    df_final = data_frame[data_frame[columna] == top[0]]
    top.pop(0)
    for i in top:

        i =data_frame[data_frame[columna] == i]
        df_final = pd.concat([df_final,i])
    
    return df_final


def grafica_investigador(persona, color):
    grafi = shrk[shrk["Investigator or Source"] == persona].reset_index()
    sns.countplot(y=grafi.Country, palette=color)


def grafico_lista_h(lista, color):

    df_final = shrk[shrk["Activity"] == lista[0]]
    lista.pop(0)
    for i in lista:

        i =shrk[shrk["Activity"] == i]
        df_final = pd.concat([df_final,i])

    df_final.sample(5)
    return sns.countplot(y=df_final.Activity, palette=color)


def guarda_grafico (nombre, nombre_expor):
    '''
    This function saves the graphic.
    Arguments:
        -nombre: The name of the graphic you want to save
        -nombre_expor: choosen name to export.

    '''
    
    nombre.figure.savefig(nombre_expor)
