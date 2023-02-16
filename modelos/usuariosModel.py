
# en esta sesion configuraremos para mostrar todos los usuarios que se encuentrar en la base de datos 

from dataSource.mysqlconect import MysqlConect

conexion = MysqlConect("localhost", "root", "","cursopython")

# seleccionar usuarios /////////////////////////////////////

def seleccionarUsuarios():
    sql = """
    SELECT * FROM `usuarios`

    """
    return conexion.getData(sql)


#consulta para eliminar un usuario de una base de datos/////////////////////////////////////////////////////


def eliminarUsuariosModel(id):
    sql = """
    DELETE FROM
     `usuarios` 
     WHERE 
     `usuarios`.`id` = {0}
    """.format(id)
    return conexion.query(sql)


# consulta para modificar usuarios /////////////////////////////////////////

def seleccionarUsuario (id):
    sql = """
    SELECT * FROM `usuarios`
    WHERE id like  "{0}"

    """.format(id)
    return conexion.getData(sql)



# consulta para modificar usuarios

def modificarUsuariosModel (datos, id):
    sql = """
    UPDATE `usuarios`
     SET 
        `nombre` = '{0}',
        `contrasenha` = '{1}', 
        `telefono` = '{2}' 
      WHERE 
            `usuarios`.`id` = {3}

    """.format(datos[0], datos[1], datos[2], id )
    return conexion.query(sql)