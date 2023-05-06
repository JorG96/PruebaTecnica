import requests


response = requests.get("http://localhost:8000/users")

print(response.json())

# [
#   {
#     "id": 1,
#     "name": "John Doe",
#     "email": "johndoe@example.com"
#   },
#   {
#     "id": 2,
#     "name": "Jane Doe",
#     "email": "janedoe@example.com"
#   }
# ]


response = requests.post("http://localhost:8000/users", json={
  "name": "Peter Parker",
  "email": "peterparker@example.com"
})

print(response.json())

# {
#   "id": 3,
#   "name": "Peter Parker",
#   "email": "peterparker@example.com"
# }


response = requests.put("http://localhost:8000/users/3", json={
  "name": "Spider-Man",
  "email": "spiderman@example.com"
})

print(response.json())

# {
#   "id": 3,
#   "name": "Spider-Man",
#   "email": "spiderman@example.com"
# }


response = requests.delete("http://localhost:8000/users/3")

print(response.json())

# {}
