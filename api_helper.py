# Este archivo contiene los llamados a la API JSON Placeholder
import requests
import json


def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response

def create_post(title, body, userId):
    payload = {
        'title': title,
        'body': body,
        'userId': userId
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
    return response

def update_post(post_id, title, body, userId):
    payload = {
        'title': title,
        'body': body,
        'userId': userId
    }
    response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=payload)
    return response

def delete_post(post_id):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    return response


