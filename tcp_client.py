import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World! FROM TCP "

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print("Connection successful")

    data = s.send(bytes(MESSAGE, encoding='utf8'))
    response = s.recv(BUFFER_SIZE)

    print("Bytes sent:", data)
    response_str = response.decode("utf-8")
    print("Sent:", str(MESSAGE))
    print("Received:", response_str)
    s.close()
