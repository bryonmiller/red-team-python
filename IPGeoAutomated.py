import requests # Requests allows for HTTP requests to be used in the program
import ipaddress # For IP address manipulation
from pprint import pprint # Pretty print formatting

# Creating variable to hold the IP and asking user for input
# ip = input("What IP would you like to check? ")

# Get IP(s) from file
f = open("ips.txt","r")
ip = f.readlines()

# For loop to request data for each IP
def scopeQuery():
    for i in ip:
        if '/' in i:
            addrs = ipaddress.ip_network(i.replace("\n",'')) # Check for CIDR and remove lines
            for addr in addrs:
                data = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=API_TOKEN&ip='+str(addr)).json()
                print(data)
        else:
            data = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=API_TOKEN&ip='+i).json()
            print (data)

scopeQuery()

# For use with a single IP entered by the user
# print (requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=API_TOKEN&ip='+ip).json())