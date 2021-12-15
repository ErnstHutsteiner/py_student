# basic example with pyodbc
import pyodbc
import pandas as pd

class Mssql:
    """
    This class handles access and data exchange to MSSQL.
    """
    def __init__(self):
        """
        Execute a query with given parameters

        Arguments:
            query {str}
        Returns:
            dataset
        """
        try:
            self.__db_connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                    'Server=erniessqlbox\INST1;'
                    'Database=Adventure;'
                    'UID=sepp;'
                    'PWD=sepp;')
            self.__db_cursor = self.__db_connection.cursor()        
        except:
            raise

    def query(self, query):
        try:
            response = self.__db_cursor.execute(query)
        except:
            response = '{"record": "failed by exception"}'
            raise
        return response    


    def pandas_query(self, query):
        try:
            query_result = pd.read_sql_query(query, self.__db_connection)
        except:
            raise
        return query_result


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__db_cursor.close()
        self.__db_connection.close()


    def __enter__(self):
        return self