import mysql.connector
import pandas as pd

def database_connect(limit):
    mydb = mysql.connector.connect(host="localhost", user="root", password="mysql", port=3307 )
    cursor = mydb.cursor()
    cursor.execute('use fire_database')
    cursor.execute(f"Select * from fire LIMIT {limit}")
    result = cursor.fetchall()
    mydb.close()

    return result


