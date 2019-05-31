import time

def updateFunc(new_values, last_sum):
	last_sum[new_values['ts']]['count'] += 1 
	last_sum[new_values['ts']]['sum'] += new_values['price'] 
	return last_sum

def ts_to_mininweek(ts):

	ts = int(time.time())
	dt = datetime.fromtimestamp(ts)

	day = dt.weekday()
	
	mininweek = ((dt * 24) + dt.hour) * 60 ) + dt.min
	
	return mininweek


if __name__ == "__main__":

	print(ts_to_mininweek(123))
