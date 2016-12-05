docker run --name jupyter_nb -p 8888:8888 -dit -e USE_HTTPS=true jupyter/all-spark-notebook start-notebook.sh

#open in browser -> new kernel -> run (sic!):
from notebook.auth import passwd
passwd()

#copy the result hash (it's public)
'sha1:80cfc8c0ea27:86c97243229abca32a038e19bcd0e0310d487226'

docker rm -f jupyter_nb

docker run --name jupyter_nb -p 8888:8888 -dit -e USE_HTTPS=true -e GRANT_SUDO=yes --user root --volume=/home/balint/workspace/kaggle/bosh/input:/data jupyter/all-spark-notebook start-notebook.sh --NotebookApp.password='sha1:6d5aa18a7421:a13e12ad295753e507fed8f7ff7ccc6dd5c710c1'

# now it should work via browser at https://localhost:8888

#if you want to login: 
docker exec -it jupyter_nb /bin/bash

#at the end kill it with:
docker rm -f jupyter_nb
