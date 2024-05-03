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
