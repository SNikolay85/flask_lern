import requests

# response = requests.post('http://127.0.0.1:8000/users/',
# json={'name': 'user_2', 'password': 'sdds475'})

# response = requests.get('http://127.0.0.1:8000/users/6')

# response = requests.patch('http://127.0.0.1:8000/users/1',
#                          json={'name': 'user_1'})
#
# print(response.status_code)
# print(response.text)

response = requests.delete("http://127.0.0.1:8000/users/1")

print(response.status_code)
print(response.text)

response = requests.get("http://127.0.0.1:8000/users/1")

print(response.status_code)
print(response.text)
