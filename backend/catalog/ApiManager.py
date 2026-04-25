from typing import Any, Dict
import requests
from django.conf import settings

SUCCESSFUL_RESPONSES = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]

class ApiManager:       
    def __init__(self, hostname: str = None, api_key: str = '', ver: str = None, ssl_verify: bool = None):

        self.hostname = hostname or settings.API_HOST
        self.ver = ver or settings.API_VERSION
        self._ssl_verify = ssl_verify if ssl_verify is not None else settings.API_SSL_VERIFY
        self._api_key = api_key

        self.url = "http://{}/{}/".format(self.hostname, self.ver)


    def get(self, endpoint: str, data: Dict = None):
        full_url = self.url + endpoint
        headers = {'x-api-key': self._api_key}
        response = requests.get(
            url=full_url, verify=self._ssl_verify, headers=headers,
            params=data)

        return response.json()

    def post(self, endpoint: str, data: Dict, files=None):
        full_url = self.url + endpoint
        headers = {'x-api-key': self._api_key}
        response = requests.post(
            url=full_url, verify=self._ssl_verify, headers=headers,
            data=data, files=files
        )

        return response.json()
    
    def put(self, endpoint: str, data: Dict, files=None):
        full_url = self.url + endpoint
        headers = {'x-api-key': self._api_key}
        response = requests.put(
            url=full_url, verify=self._ssl_verify, headers=headers,
            data=data, files=files
        )

        return response.json()

    def delete(self, endpoint: str):
        full_url = self.url + endpoint
        headers = {'x-api-key': self._api_key}
        response = requests.delete(
            url=full_url, verify=self._ssl_verify, headers=headers
        )

        return response


class BookApiManager:
    def __init__(self, client):
        self.client = client

    def get_all_books(self):
        return self.client.get("books/")

    def get_by_id(self, book_id: int):
        return self.client.get(f"books/{book_id}/")
    
    def create(self, data: Dict[str, Any], image_file=None):
        files = None
        if image_file:
            image_file.seek(0)
            files = {
                "image": (image_file.name, image_file.read(), image_file.content_type)
            }
        return self.client.post("books/", data=data, files=files)

    def delete(self, book_id: int):
        response = self.client.delete(f"books/{book_id}/")
        if response.status_code in SUCCESSFUL_RESPONSES:
            return True

        return False

    def get_books_by_genre(self, genre_id: int):
        return self.client.get("books/", data={"genre": genre_id})

    def get_books_by_publisher(self, publisher_id: int):
        return self.client.get("books/", data={"publisher": publisher_id})
    
    def get_by_id_with_related(self, book_id: int):
        return self.client.get(f"books/{book_id}/details/")
    

class GenreApiManager:
    def __init__(self, client):
        self.client = client

    def get_all_genres(self):
        return self.client.get("genres/")

    def get_by_id(self, genre_id: int):
        return self.client.get(f"genres/{genre_id}/")


class PublisherApiManager:
    def __init__(self, client):
        self.client = client

    def get_all_publishers(self):
        return self.client.get("publishers/")

    def get_by_id(self, publisher_id: int):
        return self.client.get(f"publishers/{publisher_id}/")
    
class StatsApiManager:
    def __init__(self, client):
        self.client = client

    def get_publisher_stats(self):
        return self.client.get("catalog/publishers/stats/")

    def get_genre_stats(self):
        return self.client.get("catalog/genres/stats/")

    def get_book_stats_overall(self):
        return self.client.get("catalog/books/stats/overall/")


api_manager = ApiManager()
book_api = BookApiManager(api_manager)
genre_api = GenreApiManager(api_manager)
publisher_api = PublisherApiManager(api_manager)
stats_api = StatsApiManager(api_manager)