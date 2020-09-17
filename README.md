# Pub-Server

* Using python, flask to build the publisher server api;
* Port number is 6000. To test app after run start-server.sh, (if there is an error, try chmod +x);
* After run ./start-server.sh, using terminal or postman;

## Test result

1. curl -X POST -H "Content-Type: application/json" -d '{"url": "http://localhost:8000/event"}' http://localhost:6000/subscribe/topic1
2. curl -X POST -H "Content-Type: application/json" -d '{"message": "hello"}' http://localhost:6000/publish/topic1
3. (/event endpoint) curl -X GET http://localhost:6000/event