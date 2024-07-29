import mysql.connector as sql   # to import mysql connector
mycon=sql.connect(host='localhost', user='root', password='12345678',database='hubnet') # create connection profile with sql server
mycur=mycon.cursor()            # to create an object of cursor that will allow us to run any sql query from python.
q='select * from login'              # to store an sql query in local varibale q.
mycur.execute(q)                # to execute the query that has been stored in q varibale
lod=mycur.fetchall()            # to featch all records or list from memory buffer and stored in local variable lod.
for i in lod:
    print(i)

