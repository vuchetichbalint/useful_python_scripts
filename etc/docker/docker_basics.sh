
# ez a regi szar:

docker run --hostname=antlypls/kafka --name kafka --privileged=true -t -i -v $HOME/SparkApp/Flafka2Hive:/app -e KAFKA="localhost:9092" -e ZOOKEEPER="localhost:2181" cloudera/quickstart:latest /usr/bin/docker-quickstart

docker run --hostname=quickstart.cloudera --name flume --link kafka:kafka --privileged=true -t -i -v $HOME/FlumeData:/app cloudera/quickstart:latest /usr/bin/docker-quickstart
docker run --hostname=quickstart.cloudera --name spark --link kafka:kafka --privileged=true -t -i -v $HOME/SparkApp/Flafka2Hive:/app cloudera/quickstart:latest /usr/bin/docker-quickstart

docker ps



KAFKA_SERVER=`docker ps | grep kafka | awk '{print $1}'`
FLUME_SERVER=`docker ps | grep flume | awk '{print $1}'`
SPARK_SERVER=`docker ps | grep spark | awk '{print $1}'`



docker exec -it $KAFKA_SERVER /bin/bash


$ kafka-topics.sh --create --zookeeper $ZOOKEEPER --replication-factor 1 --partitions 2 --topic twitter





# ezek itt az ujak:

docker run --name ubuntu  -t -i ubuntu /bin/bash




UBUNTU=`docker ps -a | grep ubuntu | awk '{print $1}'`

docker exec -it $UBUNTU /bin/bash

docker kill $UBUNTU

# ez csak kieg scalas cucc:

echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
apt-get update
apt-get install sbt







sudo apt-get install default-jre


sudo apt-get install python-software-properties
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update

sudo apt-get install oracle-java8-installer

update-alternatives --config java

vim /etc/environment

JAVA_HOME="YOUR_PATH"

source /etc/environment





curl -L https://dl.bintray.com/sbt/native-packages/sbt/0.13.11/sbt-0.13.11.tgz | tar xzv -C /opt -f -




