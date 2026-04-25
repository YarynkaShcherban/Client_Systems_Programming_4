from store.repositories.base_repo import BaseRepo
from store.models import Purchase


class PurchaseRepo(BaseRepo):
    def __init__(self):
        super().__init__(Purchase)

    def get_by_client(self, client_id):
        return self.model.objects.filter(client_id=client_id)

    def get_by_employee(self, employee_id):
        return self.model.objects.filter(employee_id=employee_id)

    def get_by_store(self, store_id):
        return self.model.objects.filter(store_id=store_id)

    def get_by_date_range(self, start_date, end_date):
        return self.model.objects.filter(purchase_date__range=[start_date, end_date])