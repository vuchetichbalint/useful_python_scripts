docker run --name jupyter_nb -p 8888:8888 -dit -e USE_HTTPS=true jupyter/all-spark-notebook start-notebook.sh

#open in browser -> new kernel -> run (sic!):
from notebook.auth import passwd
passwd()

#copy the result hash (it's public)
'sha1:80cfc8c0ea27:86c97243229abca32a038e19bcd0e0310d487226'

#back to the terminal, and restart the container
JUPYTER_NB_SERVER=`docker ps | grep jupyter_nb | awk '{print $1}'`

docker rm -f $JUPYTER_NB_SERVER

docker run --name jupyter_nb -p 8888:8888 -dit -e USE_HTTPS=true jupyter/all-spark-notebook start-notebook.sh --NotebookApp.password='sha1:80cfc8c0ea27:86c97243229abca32a038e19bcd0e0310d487226'
JUPYTER_NB_SERVER=`docker ps | grep jupyter_nb | awk '{print $1}'`

# now it should work via browser at https://localhost:8888

#if you want to login: 
docker exec -it $JUPYTER_NB_SERVER /bin/bash

#at the end kill it with:
docker rm -f $JUPYTER_NB_SERVER
