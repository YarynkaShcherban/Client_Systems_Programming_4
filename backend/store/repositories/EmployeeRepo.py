from store.repositories.base_repo import BaseRepo
from store.models import Employee


class EmployeeRepo(BaseRepo):
    def __init__(self):
        super().__init__(Employee)

    def find_by_last_name(self, last_name):
        return self.model.objects.filter(last_name__icontains=last_name)

    def get_by_position(self, role):
        return self.model.objects.filter(position__role__icontains=role)

    def get_by_store(self, store_id):
        return self.model.objects.filter(store_id=store_id)