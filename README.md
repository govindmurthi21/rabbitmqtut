# Instructions

## SET UP RABBIT MQ VIA DOCKER

1. [Download docker desktop](https://www.docker.com/products/docker-desktop/) =
2. Start Docker Desktop
3. Run Command `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management`
4. Run Command `python -m venv .`
5. Run Command `pip install -r requirements.txt`
6. Launch Debug. 
7. Use postman or similar to produce a message POST http://localhost:8000/message {"message": "This is the first message", "insertDate": "09/17/2024"}
