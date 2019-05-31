from ratelimiter import RateLimiter

@RateLimiter(max_calls=1, period=1)
def foo(i):
    print(i)

@RateLimiter(max_calls=5, period=10)
def bar(i):
    foo(i)

@RateLimiter(max_calls=1, period=1)
@RateLimiter(max_calls=5, period=10)
def foobar(i):
	print(i)

def a(i, rl):
	with rl:
		print(i)

if __name__ == '__main__':

	for i in range(100):
		foobar(i)
		
	exit()
	rate_limiter = RateLimiter(max_calls=1, period=1)
	for i in range(100):
		a(i, rate_limiter)


	# with decorator:
	for i in range(100):
		bar(i)

	# with context:
	rate_limiter1 = RateLimiter(max_calls=1, period=1)
	rate_limiter2 = RateLimiter(max_calls=5, period=10)

	for i in range(100):
	    with rate_limiter1:
	    	with rate_limiter2:
	        	print(i)



