from store.repositories.base_repo import BaseRepo
from store.models import Store


class StoreRepo(BaseRepo):
    def __init__(self):
        super().__init__(Store)

    def get_by_city(self, city):
        return self.model.objects.filter(city__icontains=city)

    def find_by_email(self, email):
        return self.model.objects.filter(email__iexact=email)