import requests

URL = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    r = requests.get(URL)
    print(r.status_code)
    print(r.text)
    print(type(r.text))

    categories = r.json()
    print('New type', type(categories))
    for category in categories:
        print(category['name'])