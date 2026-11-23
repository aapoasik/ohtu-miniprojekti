import unittest
from app import app
from config import db
from repositories.todo_repository import create_book

class TestBibtexValidation(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True

        with app.app_context():
            db.create_all()

        self.client = app.test_client()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_bibtex_file(self):
            response = self.client.get("/download")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.mimetype, "application/x-bibtex")

            self.assertEqual(response.data.decode("utf-8"), """@book{test1,
    author = {Test Author},
    title = {Test title},
    publisher = {Test Publisher},
    year = {1234},
    address = {123 Test St, Testville, CA 99999}
}

""")