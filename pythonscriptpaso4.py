import requests
import json

url = "https://192.168.152.129/restconf/data/ietf-interfaces:interfaces/interface=Loopback55"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback55",
    "description": "Catalina Gonzalez",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "172.16.55.1",
          "netmask": "255.255.255.0"
        }
      ]
    }
  }
})
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
