import socket
import threading

TCP_HOST = '127.0.0.1'
TCP_PORT = 8000

UDP_HOST = '127.0.0.1'
UDP_PORT = 8001


class Chat:
    def __init__(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.bind((TCP_HOST, TCP_PORT))

        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind((UDP_HOST, UDP_PORT))

    @staticmethod
    def get_response(string) -> str:
        return string + "THIS IS THE RESPONSE"

    def run(self):
        print("Starting server initialization")
        tcp_tread = threading.Thread(target=self.run_tcp)
        udp_thread = threading.Thread(target=self.run_udp)

        tcp_tread.start()
        udp_thread.start()

    def run_tcp(self):
        self.tcp_socket.listen()
        print("TCP Server initialized")
        while True:
            conn, _ = self.tcp_socket.accept()
            with conn:
                data = conn.recv(1024)  # Maximum message length is 1024 bytes
                if data:
                    # Converting the data from byte to string.
                    string_data = data.decode(encoding='utf-8')
                    print("Received via TCP:", string_data)
                    # Sending response
                    if string_data:
                        send_data = Chat.get_response(string_data)
                        conn.sendall(bytes(send_data, encoding='utf8'))
                        print("Sent back via TCP:", send_data)

    def run_udp(self):
        print("UDP Server initialized")
        while True:
            data = self.udp_socket.recvfrom(1024)  # Maximum message length is 1024 bytes
            if data:
                # Converting the data from byte to string.
                string_data = data[0].decode(encoding='utf-8')
                print("Received via UDP:", string_data)
                # Sending response
                if string_data:
                    send_data = Chat.get_response(string_data)
                    self.udp_socket.sendto(bytes(send_data, encoding='utf8'), data[1])
                    print("Sent back via UDP:", send_data)


if __name__ == '__main__':
    Chat().run()
