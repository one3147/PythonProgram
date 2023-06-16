import requests
url = "{BASEURL}"
file = open("./test.pnh","rb")
upload = {'file': file}
for i in range(1,101):
    res = requests.post(url, files=upload)
    print(res.status_code)
