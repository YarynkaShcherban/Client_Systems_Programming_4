from store.repositories.base_repo import BaseRepo
from store.models import Book
from django.db.models import Count, Avg

class BookRepo(BaseRepo):
    def __init__(self):
        super().__init__(Book)

    def find_by_name(self, name):
        return self.model.objects.filter(name__icontains=name)

    def get_books_by_publisher(self, publisher_id):
        return self.model.objects.filter(publisher_id=publisher_id)

    def get_books_cheaper_than(self, price):
        return self.model.objects.filter(price__lt=price)
    
    def get_books_by_genre(self, genre_id):
        return self.model.objects.filter(genres__genre_id=genre_id)
    
    def get_by_id_with_related(self, book_id):
        return (
            self.model.objects
            .select_related("publisher")
            .prefetch_related("author", "genres")
            .filter(book_id=book_id)
            .first()
        )

    def get_all_with_related(self):
        return self.model.objects.select_related("publisher").prefetch_related("author", "genres").annotate(num_authors=Count("author"))