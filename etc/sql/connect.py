import pandas as pd
from sqlalchemy import create_engine

#postgresql://user:pass@host:port/db
engine = create_engine('postgresql://')


#load table
table_name = 'test_metadata_table'
df = pd.read_sql_table(table_name, con=engine)
print(df)

#insert into table
a = []
x = ['tmp', 'test']
a.append(x)
df = pd.DataFrame(a, columns=['filename', 'hash'])

df.to_sql(table_name, con=engine, if_exists='append', index=False)



