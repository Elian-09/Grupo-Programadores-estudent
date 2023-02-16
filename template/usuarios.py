from controllery.usarioController import verUsuariosController


def verUsuarios():

    for fila in  verUsuariosController():
        print(fila)



# creamos la vista para borrar el usuario //////////////////////////////////////////

def borrarUsuarios():

    id = input("Seleccione el Id de Usuario a borrar: ")
    
    return id



#creamos vista para modificar usuarios//////////////////////////////////////////

def modificarUsarios():

    id = input("Seleccione el Id de Usuario a modificar: ")
    
    return id


# interfas para pedir los datos que vamos a modificar
def formularioModificarUsuarios(datos):
    
    nombre = input("nombre " + datos["nombre"] + "por : ")
    contrasenha = input("contraseña " + datos["contrasenha"] + "por : " )
    telefono = input("telefono " + datos["telefono"] + "por : ")

    return [nombre, contrasenha, telefono] 