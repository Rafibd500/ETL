print("Hello World")
import requests

url = "https://gateway7.diu.edu.bd/api/student/portal/result/semester?semesterId=82"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text)