def funcioncita(x):
    return str(x+x)


def elim_columnas(df, lista, new_name):

    '''
    This function use a list with the name of the columns you want to delete 

    Argumetns:
        -df: original dataframe from which to take the data
        -list: list with the name of the columns to delete
        -new_name: new name to de data frame

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