## Autch_Server_Simple
Stand for demonstrating authentication mechanics, autorisation on jwt token.
### Architecture

### Data flow diagram

### Deploy
* Ubuntu 22.04
* Python 3.9
* Docker 20.10
```BASH
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

docker-compose build --build-arg client
docker-compose build --build-arg autch_server
docker-compose up -d

```

### Client
```BASH
git clone https://github.com/geksogen/Autch_Server_Simple
cd Autch_Server_Simple/Client/
#gunicorn --bind 0.0.0.0:5000 wsgi:app
sudo docker build -t client:1 .
#sudo docker run --rm -d --name client_my --network=host client:1
docker run -d -p 5000:5000 client:1

```
### Auth Server
```BASH
git clone https://github.com/geksogen/Autch_Server_Simple
cd Autch_Server_Simple/Autch_server/
sudo docker build -t auth_server:1 .
sudo docker run --rm -d --name autch_server_my --network=host auth_server:1
```

### API Server
```BASH
git clone https://github.com/geksogen/Autch_Server_Simple
cd Autch_Server_Simple/API_server/
sudo docker build -t api_server:1 .
sudo docker run --rm -d --name api_server_my --network=host api_server:1
```

### Clear
```BASH
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -q)
docker network prune
docker-compose down --rmi all -v --remove-orphans
```
