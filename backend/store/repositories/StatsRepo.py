from django.db.models import Avg, Count, Sum, F
from store.models import Book, Author, Publisher, Genre, Store


class StatsRepo:

    @staticmethod
    def genres_with_books_and_avg_price():
        return Genre.objects.annotate(
            num_books=Count('book', distinct=True),
            avg_price=Avg('book__price')
        ).values('name', 'num_books', 'avg_price')

    @staticmethod
    def authors_avg_book_price():
        return Author.objects.annotate(
            avg_price=Avg('books__price')
        ).values('first_name', 'last_name', 'avg_price')

    @staticmethod
    def publishers_avg_price():
        return Publisher.objects.annotate(
            num_books=Count('books', distinct=True),
            avg_price=Avg('books__price')
        ).values('name', 'num_books', 'avg_price')

    @staticmethod
    def top_authors_by_book_count(limit=5):
        return Author.objects.annotate(
            num_books=Count('books', distinct=True)
        ).order_by('-num_books')[:limit].values('first_name', 'last_name', 'num_books')

    @staticmethod
    def expensive_publishers(threshold=10):
        return Publisher.objects.annotate(
            avg_price=Avg('books__price')
        ).filter(avg_price__gt=threshold).values('name', 'avg_price')

    @staticmethod
    def store_sales_stats():
        return Store.objects.annotate(
            total_sales=Sum('purchase__total_amount'),
            total_purchases=Count('purchase', distinct=True)
        ).values('name', 'total_sales', 'total_purchases')

    @staticmethod
    def avg_price_by_genre_and_store():
        return (
            Genre.objects
            .values(
                genre_name=F('name'),
                store_name=F(
                    'book__purchasedetail__purchase__store__name'
                )
            )
            .annotate(
                avg_price=Avg('book__purchasedetail__price_at_purchase')
            )
            .order_by('genre_name', 'store_name')
        )

    @staticmethod
    def book_overall_stats():
        data = Book.objects.aggregate(
            avg_price=Avg('price'),
            total_books=Count('book_id')
        )
        data['avg_price'] = round(data['avg_price'] or 0, 2)
        return data

    @staticmethod
    def genre_stats():
        genres = Genre.objects.annotate(
            avg_price=Avg('book__price'),
            num_books=Count('book')
        ).values('name', 'avg_price', 'num_books')

        for g in genres:
            g['avg_price'] = round(g['avg_price'] or 0, 2)
        return list(genres)

    @staticmethod
    def publisher_stats():
        publishers = Publisher.objects.annotate(
            avg_price=Avg('books__price'),
            num_books=Count('books')
        ).values('name', 'avg_price', 'num_books')

        for p in publishers:
            p['avg_price'] = round(p['avg_price'] or 0, 2)
        return list(publishers)