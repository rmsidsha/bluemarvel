from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)

# 127~ 은 자기 자신을 의미함
clientSock.connect(('127.0.0.1', 2001))

print("Checked connect")

clientSock.send('Test send'.encode('utf-8'))
print("Send message")

data = clientSock.recv(1024)
print("Received data: ", data.decode('utf-8'))
