import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost', 
                                                database='base_datos', 
                                                user='root', 
                                                password='')
        

    def busca_user(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos WHERE Users = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()
        return usersx
    
    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos WHERE Password = {}".format(password) #
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx
    
