from rest_framework import serializers
from .models import (
    Store, Position, Employee, Client, Publisher,
    Book, Genre, Author, AuthorBook, GenreBook,
    Purchase, PurchaseDetail,
)


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'first_name', 'last_name', 'email', 'phone', 'password']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False,
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False,
    )

    # Read-only computed fields
    genre_list = serializers.SerializerMethodField(read_only=True)
    author_list = serializers.SerializerMethodField(read_only=True)
    publisher_name = serializers.SerializerMethodField(read_only=True)

    # Extra fields used by the SPA frontend
    author_names = serializers.SerializerMethodField(read_only=True)
    genre_names = serializers.SerializerMethodField(read_only=True)
    genre_ids = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'book_id',
            'name',
            'isbn',
            'price',
            'publisher',
            'publisher_name',
            'authors',
            'genres',
            'genre_list',
            'author_list',
            'author_names',
            'genre_names',
            'genre_ids',
            'image',
        ]

    def get_genre_list(self, obj):
        genre_books = GenreBook.objects.filter(book=obj).select_related('genre')
        return [
            {"id": gb.genre.genre_id, "name": gb.genre.name}
            for gb in genre_books if gb.genre
        ]

    def get_author_list(self, obj):
        author_books = AuthorBook.objects.filter(book=obj).select_related('author')
        return [
            {
                "id": ab.author.author_id,
                "first_name": ab.author.first_name,
                "last_name": ab.author.last_name,
            }
            for ab in author_books if ab.author
        ]

    def get_publisher_name(self, obj):
        return obj.publisher.name if obj.publisher else None

    def get_author_names(self, obj):
        author_books = AuthorBook.objects.filter(book=obj).select_related('author')
        names = [
            f"{ab.author.first_name} {ab.author.last_name}"
            for ab in author_books if ab.author
        ]
        return ', '.join(names) if names else None

    def get_genre_names(self, obj):
        genre_books = GenreBook.objects.filter(book=obj).select_related('genre')
        names = [gb.genre.name for gb in genre_books if gb.genre]
        return ', '.join(names) if names else None

    def get_genre_ids(self, obj):
        genre_books = GenreBook.objects.filter(book=obj).select_related('genre')
        return [gb.genre.genre_id for gb in genre_books if gb.genre]

    def create(self, validated_data):
        author_ids = validated_data.pop('authors', [])
        genre_ids = validated_data.pop('genres', [])
        book = Book.objects.create(**validated_data)
        self._set_m2m_relationships(book, author_ids, genre_ids)
        return book

    def update(self, instance, validated_data):
        author_ids = validated_data.pop('authors', None)
        genre_ids = validated_data.pop('genres', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        self._set_m2m_relationships(instance, author_ids, genre_ids, is_update=True)
        return instance

    def _set_m2m_relationships(self, book, author_ids, genre_ids, is_update=False):
        if author_ids is not None or not is_update:
            if is_update:
                AuthorBook.objects.filter(book=book).delete()
            AuthorBook.objects.bulk_create([
                AuthorBook(author_id=a_id, book=book) for a_id in (author_ids or [])
            ])

        if genre_ids is not None or not is_update:
            if is_update:
                GenreBook.objects.filter(book=book).delete()
            GenreBook.objects.bulk_create([
                GenreBook(genre_id=g_id, book=book) for g_id in (genre_ids or [])
            ])


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBook
        fields = '__all__'


class GenreBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreBook
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetail
        fields = '__all__'