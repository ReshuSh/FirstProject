import pytest


class Database:
    def connect(self):
        print("Connecting to the database...")
        return "connection object"

def close(self):
    print("Closing the database connection...")


@pytest.fixture(scope="class")
def db_connection(request):
    db = Database()
    connection = db.connect()

    def teardown():


     request.addfinalizer(teardown)
    return connection


class TestDatabase:
    def test_query1(self, db_connection):
        assert db_connection == "connection object"
        print("Running test_query1")

    def test_query2(self, db_connection):
        assert db_connection == "connection object"
        print("Running test_query2")
