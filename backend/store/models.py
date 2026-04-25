from django.db import models


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField()

    class Meta:
        db_table = 'store'

    def __str__(self):
        return self.name


class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'position'

    def __str__(self):
        return self.role


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    hire_date = models.DateField(auto_now_add=True)
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, db_column='position_id')
    store = models.ForeignKey(
        Store, on_delete=models.SET_NULL, null=True, db_column='store_id')

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255, default='password')

    class Meta:
        db_table = 'client'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, unique=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'publisher'

    def __str__(self):
        return self.name

    
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.TextField()
    isbn = models.TextField(unique=True, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.SET_NULL, null=True, db_column='publisher_id', related_name='books')
    author = models.ManyToManyField(
        'Author', through='AuthorBook', related_name='books')
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)

    class Meta:
        db_table = 'book'

    def str(self):
        return self.name

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    book = models.ManyToManyField(
        Book, through='GenreBook', related_name='genres')

    class Meta:
        db_table = 'genre'

    def str(self):
        return self.name


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pseudonym = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'author'

    def str(self):
        return f"{self.first_name} {self.last_name}"
    

class AuthorBook(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, db_column='author_id', primary_key=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, db_column='book_id')

    class Meta:
        db_table = 'author_book'
        unique_together = ('author', 'book')
        managed = False


class GenreBook(models.Model):
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, db_column='genre_id', primary_key=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, db_column='book_id')

    class Meta:
        db_table = 'genre_book'
        unique_together = ('genre', 'book')
        managed = False


class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True, db_column='purchase_id')
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True, db_column='client_id')
    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, db_column='employee_id')
    store = models.ForeignKey(
        Store, on_delete=models.SET_NULL, null=True, db_column='store_id')
    purchase_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'purchase'


class PurchaseDetail(models.Model):
    purchase = models.ForeignKey(
        Purchase, on_delete=models.CASCADE, db_column='purchase_id', primary_key=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, db_column='book_id')
    quantity = models.IntegerField()
    price_at_purchase = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'purchase_detail'
        unique_together = ('purchase', 'book')
