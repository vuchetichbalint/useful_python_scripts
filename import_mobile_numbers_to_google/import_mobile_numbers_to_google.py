import pandas as pd


def normalize_number(x):
	if x[0] == '+':
		return x
	if x[:2] == '06':
		return '+36' + x[2:]
	if x[:2] == '36':
		return '+' + x
	if (x[:2] == '20') or (x[:2] == '30') or (x[:2] == '70'): 
		return '+36' + x
	raise Exception('Not valid number format:{}'.format(x))

header_file = pd.read_csv('header.csv').iloc[0:0,]
importand = pd.read_csv('importand.csv', sep=';',  dtype={'Phone 1 - Value': object})

importand['Phone 1 - Value'] = importand['Phone 1 - Value'].apply(lambda x: x.replace('(', '').replace(')', '').replace(' ', '').replace('-', '').replace('/', ''))
importand['Phone 1 - Value'] = importand['Phone 1 - Value'].apply(normalize_number)

importand['Phone 1 - Type'] = 'Mobile'
importand['Given Name'] = importand['Name']
importand['Group Membership'] = '* My Contacts'

res = pd.merge(header_file, importand, how='outer')
res = res[header_file.columns]

res.to_csv('output.csv', sep=',', index=False)