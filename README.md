## Autch_Server_Simple
Stand for demonstrating authentication mechanics, autorisation on jwt token.
### Architecture

### Data flow diagram

### Deploy Client
```BASH
git clone https://github.com/geksogen/Autch_Server_Simple
cd /Autch_Server_Simple/Client
sudo docker build -t Client:1 .
sudo docker run --rm -d --name Client --network=host Client:1
```

### Clear
```BASH
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -q)
```