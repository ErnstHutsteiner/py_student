# basic example with pyodbc
from sqlalchemy import create_engine
import pandas as pd

class Myalc:
    """
    This class handles access and data exchange to MSSQL.
    """
    def __init__(self):
        self.server= "erniessqlbox\INST1"
        self.database= "Adventure"
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.uid = "sepp"
        self.pw = "sepp"
        try:
            self.__db_connection = f'mssql://{self.uid}:{self.pw}@{self.server}/{self.database}?driver={self.driver}'
            self.this_engine = create_engine(self.__db_connection)
            self.connection = self.this_engine.connect() 
        except:
            raise

    def query(self, query):
        try:
            response = pd.read_sql_query(query, self.connection)
        except:
            response = '{"record": "failed by exception"}'
            raise
        return response

this_q = Myalc()
my_query = "select top 10 FirstName, LastName, EmailPromotion from person.person"
retval = this_q.query(my_query)
print(retval)
