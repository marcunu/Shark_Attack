def guarda_grafico (nombre, nombre_expor):
    '''
    This function saves the graphic.
    Arguments:
        -nombre: The name of the graphic you want to save
        -nombre_expor: choosen name to export.

    '''
    
    nombre.figure.savefig(nombre_expor)
