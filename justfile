_default:
    @just --list

# build the docker container
build:
    docker build -t jadonf/http-server .

# run the docker container with the http server
run-server: build
    docker run -p 4000:80/tcp -it jadonf/http-server

# run the http client connecting to the docker container
run-client:
    python3 ./client.py run static/run_metadata.json
