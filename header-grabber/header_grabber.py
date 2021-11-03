import csv
import requests

# Get URLs from file
with open('urls.txt', 'r') as urlf:
    urls = urlf.readlines()

# Open results file (added to .gitignore) for writing and create csv writer
sdf = open('headers.csv', 'w')
csv_writer = csv.writer(sdf)

def header_grabber():
    for u in urls:
        if 'https' in u:
            response = requests.get(u, allow_redirects=False)
            headers = response.headers
            csv_writer.writerow(headers.values())
        else:
            response = requests.get(u, allow_redirects=False)
            headers = response.headers
            csv_writer.writerow(headers.values())

if __name__ == "__main__":
    header_grabber()
else:
    sdf.close()
    exit()
