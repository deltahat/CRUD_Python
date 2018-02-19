# -*- coding: utf-8 -*-

import MySQLdb

# Conectar
bd = MySQLdb.connect("127.0.0.1","root","","basededatos" )


# Crear Tabla
cursor = bd.cursor()


# Creamos la tabla alumnos
sql = "CREATE TABLE transacciones (ID INT NOT NULL AUTO_INCREMENT, FECHA VARCHAR(10) NOT NULL, NOMBRE CHAR(40),CODIGO VARCHAR(25),BRUTO VARCHAR(30),COSTO VARCHAR(30),NETO VARCHAR(100),ESTADO VARCHAR(20), PRIMARY KEY (ID))"


# Ejecutamos el comando
cursor.execute(sql)


# Nos desconectamos de la base de datos
bd.close()
