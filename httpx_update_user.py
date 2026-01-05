import httpx

from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)
print('Status code create user:', create_user_response.status_code)

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)
print('Login user status code:', login_response.status_code)

patch_payload  = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

access_token = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

patch_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", json=patch_payload, headers=access_token)
patch_response_data = patch_response.json()
print('Update data:', patch_response_data)
print('Update user status code:', patch_response.status_code)

