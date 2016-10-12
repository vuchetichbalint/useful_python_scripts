# Call a daemon via REST API

With this simple script you can run processes via REST with authentication*.

It will write the actual time to output.txt even if the "parent" process dies.

- Python3
- python_deamon
- REST: Flask

After running this:
```
python app.py
```

START with:
```
http://localhost:5000/perform?action=start
```

STOP with: 
```
http://localhost:5000/perform?action=stop
```

RESTART with: 
```
http://localhost:5000/perform?action=restart
```

\* The authentication is diabled for trying, but you can easily uncomment it (@auth.login_required).

