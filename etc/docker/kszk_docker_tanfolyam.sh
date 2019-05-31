-d : detached vagy daemon, ne lepjen ki, ha mi kilepunk
-t : egyből terminálja
-i : interactive


docker webserver cluster

nginx

echo "cica" > index.html
ezt felcsatoljuk -v-vel ide: /usr/sharenginx/html:ro 
#:ro readolny
-p 80:80


docker network ls
#ide pakolja bele dinamikusan, majd letre kell hozni egy kulon halozatot, mert egyebkent nem engedni a statikus cimeket

HAProxy: tcp kapcsolatokat tud load-balanceolni

- HAProxy (192.168.10.21)
--- nginx (192.168.10.1)
--- nginx (192.168.10.2)


backeng web-servers
	balance roundrobin
	server web1 [ip]:80 check
	server web2 [ip]:80 check


docker file:
	semmi izgi


docker run --ip 192.168.10.21 --net webnetwork -p 1936:1936
-P : kihozza az osszes portot

docker network create -d bridge webnetwork --subnet 192.168.10.0/24 --gateway 192.168.10.254


docker compose:

docker mmgt:
	kubernetes / swarm