from http import HTTPStatus

from fastapi.testclient import TestClient  # type: ignore

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_page_deve_retornar_pagina():
    client = TestClient(app)

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
