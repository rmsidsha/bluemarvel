from socket import *

# 소켓 셋팅
# 기본 socket 모듈을 불러 온 다음 소켓을 생성

# AF = Address Family: 주소 체계에 해당함
# INET = IPv4   ,  INET6 = IPv6를 의미
# SOCK_STREAM = 소켓 타입을 의미, STREAM과 DGRAM만이 주로 이용된다고 함
serverScok = socket(AF_INET, SOCK_STREAM)

# 소켓을 bind해 줌. 클라이언트 쪽에서는 불필요, 서버에서 필요
# 생성된 소켓의 번호와 실제 어드레스 패밀리를 연걸
# bind(())로 튜플을 인자로 줌, 첫번째는 ip주소, 뒷부분은 포트번호로
# 어드레스 페밀리는 (ip, port) 형식으로 한 쌍으로 구성된 튜플이다
# AF_INET일 때의 빈문자열은 INADDR_ANY를 의미, 모든 인터페이스와의 연결
# 8080포트에서 모든 인터페이스에게 연결하도록 한다
serverScok.bind(('', 2001))

# listen: 상대방의 접속을 기다리겠다.
# 서버 쪽에서 밖에 쓰이지 않음.
# 인자는 총 몇개의 동시접속을 허용할 것이냐는 뜻, 인자를 입력하지 않으면 파이썬에서 랜덤으로 숫자를 정함
serverScok.listen(1)


# 접속을 수락하고 그 후의 통신을 하는 단계
connectionSock, addr = serverScok.accept()
print("Checked from ", str(addr))

data = connectionSock.recv(1024)
print("Received data", data.decode('utf-8'))

connectionSock.send("Here is server".encode('utf-8'))
print("Send message")
