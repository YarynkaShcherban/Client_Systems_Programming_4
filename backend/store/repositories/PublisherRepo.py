from store.repositories.base_repo import BaseRepo
from store.models import Publisher
from django.db.models import Count, Avg

class PublisherRepo(BaseRepo):
    def __init__(self):
        super().__init__(Publisher)

    def find_by_email(self, email):
        return self.model.objects.filter(email__iexact=email)
    
    def get_stats(self):
        raw = (self.model.objects.annotate(
            avg_price=Avg('book__price'),
            num_books=Count('book')
        ).values('name', 'avg_price', 'num_books'))

        result = []
        for p in raw:
            p["avg_price"] = round(p["avg_price"], 2) if p["avg_price"] is not None else None
            result.append(p)
        return result