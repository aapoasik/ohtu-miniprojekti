import unittest
from app import app
from config import db
import db_helper
from repositories.todo_repository import create_book

class TestBibtexValidation(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True

        with app.app_context():
            db_helper.setup_db()

        self.client = app.test_client()

    def tearDown(self):
        with app.app_context():
            db_helper.reset_db()

    def test_bibtex_file(self):
        with app.app_context():
            test_book = create_book("test1", "Test title", "Test Author", 1234, "Test Publisher", "123 Test St, Testville, CA 99999")

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

