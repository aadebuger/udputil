import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 8888

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(10) # buffer size is 1024 bytes
    print("received message:", data)
    sock.sendto(bytes('hello', encoding = "utf8"),addr)  


