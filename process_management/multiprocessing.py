from multiprocessing import Pool

def f(params):
	df, _ = params
	return df



params = [(df1, 'asd'), (df2, 'asd'), (df3, 'asd'), (df4, 'asd'), (df5, 'asd'), (df6, 'asd'), (df7, 'asd')]

p = Pool(4)

iterator = p.imap(f, params)

results = []
for result in iterator:
	results.append(result)

results = pd.concat(results)