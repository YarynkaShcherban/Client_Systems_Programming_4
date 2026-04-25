from store.repositories.base_repo import BaseRepo
from store.models import Client


class ClientRepo(BaseRepo):
    def __init__(self):
        super().__init__(Client)

    def find_by_email(self, email):
        return self.model.objects.filter(email__iexact=email).first()

    def find_by_phone(self, phone):
        return self.model.objects.filter(phone__iexact=phone).first()