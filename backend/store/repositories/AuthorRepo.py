from store.repositories.base_repo import BaseRepo
from store.models import Author


class AuthorRepo(BaseRepo):
    def __init__(self):
        super().__init__(Author)

    def find_by_last_name(self, last_name):
        return self.model.objects.filter(last_name__icontains=last_name)

    def get_alive_authors(self):
        return self.model.objects.filter(death_date__isnull=True)

    def find_by_country(self, country):
        return self.model.objects.filter(country__iexact=country)