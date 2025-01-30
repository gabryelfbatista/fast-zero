from fast_zero.models import User


def test_create_user():
    user = User(
        username='Gabryel', email='ga@email.com', password='minhasenha'
    )

    assert user.username == 'Gabryel'
