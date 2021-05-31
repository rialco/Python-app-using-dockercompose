try:
    conn = mysqlc.connect( host=hostname, user=username, passwd=password, db=database )
    if conn.is_connected():
        cursor = conn.cursor()
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO casos_covid (ciudad, edad, sexo, estado) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)