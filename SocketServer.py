import socket

# Creating socket object with default values of INET addr and socket stream
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding socket to local address
server.bind(('0.0.0.0', 8080))
server.listen() # listening for connecctions


while True:
    conn, addr = server.accept() # accepts any connection received
    from_client = ''

    while True:
        data = conn.recv(4096) # conn.recv takes a number bytes to read from socket stream
        if not data:
            break
        dataFromClnt = data.decode()    
        from_client += dataFromClnt
        print(from_client)
        conn.send("I am SERVER \n".encode())

    conn.close() # closing connection
    print("client disconnected \\...")
