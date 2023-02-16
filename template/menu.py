# funcion o interfas para el menu de opciones *************************************
def menu():

    opcion = input("""
                    
            __..._   _...__
        _..-"      `Y`      "-._
        \ Once upon |           /
        \\  a time..|          //
        \\\         |         ///
        \\\ _..---.|.---.._ ///
            \\`_..---.Y.---.._`//
            '`               `'

                    menu: 


>1: iniciar sesion
>2: Registrarse
>0: salir

opcion: """)

    return opcion


#funcion o interfas para salir de la app ******************************************************

def salir():
     print("""
     
         .===========.        
         |   |       |        
         |  /|\      |        
         | /a|d\     |        
         |___________|        
         |_________-_|_,-.    
         [_____________]   )   
        .,,,,,,,,,, ,,.  (_   
        /,,,,,,,,,,, ,,,\ (>`\ 
        (______.-``-._____) \__)

Gracias por usar nuestra aplicacion 
""")