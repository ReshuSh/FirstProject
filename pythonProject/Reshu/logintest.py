import pytest


@pytest.mark.login
def test_login_success():
    assert login('user', 'password') == 'success'


@pytest.mark.login
def test_login_failure():
    assert login('user', 'wrong_password') == 'failure'


@pytest.mark.logout
def test_logout():
    assert logout('user') == 'success'
