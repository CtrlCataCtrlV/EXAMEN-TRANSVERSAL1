import requests
import json

url = "https://192.168.152.129/restconf/data/ietf-interfaces:interfaces/interface=Loopback44"

payload = ""
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
