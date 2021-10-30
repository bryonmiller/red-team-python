import ipaddress # For IP address manipulation
import csv
import requests # Requests allows for HTTP requests to be used in the program

# Set URL for API to variable
apiurl = 'https://api.ipgeolocation.io/ipgeo?apiKey='

# Get IP(s) from file
with open('ips.txt', 'r') as ipf:
    iplist = ipf.readlines()

# Open results file (added to .gitignore) for writing and create csv writer
sdf = open('scopedata.csv', 'w')
csv_writer = csv.writer(sdf)

# Retrieve API token (this file should also be added to .gitignore)
with open('apitoken.txt', 'r') as apitf:
    apitoken = apitf.readlines()

# Function to request data for each IP and write to csv
def scope_query():
    print("Collecting data and writing to scopedata.txt. Please wait.")
    for i in iplist:
        if '/' in i: # Check for CIDR
            addrs = ipaddress.ip_network(i.replace("\n",'')) # Generate network IPs and remove lines
            for addr in addrs:
                data = requests.get(apiurl+apitoken[0]+'&ip='+str(addr)).json()
                csv_writer.writerow(data.values())
        else:
            data = requests.get(apiurl+apitoken[0]+'&ip='+i).json()
            csv_writer.writerow(data.values())

scope_query()

sdf.close() # Close the written data file

print("Scope query complete. See scopedata.txt for results.")