
from modelos.loginModels import consultarIniciarSesion
from modelos.loginModels import registrarUsuariosmodelos

#//////////////////////////////////////////////////////////////////

# esto controla si el usuario se encuentra registrado en la base de datos y nos devuelve la informacion 

def validarIncioSesion(datos):

    datosDeUsuario = consultarIniciarSesion(datos)

    if len(datosDeUsuario) != 0:
        return datosDeUsuario
    else:
        return False
   

#/////////////////////////////////////////////////////////////////////////
#creamos controlador para registrar un usuario 

def registrarUsuariocontroller(datos):

# nos falta crear aca crear la validacion de si existe un usuario con los mismos datos 
    return registrarUsuariosmodelos(datos)
