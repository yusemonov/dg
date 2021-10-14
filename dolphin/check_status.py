import requests

url = "https://finnyheder.com/new/accounts/"

payload = ""
headers = {
    'Authorization': '1-c1df40635d8ee80097645ec1e003c99e',
    'Content-Type': 'application/json'
}

response = requests.request(
    "GET", url, headers=headers, data=payload).json()
for d in response['data']:
    print(d['status'])
