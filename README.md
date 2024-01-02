## Autch_Server_Simple
Stand for demonstrating authentication mechanics, autorisation on jwt token.
### Architecture

### Data flow diagram

### System requirements
* Ubuntu 22.04
* Docker-compose 20.10

### Docker-compose install
```BASH
sudo snap install docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### REQ
Set IP address to client.py
```Python
AUTH_PATH = 'http://<IP>:5001/auth'
TOKEN_PATH = 'http://<IP>:5001/token'
RES_PATH = 'http://<IP>:5002/users'
REDIRECT_URL = 'http://<IP>:5000/callback'
```

### Deploy
```BASH
git clone https://github.com/geksogen/Autch_Server_Simple
cd Autch_Server_Simple
sh ./deploy.sh
# 3 раза запустить :)
```
### Clear
```BASH
sh ./clear.sh
```
