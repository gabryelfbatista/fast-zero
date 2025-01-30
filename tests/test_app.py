from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_page_deve_retornar_pagina(client):
    response = client.get('/html')

    assert (
        response.text
        == """
    <html>
        <body>
            <h1> Pagina de retorno </h1>
        </body>
    </html>
    """
    )


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'id': 1,
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'id': 1,
                'email': 'test@test.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '',
            'username': 'testusername2',
            'id': 1,
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername2',
        'id': 1,
        'email': 'test@test.com',
    }

    # Teste 404 not found

    response = client.put(
        '/users/2',
        json={
            'password': '',
            'username': 'testusername2',
            'id': 1,
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}

    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
