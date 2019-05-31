import pandas as pd
import sqlite3
from sqlalchemy import create_engine

"""
Before that:

$ brew install sqlite
$ sqlite3 test.db
sqlite> .tables
sqlite> .exit
$ ls
test.db

"""


if __name__ == '__main__':
	engine = create_engine('sqlite:///test.db')


	#load table
	table_name = 'test_metadata_table'
	
	try:
		df = pd.read_sql_table(table_name, con=engine)
		print(df)
	except:
		pass

	#insert into table
	a = []
	x = ['tmp', 'test']
	a.append(x)
	df = pd.DataFrame(a, columns=['filename', 'hash'])

	df.to_sql(table_name, con=engine, if_exists='append', index=False)



