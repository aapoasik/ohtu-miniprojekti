import unittest, db_helper
from repositories.todo_repository import create_book
from app import app, db

class TestBibtexValidation(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        with app.app_context():
            db.create_all()
        test_book = create_book("test1", "Test title", "Test Author", "1234", "Test Publisher", "123 Test St, Testville, CA 99999")


    def tearDown(self):
        self.app_context.pop()

    def test_bibtex_file(self):
        with app.test_client() as client:
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
