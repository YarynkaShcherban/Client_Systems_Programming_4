from store.repositories import *

# єдина точка доступу
class UnitOfWork:
    def __init__(self):
        self.authors = AuthorRepo()
        self.books = BookRepo()
        self.clients = ClientRepo()
        self.publishers = PublisherRepo()
        self.employees = EmployeeRepo()
        self.positions = PositionRepo()
        self.purchases = PurchaseRepo()
        self.purchase_details = PurchaseDetailRepo()
        self.genres = GenreRepo()
        self.stores = StoreRepo()

    def clear_all(self):
        self.purchase_details.model.objects.all().delete()
        self.purchases.model.objects.all().delete()
        self.books.model.objects.all().delete()
        self.authors.model.objects.all().delete()
        self.clients.model.objects.all().delete()
        self.employees.model.objects.all().delete()
        self.genres.model.objects.all().delete()
        self.positions.model.objects.all().delete()
        self.publishers.model.objects.all().delete()
        self.stores.model.objects.all().delete()