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
    response = test_client.put(f'/update_owner/{owner_data["id"]}', data=json.dumps(owner_data),
                               content_type='application/json')
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


def test_add_food_to_pet(test_client, init_database):
    pet_food_data = {
        "pet_name": "Whiskers",
        "food_id": 3
    }

    response = test_client.post('/add_food_to_pet', data=json.dumps(pet_food_data), content_type='application/json')
    assert response.status_code == 201


def test_get_foods_for_pet(test_client, init_database):
    response = test_client.get('/foods/Whiskers')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    print(data)
    print(type(data))
    print(data["foods"])
    assert isinstance(data["foods"], list)
    assert "brand" in data["foods"][0]
    assert "flavor" in data["foods"][0]


def test_remove_food_from_pet(test_client, init_database):
    food_to_remove = {"pet_name": "Whiskers", "food_id": 3}

    response = test_client.delete('/remove_food_from_pet', data=json.dumps(food_to_remove),
                                  content_type='application/json')
    assert response.status_code == 200


def test_get_all_activities(test_client, init_database):
    response = test_client.get('/activities')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    print(data)
    print(type(data))
    print(data["activities"])
    assert isinstance(data["activities"], list)
    assert "name" in data["activities"][0]
    assert "description" in data["activities"][0]


def test_add_activity(test_client, init_database):
    activity_data = {
        "activityName": "Brushing",
        "activityDescription": "Brush them gently from head to tail and get all of the loose hair off. Make sure to "
                               "give a treat at the end."
    }
    response = test_client.post('/add_activity', data=json.dumps(activity_data), content_type='application/json')
    assert response.status_code == 201


def test_get_activity(test_client, init_database):
    response = test_client.get('/activities/1')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    print(data)
    print(type(data))
    assert isinstance(data, dict)
    assert "name" in data
    assert "description" in data


def test_update_activity(test_client, init_database):
    activity_data = {
        "activityName": "play",
        "activityDescription": "Play indoors and get him to run around and catch. Give him a tree to reinforce good "
                               "behavior."
    }
    response = test_client.put('/update_activity/1', data=json.dumps(activity_data),
                               content_type='application/json')
    assert response.status_code == 200


def test_delete_activity(test_client, init_database):
    response = test_client.delete('/activities/1')
    assert response.status_code == 200


def test_get_scheduled_activities(test_client, init_database):
    response = test_client.get('/scheduled_activities')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    scheduled_activities = data["scheduled_activities"]
    print(scheduled_activities)
    print(type(scheduled_activities))
    assert isinstance(scheduled_activities, list)
    assert "activity_id" in scheduled_activities[0]
    assert "pet_name" in scheduled_activities[0]
    assert "deadline" in scheduled_activities[0]


def test_add_scheduled_activity(test_client, init_database):
    scheduled_activity_data = {
        "activity_id": 1,
        "pet_name": "Whiskers",
        "deadline": "2024-05-15"
    }

    response = test_client.post('/add_scheduled_activity', data=json.dumps(scheduled_activity_data),
                                content_type='application/json')
    assert response.status_code == 201


def test_update_scheduled_activity(test_client, init_database):
    scheduled_activity_data = {
        "activity_id": 2,
        "pet_name": "Whiskers",
        "deadline": "2024-05-15"
    }

    response = test_client.put('/update_scheduled_activity/1', data=json.dumps(scheduled_activity_data),
                               content_type='application/json')
    assert response.status_code == 200


def test_delete_scheduled_activity(test_client, init_database):
    response = test_client.delete('/update_scheduled_activity/1')
    assert response.status_code == 200


def test_get_scheduled_activities_today(test_client, init_database):
    response = test_client.get('/scheduled_activities_today')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    scheduled_activities = data["scheduled_activities"]
    print(scheduled_activities)
    print(type(scheduled_activities))
    assert isinstance(scheduled_activities, list)
    assert "activity_name" in scheduled_activities[0]
    assert "pet_name" in scheduled_activities[0]
    assert "deadline" in scheduled_activities[0]
