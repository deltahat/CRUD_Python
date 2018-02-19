# -*- coding: utf-8 -*-
import MySQLdb


def main():

# Conectar
    bd = MySQLdb.connect("127.0.0.1","root","toor","escuela" )




# Crear Tabla
    cursor = bd.cursor()

# Creamos la tabla alumnos
    sql = "CREATE TABLE alumnos (NOMBRE  CHAR(20) NOT NULL,APELLIDO  CHAR(20),EDAD INT,SEXO CHAR(1))"

    cursor.execute(sql)









# Altas
    sql = "INSERT INTO alumnos VALUES "
    sql+="('Carlos', 'mendez', 24, 'M'),"
    sql+="('Pedro', 'peres', 21, 'M'),"
    sql+="('Ramiro', 'gomez', 22, 'M');"

# Ejecutamos el comando
    cursor.execute(sql)
# Efectuamos los cambios en la base de datos
    bd.commit()




#·Bajas

    sql = "DELETE FROM alumnos WHERE APELLIDO='mendez'"

# Ejecutamos el comando
    cursor.execute(sql)
# Efectuamos los cambios en la base de datos
    bd.commit()




#Modificaciones

    sql = "UPDATE alumnos SET EDAD = EDAD + 300 WHERE APELLIDO = 'gomez'"

# Ejecutamos el comando
    cursor.execute(sql)
# Efectuamos los cambios en la base de datos
    bd.commit()




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

main()

# Conectar
    bd = MySQLdb.connect("127.0.0.1","root","","escuela" )

# Apuntar Tabla
    cursor = bd.cursor()

#---------------------------------------------------
# Altas
    sql = "INSERT INTO alumnos VALUES "
    sql+="('Draco Antonio', 'medialuno', 4, 'M'),"
    sql+="('Rubi', 'Fanenmanen', 5, 'F');"
 
# Ejecutamos el comando
    cursor.execute(sql)
# Efectuamos los cambios en la base de datos
    bd.commit()
#-------------------------------------------------




# Nos desconectamos de la base de datos
    bd.close()

main()


'''
#------------------------------------------
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
#--------------------------------------------------
'''