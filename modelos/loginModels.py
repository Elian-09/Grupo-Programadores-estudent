from dataSource.mysqlconect import MysqlConect

conexion = MysqlConect("localhost", "root", "","cursopython" )

def consultarIniciarSesion(datos):
    
    sql = """
    SELECT * FROM `usuarios` 
    WHERE 
        `nombre` like "{0}" AND 
        `contrasenha` like "{1}"
    """.format (datos[0], datos[1] )


    return conexion.getData(sql)

#/////////////////////////////////////////////////////////////////////////////////////////
# funcion para registrar o agregar un usuario en la base de datos, 

def registrarUsuariosmodelos(datos): 
    sql = """
        INSERT INTO `usuarios` 
            (`id`, `nombre`, `contrasenha`, `telefono`) 
        VALUES 
            (NULL, '{0}', '{1}', '{2}');
    """.format (datos[0], datos[1], datos[2])
    return conexion.query(sql)