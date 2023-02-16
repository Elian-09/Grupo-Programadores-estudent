#formulario para regisrarse ////////////////////////////////////////////////////////////////////////////////////

def formularioRegistro():
    print("Area de registro, ingresa los datos solicitados. ")
    usuario = input ("Ingrese su usuario: ")
    contrasenha = int ( input(" ingrese una contraseña segura: "))
    telefono = input ("ingrese su numero de celular: ")

    return [usuario, contrasenha, telefono]
    

