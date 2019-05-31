import time


def do_main_program():
	while True:
		time.sleep(1)
		f = open('output.txt', 'a')
		f.write("stuff")
		f.close()
	return 0