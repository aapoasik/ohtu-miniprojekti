import unittest
from repositories.todo_repository import create_book
from src.app import app, db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.app_context():
        db.create_all()

        with app.test_client() as client:
            yield client
            
        db.session.remove()
        db.drop_all()

class TestBibtexValidation(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        test_book = create_book("test1", "Test title", "Test Author", "1234", "Test Publisher", "123 Test St, Testville, CA 99999")

    def tearDown(self):
        self.app_context.pop()

    def test_bibtex_file(client):
            response = client.get("/download")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.mimetype, "application/x-bibtex")
            
            assert response.data.decode("utf-8") == """@book{test1,
    author = {Test Author},
    title = {Test title},
    publisher = {Test Publisher},
    year = {1234},
    address = {123 Test St, Testville, CA 99999}
}

"""
