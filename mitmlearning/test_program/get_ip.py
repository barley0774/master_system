import socket

connect_interface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connect_interface.connect(("8.8.8.8", 80))
print(connect_interface.getsockname()[0])
connect_interface.close()