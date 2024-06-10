from Conexion import *

class CClientes:

    def mostrarClientes():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from alumnos;")
            miResultado = cursor.fetchall()
            cone.commit
            cone.close()
            return miResultado


        except mysql.connector.Error as error:
            print("Error al ingresar datos {}".format(error))

    def ingresarClientes(nombres, apellidos, dni, fecha):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()  

            sql = "INSERT INTO alumnos (Nombre, Apellido, dni, fecha) VALUES (%s, %s, %s, %s);"
            valores = (nombres, apellidos, dni, fecha)

            cursor.execute(sql, valores)

            cone.commit()
            print(cursor.rowcount, "Registro ingresado")

            cursor.close()
            cone.close()

        except mysql.connector.Error as error:
            print("Error al ingresar datos: {}".format(error))
            
    
    def modificarClientes(codigo, nombres, apellidos, dni,fecha):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE alumnos SET Nombre = %s, Apellido = %s, dni = %s, fecha = %s WHERE codigo = %s;"

            valores=(nombres,apellidos,dni, fecha,codigo)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error de actualizacion datos {}".format(error))

    def eliminarClientes(codigo):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM alumnos WHERE codigo = %s;"

            valores=(codigo,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            cone.close()
        except mysql.connector.Error as error:
            print("Error de eliminacion datos {}".format(error))
            