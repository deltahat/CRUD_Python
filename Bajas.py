# -*- coding: utf-8 -*-

import MySQLdb

# Conectar
bd = MySQLdb.connect("127.0.0.1","root","","escuela" )


# Creamos el cursor
cursor = bd.cursor()


#Bajas
sql = "DELETE FROM alumnos WHERE APELLIDO='mendez'"


# Ejecutamos el comando
cursor.execute(sql)


# Efectuamos los cambios en la base de datos
bd.commit()


# Nos desconectamos de la base de datos
bd.close()