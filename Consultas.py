# -*- coding: utf-8 -*-

import MySQLdb

# Conectar
bd = MySQLdb.connect("127.0.0.1","root","","escuela" )


# Creamos el cursor
cursor = bd.cursor()


# Consultar
sql = "SELECT * FROM alumnos"


# Ejecutamos el comando
cursor.execute(sql)


# Obtenemos todos los registros en una lista de listas
resultados = cursor.fetchall()
for registro in resultados:
    nombre = registro[0]
    apellido = registro[1]
    edad = registro[2]
    sexo = registro[3]


# Imprimimos los resultados obtenidos
print "nombre=%s, apellido=%s, edad=%d, sexo=%s," % (nombre, apellido, edad, sexo)


# Nos desconectamos de la base de datos
bd.close()
