import  httpx

from httpx_authentication import login_response

login_payload = {
    "email": "test@mail.com",
    "password": "testtest"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

access_token = {
    'Authorization': f'Bearer {login_response_data['token']['accessToken']}'
}

user_information_response = httpx.get('http://localhost:8000/api/v1/users/me', headers= access_token)
user_information_response_data = user_information_response.json()

print("User information response:", user_information_response_data)
print("Status Code:", user_information_response.status_code)