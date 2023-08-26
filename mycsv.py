import os
import mysql.connector
import pandas

cnx = mysql.connector.connect(user='root',
                              password='er123456',
                              host='127.0.0.1',
                              database='test'
                              )

query = "SELECT * FROM carsData;"
cursor = cnx.cursor()
cursor.execute(query)
result = cursor.fetchall()

# convert mysql to csv
df = pandas.DataFrame()


for i in result:
    d2 = pandas.DataFrame(list(i)).T
    df = pandas.concat([df, d2])

df.to_csv('_______.csv')