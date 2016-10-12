# Call a daemon via REST API

With this simple script you can run processes via REST with authentication.
It will write the actual time to output.txt even if the "parent" process dies.

Python3
python_deamon
REST: Flask

START with: 
http://localhost:5000/perform?action=start

STOP with: 
http://localhost:5000/perform?action=stop

RESTART with: 
http://localhost:5000/perform?action=restart

