import requests

url = "http://132.148.146.12/RestApiOOps/token"

payload = "grant_type=password&UserName=&Password="
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "960044e3-cac7-4e00-0b34-93c018e7c53e"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)