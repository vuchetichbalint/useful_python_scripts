from datetime import datetime, date, timedelta
import pandas as pd

def date_lagger(date, lag):
    d = datetime.strptime(day, '%Y-%m-%d').date()
    d += timedelta(days=lag)
    return d.strftime('%Y-%m-%d')

def duplicate_last_rows():
	df = pd.DataFrame({'col1':list("abc"),'col2':range(3)},index = range(3))
	df_2 = df[df['col2']>0]
	df_3 = df.append([df_2]*2, ignore_index=True)

def use_database():
	"""	Before that:
	$ brew install sqlite
	$ sqlite3 test.db
	sqlite> .tables
	sqlite> .exit
	"""
	import sqlite3
	from sqlalchemy import create_engine
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

def manipulate_pandas_plot(df):

	ax = df.plot()
	ax.set_xlabel("time")
	ax.set_ylabel("speed")

	plt.plot()

def apply_return_multiple rows():
	#   one  two
	#0    3    a
	#1    5  b,c
	# #becomes:
	#   one  0
	#0    3  a
	#1    5  b
	#2    5  c
	df = pd.DataFrame([{'one': 3, 'two': 'a'}, {'one': 5, 'two': 'b,c'}])
	df2 = pd.concat([df['one'], pd.DataFrame(df['two'].str.split(',').tolist(), index=df.index)], axis=1)
	df3 = df2.set_index('one').unstack().dropna().reset_index(level=1).reset_index(drop=True)

if __name__ == '__main__':

	pass




