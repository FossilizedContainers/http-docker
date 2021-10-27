## HTTP Server inside a Docker Container

Simple example showing how to interact with an HTTP Server inside a Docker Container.

This uses the [`just`](https://github.com/casey/just#just) command runner, or you can run the commands listed in `justfile` manually.

```bash
# build the image
$ docker build -t jadonf/http-server .

# run the image & http server, binding it to 127.0.0.1:4000
$ docker run -p 4000:80/tcp -it jadonf/http-server

# (in a new terminal) run the client
$ python3 ./client.py
```
