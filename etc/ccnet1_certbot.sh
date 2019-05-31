sudo systemctl restart airflow-webserver.service
sudo systemctl restart airflow-worker.service
sudo systemctl restart airflow-scheduler.service
sudo systemctl restart airflow-flower.service

sudo systemctl restart rabbitmq-server.service

sudo systemctl restart gitlab-runsvdir
sudo systemctl restart gitlab-runner

# -----------------------------------------------------


sudo systemctl stop airflow-webserver.service
sudo systemctl stop airflow-worker.service
sudo systemctl stop airflow-scheduler.service
sudo systemctl stop airflow-flower.service

sudo systemctl stop rabbitmq-server.service

sudo systemctl stop gitlab-runsvdir
sudo systemctl stop gitlab-runner



cd /home/rbalazs/certbot/
./certbot-auto
# ...

sudo apt-get update
sudo apt-get install --only-upgrade gitlab-ce

sudo gitlab-ctl reconfigure
sudo gitlab-ctl restart


# kill nginx:
fuser -k 80/tcp
#elvileg kesz ¯\_(ツ)_/¯

sudo systemctl restart gitlab-runsvdir
sudo systemctl restart gitlab-runner

#ha nem, akkor:
gitlab-ctl tail



netstat -tulpn | grep :80
kill -9 <pid>

sudo systemctl restart nginx.service
sudo journalctl -u nginx.service
sudo fuser -k 80/tcp


sudo systemctl stop gitlab-runsvdir
sudo systemctl stop gitlab-runner
sudo systemctl stop nginx.service

# vegul:

sudo systemctl start airflow-webserver.service
sudo systemctl start airflow-worker.service
sudo systemctl start airflow-scheduler.service
sudo systemctl start airflow-flower.service

sudo systemctl start rabbitmq-server.service