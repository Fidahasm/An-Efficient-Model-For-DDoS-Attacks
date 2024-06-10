import requests

while True:
    res=requests.get("http://192.168.55.222:8001/")
    print(res.text)