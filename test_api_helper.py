import pytest
import responses
import json
from api_helper import get_posts, create_post, update_post, delete_post


@responses.activate
def test_get_posts():
    mock_reponse = [
        {'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'},
        {'id': 2, 'title': 'qui est esse'}
    ]
    responses.add(
        responses.GET,
        'https://jsonplaceholder.typicode.com/posts',
        json=mock_reponse,
        status=200
    )
    response_get = get_posts()

    assert response_get.status_code == 200
    assert response_get.json == mock_reponse