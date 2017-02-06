import pandas as pd

header_file = pd.read_csv('header.csv').iloc[0:0,]
importand = pd.read_csv('importand.csv', sep=';',  dtype={'Phone 1 - Value': object})

importand['Phone 1 - Value'] = importand['Phone 1 - Value'].apply(lambda x: x.replace('(', '').replace(')', '').replace(' ', '').replace('-', ''))

importand['Phone 1 - Type'] = 'Mobile'
importand['Given Name'] = importand['Name']
importand['Group Membership'] = '* My Contacts'


res = pd.merge(header_file, importand, how='outer')
res = res[header_file.columns]

res.to_csv('output.csv', sep=',', index=False)