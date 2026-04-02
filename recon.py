import socket 

target = input("Masukkan domain: ")
ip = socket.gethostbyname(target)

print("IP Addres:", ip)
