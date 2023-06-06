import requests
files = {"name":"mafe", "age":13}
response = requests.post('https:www.google.com', json=files)
print(response)
