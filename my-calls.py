import httpx

url = "https://automatic-disco-56pr9745w95c7pq6-5000.app.github.dev/"

response = httpx.get(url)
print(response.status_code)
print(response)

response = httpx.get(url)
print(response.status_code)
print(response.text)

mydata = {
    "text": "Hello Angel!",
    "param2": "Making a POST request",
    "body": "my own value"
}

# A POST request to the API
response = httpx.post(url + "echo", data=mydata)
print(response.status_code)
print(response.text)

auth_data = {
    "id": "angel.partida@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

# Print the response
response = httpx.post(url + "login", data=auth_data)
print(response.status_code)
print(response.text) 