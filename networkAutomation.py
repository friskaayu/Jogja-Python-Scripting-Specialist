'''
1. Membuat user interaktif dimana ketika user masuk bisa input IP Address, Username, Password
2. Kemudian user bisa pilih
    -nulis command seperti SSH
    -upload file configuration

'''

from netmiko import ConnectHandler
import getpass
import socket
import sys
import os

ip = input("Ip : ")
username = input("Username : ")
password = input("Password : ")
linux = {
    'device_type':'linux',
    'ip':ip,
    'username':username,
    'password':password,
    'port':22,
    'verbose':True
}

connection = ConnectHandler(**linux)
connection.enable()
print(" Ketik 1 untuk nulis command seperti SSH")
print(" Ketik 2 untuk upload file configuration")
a = int(input("Masukan Pilihan (1/2) : "))
if a == "1":
    while True:
        co = input('Command : ')
        output = connection.send_command(co)
        print(output)
        co = ''
elif a == "2":
    b = input("upload nama file dan directorynya : ")
    with open(b,"rb") as b:
    data = b.read()
    print(data)
    b = ''
else:
    print("masukan salah")
connection.disconnect()