import mysql.connector
from data import nameList,subModelList, yearList, newPriceList, exteriorColor, interiorColor, wheelDriveType,useTypeList, cityList, transmissionType, distanceList,engineType,fuelTypeList

# connect to database
cnx = mysql.connector.connect(user='root',
                              password='er123456',
                              host='127.0.0.1',
                              database='test'
                              )

cursor = cnx.cursor()

val = list(zip(nameList,subModelList,yearList,newPriceList,exteriorColor,interiorColor,wheelDriveType, useTypeList,cityList ,transmissionType, distanceList,engineType,fuelTypeList))

sql = "INSERT INTO carsData (name, submodel, year, price, ecolor, icolor, wd, usetype, city, tra, " \
      "dis, eng, fuel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
cursor.executemany(sql, val)

cnx.commit()
cnx.close()


