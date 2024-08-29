import requests


url = "http://127.0.0.1:8000/articles/json-drf/"
# 이 url로 (GET 방식으로) call
response = requests.get(url) 

print(response)
print(response.json())