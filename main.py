from template.menu import menu, salir
from template.login import formularioInicioSesion
from template.formularioRegistro import formularioRegistro
import os
from controllery.usarioController import eliminarUsuariosController
from controllery.loginController import validarIncioSesion, registrarUsuariocontroller
from controllery.usarioController import verUsuariosController, seleccionarUsuarioController, modificarUsuarioController
from template.usuarios import verUsuarios, modificarUsarios, formularioModificarUsuarios
from template.inicio import inicio
from template.usuarios import borrarUsuarios
#/////////////////////////////////////////////////////////////////

while True:
    os.system("cls") # esto nos permite limpias la pantallas repetidas 

    opcion = menu() # menu de opciones


    if opcion == "1": #formulario de inicio de sesion

        datos =  formularioInicioSesion() # pedimos los datos de usuario
        
        if validarIncioSesion(datos) == False:# tomamos los datos que nos recoge el formulario de sesion y los validadmos si estan correctos
            print("usuario incorrecto, Vuelve a intentarlo.")
        else: 

            while True: # creamps while para que entre directamente a la sesion de inicio 
                os.system("cls") 

                opcion = inicio()

                if opcion == "1":
                    print("lista de usuarios")
                    
                    verUsuarios()
                    input("")

                elif opcion == "2":
                    print("Eliminar Usuarios: ")
                    verUsuarios()
                    eliminarUsuariosController(borrarUsuarios())
                    input()
                
                elif opcion == "3":
                    print("Modificar usuarios.")
                    verUsuarios()
                    id = modificarUsarios()
                    datos = seleccionarUsuarioController(id)
                    modificarUsuarioController( formularioModificarUsuarios(datos[0]), id )
                    input()

                elif opcion == "0":
                    print("Sesion finalizada...")
                    
                    input("")
                    break
                else:
                    print("por favor seleccione una opcion del menu. ")
                    
        input("")

    elif opcion == "2":   # opocion para validar el el registro de uina persona ////////////////////////////

        registrarUsuariocontroller( formularioRegistro() )
        input("presione Enter para continuar....")

    elif opcion == "0": # opcion de salir

        salir()
        break

    else: 
        print("---Por favor ingrese una opcion validad---")
        input("")