import pandas as pd
import sqlalchemy
import urllib

DB_CONNECTION = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:10.222.10.4,1433;Database=DWH_IOT;trusted_connection=yes;'

quoted_conn_str = urllib.parse.quote_plus(DB_CONNECTION)
engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted_conn_str))

df = pd.read_sql(
        sql='''SELECT TOP 1000 * FROM [DWH_IOT].[DWH].[T_Astrata_Positions]''',
        con=engine
        )

print(df)

