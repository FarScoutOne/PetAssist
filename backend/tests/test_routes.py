import json


def test_owners(test_client, init_database):
    response = test_client.get('/owners')

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))  # decode the binary data to string
    print(data)  # prints the data to stdout
    print(type(data))  # prints the type of data to stdout
    print(data["owners"])
    assert isinstance(data["owners"], list)
    assert "name" in data["owners"][0]
    assert "id" in data["owners"][0]
    assert "age" in data["owners"][0]
    assert "role" in data["owners"][0]


def test_add_owner(test_client, init_database):
    owner_data = {
        "name": "David",
        "age": 8,
        "role": "child"
    }
    response = test_client.post('/add_owner', data=json.dumps(owner_data), content_type='application/json')
    assert response.status_code == 201


def test_update_owner(test_client, init_database):
    owner_data = {
        "id": 1,
        "name": "Bob",
        "age": 35,
        "role": "parent"
    }
    response = test_client.put(f'/update_owner/{owner_data["id"]}', data=json.dumps(owner_data), content_type='application/json')
    assert response.status_code == 200


def test_delete_owner(test_client, init_database):
    response = test_client.delete('/owner/1')
    assert response.status_code == 200


def test_pets(test_client, init_database):
    response = test_client.get('/pets')

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    print(data)  # prints the data to stdout
    print(type(data))  # prints the type of data to stdout
    print(data["pets"])
    assert isinstance(data["pets"], list)
    assert "name" in data["pets"][0]
    assert "type" in data["pets"][0]


def test_delete_pet(test_client, init_database):
    response = test_client.delete('/pet/Spot')
    assert response.status_code == 200


def test_foods(test_client, init_database):
    response = test_client.get('/foods')

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    print(data)
    print(type(data))
    print(data["foods"])
    assert isinstance(data["foods"], list)
    assert "id" in data["foods"][0]
    assert "brand" in data["foods"][0]
    assert "flavor" in data["foods"][0]


def test_add_food(test_client, init_database):
    food_data = {
        "brand": "Purina",
        "flavor": "Chicken"
    }
    response = test_client.post('/add_food', data=json.dumps(food_data), content_type='application/json')
    assert response.status_code == 201


def test_delete_food(test_client, init_database):
    response = test_client.delete('/foods/1')
    assert response.status_code == 200


def test_


def test_add_food_to_pet(test_client, init_database):
    pet_food_data = {
        "pet_name": "Whiskers",
        "food_id": 3
    }

    response = test_client.post('/add_food_to_pet', data=json.dumps(pet_food_data), content_type='application/json')
    assert response.status_code == 201
