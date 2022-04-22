import requests, json


def post_data():
    data = {
        'title': 'Lorem',
        'content': 'Ipsum',
        'date_posted': "2022-01-15T09:12:07Z"
    }
    json_data = json.dumps(data)

    URL = f"http://localhost:8000/api/posts.json/"

    r = requests.post(url = URL, data=json_data)
    print(r.json())

def update_data():
    data = {
        'title': 'LoremKakauIpsum',
        'content': 'IpsumKakauLorem',
        'date_posted': "2022-01-29T09:12:07Z"
    }

    URL = f"http://localhost:8000/api/posts/1/"

    json_data = json.dumps(data)
    r = requests.put(url = URL, data=json_data)
    data = r.json()
    print(data)

def delete_data():
    URL = f"http://localhost:8000/api/posts/1/"
    r = requests.delete(url = URL)
    data = r.json()
    print(data)

post_data()


