# PR-Lab2
Lab 2 for network programming course at university

# 70% check
The program has is using 6 protocols. TCP, UDP, HTTP, and FTP are used for communication to the chatbot server.
Each of these four protocols have a different client.

You type 'email receiver@gmail.com' to email the chat history to the specified receiver email.
Email is sent with the help of the SSL and SMTP protocols. SSL is used to make a ssl context that the smtp uses when sending an email.
SSL context is used because i couldn't use smtp without it.
# 40% check
The program is using 3 protocols to transmit a message to the 3 corresponding servers from the chat.
The chat is currently only answering with received_message+"THIS IS THE RESPONSE".
The used protocols are TCP, UDP, HTTP

Run chat.py file to start the chat servers.  

Run each client file to send one "Hello, World! FROM X " message. Check the chat console to see what it received and from where.
