#!/usr/bin/env python
 
import sys, time
from daemon_class import Daemon

class MyDaemon(Daemon):
	def run(self):
		# daemon running from / so you have to maually set wd
		wd = '/home/balint/workspace/useful_python_scripts/call_a_deamon_via_rest'
		with open( wd + "/output.txt", "w") as f:
				f.write("This is the beginning...")
		time.sleep(5)
		while True:
			with open( wd + "/output.txt", "w") as f:
				f.write("The time is now: " + time.ctime())
			time.sleep(1)
 
if __name__ == "__main__":
	daemon = MyDaemon('/tmp/daemon-example.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print("Unknown command")
			sys.exit(2)
		sys.exit(0)
	else:
		print("usage: %s start|stop|restart" % sys.argv[0])
		sys.exit(2)