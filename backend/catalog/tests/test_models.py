import logging
import sys
from decimal import Decimal
from django.test import TestCase
from store.models import (
    Store, Position, Employee,
    Publisher, Book, Client,
    Purchase, PurchaseDetail
)

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    stream=sys.stdout
)

class TestDatabaseQueries(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.store = Store.objects.create(
            name="Central Store",
            city="Kyiv",
            address="Main street 1",
            phone="+380001112233",
            email="store@test.com"
        )

        cls.position = Position.objects.create(
            role="Seller",
            salary=Decimal("15000.00")
        )

        cls.employee = Employee.objects.create(
            first_name="Ivan",
            last_name="Petrenko",
            phone="+380009998877",
            email="ivan@test.com",
            position=cls.position,
            store=cls.store
        )

        cls.publisher = Publisher.objects.create(
            name="Test Publisher",
            phone="+380777888999",
            email="pub@test.com"
        )

        cls.book = Book.objects.create(
            name="Django for Professionals",
            price=Decimal("500.00"),
            publisher=cls.publisher
        )

        cls.client = Client.objects.create(
            first_name="Anna",
            last_name="Ivanova",
            phone="+380666555444",
            email="anna@test.com"
        )

        cls.purchase = Purchase.objects.create(
            client=cls.client,
            employee=cls.employee,
            store=cls.store,
            total_amount=Decimal("1000.00")
        )

        PurchaseDetail.objects.create(
            purchase=cls.purchase,
            book=cls.book,
            quantity=2,
            price_at_purchase=Decimal("500.00")
        )


    def test_store_creation(self):
        self.assertEqual(Store.objects.count(), 1)
        self.assertEqual(self.store.city, "Kyiv")
        logger.info("Тест : Store створено коректно.")


    def test_employee_relationships(self):
        self.assertEqual(self.employee.store.name, "Central Store")
        self.assertEqual(self.employee.position.role, "Seller")
        logger.info("Тест : Employee FK працює.")


    def test_purchase_total_amount(self):
        purchase = Purchase.objects.first()
        self.assertEqual(purchase.total_amount, Decimal("1000.00"))
        logger.info("Тест : загальна сума покупки правильна.")


    def test_purchase_detail_quantity(self):
        detail = PurchaseDetail.objects.first()
        self.assertEqual(detail.quantity, 2)
        self.assertEqual(detail.book.name, "Django for Professionals")
        logger.info("Тест : Перевірено цілісність деталей покупки.")


    def test_book_publisher_relation(self):
        self.assertEqual(self.book.publisher.name, "Test Publisher")
        logger.info("Тест : зв'язок книги з видавцем працює. ")