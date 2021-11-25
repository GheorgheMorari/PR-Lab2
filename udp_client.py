import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 8001
BUFFER_SIZE = 1024
MESSAGE = "Hello, World! FROM UDP "

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    data = s.sendto(bytes(MESSAGE, encoding='utf8'), (UDP_IP, UDP_PORT))
    response = s.recvfrom(BUFFER_SIZE)[0]

    print("Bytes sent:", data)
    response_str = response.decode("utf-8")
    print("Sent:", str(MESSAGE))
    print("Received:", response_str)
    s.close()
