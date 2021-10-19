import requests # Requests allows for HTTP requests to be used in the program
from pprint import pprint # Pretty print formatting

# Creating variable to hold the IP and asking user for input
# ip = input("What IP would you like to check? ")

# Get IP(s) from file
f = open("ips.txt","r")
ip = f.readlines()

# For loop to request data for each IP
for i in ip:
    data = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=API_TOKEN&ip='+i).json()
    pprint(data)

# For use with a single IP entered by the user
# print (requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=f80001219f4e463494bcfd2fb08b92a3&ip='+ip).json())
