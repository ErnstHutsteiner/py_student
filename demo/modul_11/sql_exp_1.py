# basic example with pyodbc
import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                  'Server=erniessqlbox\INST1;'
                  'Database=Adventure;'
                  'UID=sepp;'
                  'PWD=sepp;')


SQL = "SELECT * FROM person.person"

print(SQL)
# wir führen eine Query aus
try:
    cursor = conn.cursor()
    response = cursor.execute(SQL)
    print(response.description)
    cursor.close()
    conn.commit()
finally:
    conn.close()