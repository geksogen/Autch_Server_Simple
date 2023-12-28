## Autch_Server_Simple
Stand for demonstrating authentication mechanics, autorisation on jwt token.
### Architecture

### Data flow diagram

### Deploy
* Ubuntu 22.04
* Python 3.9
* Docker 20.10
### Client
```BASH
git clone https://github.com/geksogen/Autch_Server_Simple
cd Autch_Server_Simple/Client/
#gunicorn --bind 0.0.0.0:5000 wsgi:app
sudo docker build -t client:1 .
#sudo docker run --rm -d -p 5000:5000 client:1
sudo docker run --rm -d --name client_my --network=host client:1
```
### Auth Server
```BASH
git clone https://github.com/geksogen/Autch_Server_Simple
cd Autch_Server_Simple/Autch_server/
sudo docker build -t auth_server:1 .
sudo docker run --rm -d --name autch_server_my --network=host auth_server:1
```

### Clear
```BASH
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -q)
```
