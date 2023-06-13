import requests

url = "https://192.168.152.129/restconf/data/ietf-interfaces:interfaces"

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
