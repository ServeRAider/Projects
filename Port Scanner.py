# Portscanning.py
"""

Purpose: My first real Cyber Security application: a Port Scanner

Design: Ask for an IP Address or Domain Name
Ask for beginnning port number
Ask for Ending port number 
Scan the ports to see if they are open 



"""

import socket # socket module is used for port communication
target_port = 80
target_name = str(input("Please enter the IP or Domain you would like to scan: "))  #domain or address (can type in IP address)
startport= int(input("Enter the port you would like to begin your scan with: ")) # User picks starting port number
endport= int(input("Enter the port you would like to end your scan with: ")) # User picks ending port number
target_ip = socket.gethostbyname(target_name) #gethostbyname allows me to get the ipaddress

print (f"IP Address is: {target_ip}")

#creating a socket on my local machine and getting it ready to talk to the target machine 
#AF_INET means that use the IPv4 address
#SOCK_STREAN is the TCP protocol
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.settimeout(1)

#connect mysock to the target port -give it the IP number and the port number 
#This fuction returns 0 if function is good, else returns error number 
# print (f" Result is : {mysock.connect_ex((target_ip, 23))}")
for target_port in range (startport,endport + 1):
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.settimeout(10) #timeout is from your end and has to be set judiciously
    if mysock.connect_ex((target_ip, target_port)) == 0:
        print(f"For ip address: {target_ip} port: {target_port} is open ")
    else: 
        print(f"Port {target_port} is closed")
