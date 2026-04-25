import sys
import logging
from io import BytesIO
from unittest.mock import patch, MagicMock
from django.test import SimpleTestCase
from django.conf import settings
from catalog.ApiManager import ApiManager, BookApiManager

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    stream=sys.stdout
)

class TestApiAdvancedMocking(SimpleTestCase):
    def setUp(self):
        self.hostname = "test-api.com"
        self.version = "v1"
        self.api_key = "secret_token_123"
        self.manager = ApiManager(
            hostname=self.hostname, 
            api_key=self.api_key, 
            ver=self.version, 
            ssl_verify=False
        )
        self.book_api = BookApiManager(self.manager)

    @patch('requests.get')
    def test_get_request_construction(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "ok"}
        mock_get.return_value = mock_response
        
        endpoint = "books/"
        params = {"genre": 5}

        result = self.manager.get(endpoint, data=params)
        expected_url = f"http://{self.hostname}/{self.version}/{endpoint}"
        mock_get.assert_called_once_with(
            url=expected_url,
            verify=False,
            headers={'x-api-key': self.api_key},
            params=params
        )
        self.assertEqual(result, {"status": "ok"})
        logger.info("Тест : Конструкція GET-запиту. URL та API-ключ сформовано вірно.")


    @patch('requests.post')
    def test_book_create_with_image(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"book_id": 99, "title": "New Book"}
        mock_post.return_value = mock_response
        file_content = b"fake image data"
        test_image = BytesIO(file_content)
        test_image.name = "cover.jpg"
        test_image.content_type = "image/jpeg"
        book_data = {"title": "Test Book", "price": 500}

        result = self.book_api.create(data=book_data, image_file=test_image)
        self.assertEqual(result["book_id"], 99)
        args, kwargs = mock_post.call_args
        self.assertIn('files', kwargs)
        self.assertEqual(kwargs['files']['image'][0], "cover.jpg")
        self.assertEqual(kwargs['files']['image'][1], file_content)
        logger.info("Тест : Завантаження зображення. Multipart-дані передаються коректно.")


    @patch('requests.delete')
    def test_delete_book_status_logic(self, mock_delete):
        mock_delete.return_value = MagicMock(status_code=204)
        self.assertTrue(self.book_api.delete(book_id=1))

        mock_delete.return_value = MagicMock(status_code=404)
        self.assertFalse(self.book_api.delete(book_id=1))
        logger.info("Тест : Логіка видалення. Коди 204 та 404 обробляються згідно з SUCCESSFUL_RESPONSES.")


    @patch('requests.get')
    def test_api_error_handling_non_json(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("No JSON object could be decoded")
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            self.manager.get("error-endpoint/")
        logger.info("Тест : Обробка помилок. Система стійка до некоректних JSON-відповідей сервера.")


    def test_initialization_from_settings(self):
        with self.settings(API_HOST="prod-server.com", API_VERSION="v2"):
            manager = ApiManager()
            self.assertEqual(manager.hostname, "prod-server.com")
            self.assertEqual(manager.ver, "v2")
            self.assertIn("prod-server.com/v2/", manager.url)
        logger.info("Тест : Конфігурація. ApiManager успішно підтягнув дані з django.conf.settings.")