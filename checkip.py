import os

from netmiko import ConnectHandler

user = os.environ["USER"]
password = os.environ["PASSWORD"]

devices = {
    "device_type": "cisco_ios",
    "ip": "192.168.69.201",
    "username": user,
    "password": password,
}

net_connect = ConnectHandler(**devices)
output = net_connect.send_command("show ip interface brief")
print(output)
