# HTTP

-   Typical web application has clients and servers
    -   [Client](g:client) initiates communication by sending a message and waiting for a response
    -   [Server](g:server) waits for requests and then replies to them
-   Communicate using [Internet Protocol](g:ip) (IP), and specifically [Transmission Control Protocol](g:tcp) (TCP/IP)
    -   Makes communication between computers look like reading and writing files
-   A [socket](g:socket) is one end of a point-to-point channel
    -   Consists of an IP address (identifies machine) and a port on that machine
    -   [IP address](g:ip-address) is four 8-bit numbers(e.g., `93.184.216.34`)
    -   [Domain Name System](g:dns) (DNS) matches these to symbolic names like `example.com`
    -   [Port](g:port) is a number in the range 0-65535
    -   Only one process can use a port at a time

## Using Sockets

-   `socketserver` module provides:
    -   `TCPServer` class to manage incoming connections
    -   `BaseRequestHandler` class that does everything except process the incoming data
-   `TCPServer` creates a new handler each time it gets a connection and calls that object's `handle` method
-   [`simple_server.py`](./simple_server.py) reads up to 1024 bytes of data and returns a message

```{file="simple_server.py"}
"""Basic socket server."""

import socketserver


CHUNK_SIZE = 1024
SERVER_ADDRESS = ("localhost", 5000)


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(CHUNK_SIZE)
        cli = self.client_address[0]
        msg = f"server received {len(data)} bytes from {cli}"
        print(msg)
        print(data)
        self.request.sendall(bytes(msg, "utf-8"))


if __name__ == "__main__":
    server = socketserver.TCPServer(SERVER_ADDRESS, MyHandler)
    server.serve_forever()
```

-   Use [netcat][netcat] to open a connection and send some text with [`send_with_nc.sh`](./send_with_nc.sh)

```{file="send_with_nc.sh"}
echo "testing" | nc 127.0.0.1 5000
```

## HTTP Request and Response

-   [HyperText Transfer Protocol](g:http) (HTTP) is deliberately simple
    -   Send [request](g:http-request) with path, headers, and body
    -   Get [response](g:http-response) with status, headers, and content
-   Minimal request is just `GET /index.html HTTP/1.1`
    -   Method
    -   Path
    -   Protocol version
-   [`http_request_headers.txt`](./http_request_headers.txt) shows more realistic request

```{file="http_request_headers.txt"}
```

-   [`http_response.txt`](./http_response.txt) shows possible response

```{file="http_response.txt"}
```

-   [`http_server.py`](./http_server.py) responds to `GET` with same page every time.

```{file="http_server.py"}
```

[netcat]: https://en.wikipedia.org/wiki/Netcat
