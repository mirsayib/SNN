import requests, json


def get_data(id = None):
    URL = f"http://localhost:8000/api/posts/{id}/"

    json_data = json.dumps(data)
    r = requests.get(url = URL)

    print(r.json())


# get_data(1)

def post_data():
    data = {
        'title': 'Lorem',
        'content': 'Ipsum69',
        'date_posted': "2022-01-15T09:12:07Z"
    }
    json_data = json.dumps(data)

    URL = f"http://localhost:8000/api/create/post/"

    r = requests.post(url = URL, data=json_data)
    print(r.json())

def update_data():
    data = {
        'id': 1,
        'title': 'Lorem',
        'content': 'Ipsum',
        'date_posted': "2022-01-29T09:12:07Z"
    }

    URL = f"http://localhost:8000/api/update/post/"

    json_data = json.dumps(data)
    r = requests.put(url = URL, data=json_data)
    data = r.json()
    print(data)

def delete_data():
    data = {'id': 12}
    URL = f"http://localhost:8000/api/delete/post/"

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data=json_data)
    data = r.json()
    print(data)

post_data()


