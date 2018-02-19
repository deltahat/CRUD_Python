# -*- coding: utf-8 -*-
nombre = raw_input("ingrese nombre: ")
apellido = raw_input("ingrese apellido: ")

import MySQLdb

# Conectar
bd = MySQLdb.connect("127.0.0.1","root","","escuela" )


# Creamos el cursor
cursor = bd.cursor()


# Altas
sql = "INSERT INTO alumnosbizarros VALUES "
sql+="('%s', '%s', 22, 'M');"%(nombre, apellido)


# Ejecutamos el comando
cursor.execute(sql)


# Efectuamos los cambios en la base de datos
bd.commit()


# Nos desconectamos de la base de datos
bd.close()