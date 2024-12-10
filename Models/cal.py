import mysql.connector

class CalculadoraModelo:

    def __init__(self):
      self.conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="calculadora",
        )
      self.cursor = self.conexion.cursor()

    def operaciones(self,numero1,operador,numero2):
       consulta = "INSERT INTO  operaciones (numero1,operador,numero2) VALUES (%s,%s,%s)"
       self.cursor.execute(consulta,(numero1,operador,numero2))
       self.conexion.commit()

    def resultado(self,resultado):
       consultaResultado = "INSERT INTO resultados (resultado) VALUES (%s)"
       self.cursor.execute(consultaResultado,(resultado,))
       self.conexion.commit()

    def Historial(self,id_operacion,id_resultado):
       consultaHistorial = "INSERT INTO resultados_operaciones (id_operacion,id_resultado) VALUES (%s,%s)"
       self.cursor.execute(consultaHistorial,(id_operacion,id_resultado))
       self.conexion.commit()

    def Ver_Historial(self):
       self.cursor.execute ("""SELECT rp.id AS ID, o.numero1, o.operador AS signo, o.numero2, r.resultado
FROM resultados_operaciones AS rp
JOIN operaciones AS o ON  rp.id_operacion = o.id
JOIN resultados AS r ON  rp.id_resultado = r.id""" )
       return self.cursor.fetchall()
       

    def ultimo_id(self):
       consultaid = "SELECT LAST_INSERT_ID()"
       self.cursor.execute(consultaid)
       return self.cursor.fetchone()[0]
    
    def cerrar_conexion (self):
       self.conexion.close()
       