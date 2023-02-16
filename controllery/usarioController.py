from modelos.usuariosModel import seleccionarUsuarios, seleccionarUsuario
from modelos.usuariosModel import eliminarUsuariosModel, modificarUsuariosModel


def verUsuariosController():

    return seleccionarUsuarios()


# creamos funcion para eliminar usuarios de una base de datos/////////////////////////////

def eliminarUsuariosController(id):
    
    try:
        id = int(id)
        eliminarUsuariosModel(id)
        print("Se elimino el usario..")
        return True
        input()

    except:
        print("Por favor ingrese un id valido. ")
        return False


def seleccionarUsuarioController(id):
    if len(id) != 0:
        datos = seleccionarUsuario(id)
        if  len(datos) !=0:
            return datos
        else:
            print("Por favor ingrese un id valido. ")
            return False

    else:
        print("Por favor ingrese un id valido. ")
        return False

#controlador paa modicar usuario //////////////////////////////////
def modificarUsuarioController(datos, id):
    return modificarUsuariosModel(datos, id)