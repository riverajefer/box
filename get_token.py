import requests

url = "http://132.148.146.12/RestApiOOps/token"

payload = "grant_type=password&UserName=&Password="
headers = { 'content-type': "application/x-www-form-urlencoded"}

response = requests.request("POST", url, data=payload, headers=headers)

print (response.text)