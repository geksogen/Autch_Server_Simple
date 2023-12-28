cd /Client/
sudo docker build -t client:1 .
sudo docker run --rm -d --name client_my --network=host client:1

cd ../Autch_server/
sudo docker build -t auth_server:1 .
sudo docker run --rm -d --name autch_server_my --network=host auth_server:1

cd ../API_server/
sudo docker build -t api_server:1 .
sudo docker run --rm -d --name api_server_my --network=host api_server:1

docker ps:
