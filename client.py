import requests

#response = requests.post('http://127.0.0.1:5000/users/',
                       #  json={'name': 'user_2', 'password': 'sdsdsds475'})

response = requests.get('http://127.0.0.1:5000/users/3')

print(response.status_code)
print(response.text)
