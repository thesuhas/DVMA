import requests

url = "https://localhost:8082/api/sqlquery"

data = {"user_id": 1}

res = requests.post(url=url, json = data, headers = {'Content-type': 'application/json'})
print(res.text, res.status_code)