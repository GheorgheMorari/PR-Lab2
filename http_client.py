import http.client

HTTP_IP = '127.0.0.1'
HTTP_PORT = 8002
BUFFER_SIZE = 1024
MESSAGE = "Hello, World! FROM HTTP "
URL = HTTP_IP + ":" + str(HTTP_PORT)

if __name__ == '__main__':
    conn = http.client.HTTPConnection(HTTP_IP, HTTP_PORT)
    print("Connection successful")
    conn.request("GET", URL, bytes(MESSAGE, encoding='utf8'))
    response = conn.getresponse()

    response_str = response.read().decode("utf-8")
    print("Sent:", str(MESSAGE))
    print("Received:", response_str)
    conn.close()
