def guarda_grafico (nombre, nombre_expor):
    '''
    This function saves the graphic.
    Arguments:
        -nombre: The name of the graphic you want to save
        -nombre_expor: choosen name to export.

    '''
    
    nombre.figure.savefig(nombre_expor)

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

def rotar_labels(grafico, angulo):
    grafico.set_xticklabels(grafico.get_xticklabels(), rotation=angulo)