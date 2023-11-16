import requests
import env

header_data = env.data

data = {'grant_type': 'password', 'username': header_data['user_name'], 'password': header_data['user_pass']}
auth = requests.auth.HTTPBasicAuth(header_data['app_id'], header_data['secret'])

auth_request = requests.post(header_data['base_url'] + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'facul-IDS-001 by Local-Translator1863'},
		  auth=auth)
auth_response = auth_request.json()

print(auth_response)

token = f'{auth_response["token_type"]}  {auth_response["access_token"]}'
print(f'\n TOKEN = {token}')
print("---- ----- ----- \n")

user_agent = header_data["api_project_nme"] + 'by'  +  header_data["user_name"]
headers = {'Authorization': token, 'User-Agent': user_agent }
response = requests.get(header_data['base_url_auth'] + '/api/v1/me', headers=headers)

print(response.status_code)
print(response.json())

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])