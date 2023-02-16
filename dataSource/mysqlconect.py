import pymysql.cursors

class MysqlConect():

    #creamos la variable que nos va a conectar a Mysql
    conexion = ""

    # creamos un metodo contructor para conectarnos a Myqsl
    def __init__(self, host, user, password, database):
        # nos conectamos a la base de datos (metodo contructor )

        self.conexion = pymysql.connect(host = host, # esta es  la ruta de la base de dato
                                    user = user, # por defecto es root
                                    password = password, # aca es opcional si se quiere agregar contraseña o de lo contrario se dja vacia
                                    database = database, # aca va  el nombre de la base de dato con la que se crea 
                                    cursorclass = pymysql.cursors.DictCursor)

    # optener datos de la base de datos (select) 
    def getData(self, sql): 

        cursor = self.conexion.cursor() # creamos variable para almacenar los datos de la conection de la base de datos que se configuro
        cursor.execute(sql) # aca ejecutamos la variable 
        return cursor.fetchall() # esto me muestra todo el resultado de la tabla de la base de dato
        

    # ejecutar consultas (insert, delete, update)
    def query(self, sql): 

        cursor = self.conexion.cursor() # creamos variable para almacenar los datos de la conection de la base de datos que se configuro
        cursor.execute(sql) # aca ejecutamos la variable 
        return self.conexion.commit() # esto me muestra todo el resultado de la tabla de la base de dato
        