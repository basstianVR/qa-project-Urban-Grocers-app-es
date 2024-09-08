import sender_stand_request
import data

def create_user_and_get_token():
    creation_response = sender_stand_request.post_new_user(data.user_body)
    return creation_response.json()['authToken']


def positive_assert(kit_body, auth_token):
    creation_response = sender_stand_request.post_new_kit_in_new_user(kit_body, auth_token)

    assert creation_response.status_code == 201
    assert creation_response.json()["name"] == kit_body["name"]

def negative_assert(kit_body, auth_token):
    creation_response = sender_stand_request.post_new_kit_in_new_user(kit_body, auth_token)

    assert creation_response.status_code == 401

# Test 1 - 	El número permitido de caracteres (1)
def test_create_user_kit_with_1_character_in_name():
    auth_token = create_user_and_get_token()
    positive_assert(data.kit_body_test_1, auth_token)

# Test 2 - El número permitido de caracteres (511)
def test_create_user_kit_with_511_characters_in_name():
    auth_token = create_user_and_get_token()
    positive_assert(data.kit_body_test_2, auth_token)

# Test 3 - El número de caracteres es menor que la cantidad permitida (0)
def test_create_user_kit_with_0_characters_in_name():
    auth_token = create_user_and_get_token()
    negative_assert(data.kit_body_test_3, auth_token)

# Test 4 - El número de caracteres es mayor que la cantidad permitida (512)
def test_create_user_kit_with_512_characters_in_name():
    auth_token = create_user_and_get_token()
    negative_assert(data.kit_body_test_4, auth_token)

# Test 5 - Se permiten caracteres especiales
def test_create_user_kit_with_special_characters_in_name():
    auth_token = create_user_and_get_token()
    positive_assert(data.kit_body_test_5, auth_token)

# Test 6 - Se permiten espacios
def test_create_user_kit_with_space_characters_in_name():
    auth_token = create_user_and_get_token()
    negative_assert(data.kit_body_test_6, auth_token)

# Test 7 - Se permiten números
def test_create_user_kit_with_numbers_characters_in_name():
    auth_token = create_user_and_get_token()
    positive_assert(data.kit_body_test_7, auth_token)

# Test 8 - El parámetro no se pasa en la solicitud
def test_create_user_kit_without_name():
    auth_token = create_user_and_get_token()
    negative_assert(data.kit_body_test_8, auth_token)

# Test 9 - Se ha pasado un tipo de parámetro diferente (número)
def test_create_user_kit_number_type_in_name():
    auth_token = create_user_and_get_token()
    negative_assert(data.kit_body_test_9, auth_token)







#response_new_kit = positive_assert_in_new_user(data.kit_body, create_user_and_get_token())

#response_new_kit = sender_stand_request.post_new_kit(data.kit_body)
#print(response_new_kit.status_code)
#print(response_new_kit.text)



