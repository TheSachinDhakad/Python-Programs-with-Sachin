import requests
# r = requests.get("https://www.google.com/")
# print(r.text)
# #
# print(r.status_code)

url = "https://www.google.com/"
data = "youtube.com"
r2 = requests.post(url=url , data=data)
print(r2)
print(r2.status_code)