import configuration
import requests
import data


#Crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_kit_in_new_user(kit_info, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_info,
                         headers=headers)

def post_new_kit(kit_info):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_info,
                         headers=data.headers)


#responses = post_new_user(data.user_body)
#print(responses.text)
#print(responses.status_code)
#print(responses.json()['authToken'])

