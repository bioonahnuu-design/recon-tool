import socket 
import subprocess

target = input("Masukkan domain: ")

# Get IP 
ip = socket.gethostbyname(target)
print("\n[+] IP Address:", ip)

# WHOIS 
print("\n[+] WHOIS Info:")
subprocess.call(["whois", target])

#DNS Lookup 
print("\n[+] DNS Info:")
subprocess.call(["nslookup", target])
