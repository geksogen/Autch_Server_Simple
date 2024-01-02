docker-compose build --build-arg client
docker-compose build --build-arg autch_server
docker-compose build --build-arg api_server
docker-compose up -d client
docker-compose up -d autch_server
docker-compose up -d api_server
docker-compose ps
