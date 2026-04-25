from store.repositories.base_repo import BaseRepo
from store.models import Genre
from django.db.models import Count, Avg

class GenreRepo(BaseRepo):
    def __init__(self):
        super().__init__(Genre)

    def find_by_name(self, name):
        return self.model.objects.filter(name__icontains=name)

    def get_genres_for_book(self, book):
        return self.model.objects.filter(book=book)
    
    def get_stats(self):
        raw = (self.model.objects.annotate(
            avg_price=Avg('book__price'),
            num_books=Count('book')
        ).values('name', 'avg_price', 'num_books'))

        result = []
        for g in raw:
            g["avg_price"] = round(g["avg_price"], 2) if g["avg_price"] is not None else None
            result.append(g)
        return result