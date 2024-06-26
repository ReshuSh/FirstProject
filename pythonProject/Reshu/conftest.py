# conftest.py
import pytest

@pytest.fixture
def db_connection():
    print("Setting up database connection...")
    conn = "database_connection"
    yield conn
    print("Tearing down database connection...")
    conn = None

@pytest.fixture
def another_fixture():
    print("Setting up another fixture...")
    resource = "another_resource"
    yield resource
    print("Tearing down another fixture...")
    resource = None
