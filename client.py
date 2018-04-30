import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.0.1', 9876)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print('sending "%s"' % message)
    sent = sock.sendto(bytes(message, encoding = "utf8"), server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4)
    print('received "%s"' % data)

finally:
    print( 'closing socket')
    sock.close()
