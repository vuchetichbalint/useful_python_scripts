https://hub.docker.com/r/tutum/mongodb/

#igy kell elinditani pl. 
# -d  = detached
# -v  = volume fel lehet mountolni egy mappat
# -p  = port (ebbol most a ccnet1...hu:28017-en lehet elerni kivulrol, a 27017 meg a native drive port)
docker run --name mongodb_source -d -p 27017:27017 -p 28017:28017 -v /home/balint/workspace/nav/penztargep-forgalom/infra/source_db:/data/db tutum/mongodb
docker run --name mongodb_target -d -p 27018:27017 -p 28018:28017 -v /home/balint/workspace/nav/penztargep-forgalom/infra/target_db:/data/db tutum/mongodb

# kilistazni [-a: ha az osszes letezo kell, nem csak a jelenleg futoak]
docker ps [-a]

# nyerjuk ki a container id-ket
SOURCE_SERVER=`docker ps | grep mongodb_source | awk '{print $1}'`
TARGET_SERVER=`docker ps | grep mongodb_target | awk '{print $1}'`
SPARK_SERVER=`docker ps | grep pyspark_mongo_nb | awk '{print $1}'`

# es igy lehet belelepni
docker exec -it $SOURCE_SERVER /bin/bash

docker exec -it $TARGET_SERVER /bin/bash

docker exec -it $SPARK_SERVER /bin/bash

# igy lehet megnezni az admin jelszot
docker logs $SOURCE_SERVER
docker logs $TARGET_SERVER
docker logs $SPARK_SERVER

# es igy lehet megolni oket:
docker rm -f $SOURCE_SERVER
docker rm -f $TARGET_SERVER
docker rm -f $SPARK_SERVER



jrXQiry19YBN

#???
#2ewZO9GcvsdW

#leiras: https://github.com/nabilm/pyspark_mongodb_nb/blob/master/README.md
docker run -d -p 8888:8888 -p 4040:4040 -p 4041:4041 -v /pysprak/:/pyspark --name pyspark_mongo_nb nabilm/pyspark_mongo_nb






mongoimport --db test --collection restaurants --file ~/primer-dataset.json



db.grantRolesToUser(
    "admin",
    [
      { role: "read", db: "admin" }
    ]
)


mongo --port 27017 -u admin -p jrXQiry19YBN --authenticationDatabase admin


mongo admin -u admin -p jrXQiry19YBN --port 27017

#
#https://docs.mongodb.com/v2.6/tutorial/add-admin-user/

use admin
db.createUser(
    {
      user: "superuser",
      pwd: "12345678",
      roles: [ "root" ]
    }
)






mongo admin -u superuser -p 12345678 --port 27017 --authenticationDatabase admin


mongoimport http://ccnet1.tmit.bme.hu:28017/admin -u superuser -p 12345678 --db test --collection restaurants --drop --file ~/primer-dataset.json




db.grantRolesToUser(
    "superuser",
    [
      { role: "readWrite", db: "test" }
    ]
)


readWrite
userAdmin
dbOwner
dbAdmin


http://stackoverflow.com/questions/23721866/mongodb-2-6-1-command-line-authentication-fails





mongoimport -u superuser -p 12345678 --db test --collection restaurants --drop --file ~/primer-dataset.json --authenticationDatabase admin

https://www.mongodb.com/blog/post/using-mongodb-hadoop-spark-part-3-spark-example-key-takeaways







use admin
db.createUser(
    {
      user: "balint",
      pwd: "123",
      roles: [ "userAdminAnyDatabase" ]
    }
)



mongo -u balint -p 123 --port 27017 --authenticationDatabase admin


#igy kell letrehozni:
http://stackoverflow.com/questions/20525103/what-mongodb-user-privileges-do-i-need-to-add-a-user-to-a-new-another-mongo-data

db.addUser({ user: "user", pwd: "1234", roles: ["readWrite"] })

#kell egy ilyen furcsa jog hozza
http://pauldone.blogspot.hu/2014/05/mongodb-connector-authentication.html

use test
db.updateUser("user", {
                   roles : [
                      { role: "readWrite", db: "test" },
                      { role : "clusterManager", db : "admin"  }
                   ]
              })




#ImportError: No module named 'bson'
apt-get update
apt-get install python-pip python-dev build-essential 
pip install --upgrade pip 
pip install --upgrade virtualenv




pip install bson
pip install mongoengine