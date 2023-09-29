# Este archivo contiene los llamados a la API JSON Placeholder
import requests


def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response