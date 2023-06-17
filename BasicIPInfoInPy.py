import requests
import json

def get_ip_information(ip):
    url = f"http://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def save_results(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

ip = input("Enter the IP address: ")

information = get_ip_information(ip)

if information:
    save_results(information, "results.json")
    print("The information has been saved to 'results.json'.")
else:
    print("Failed to obtain information for the specified IP address.")
