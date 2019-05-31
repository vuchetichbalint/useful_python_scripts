docker run \
    --name neo4j -dit \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    neo4j



http://ccnet1.tmit.bme.hu:7474/
user: neo4j
pass: kutya4