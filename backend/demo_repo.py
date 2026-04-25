import os
import django
from datetime import date
from decimal import Decimal
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore_project.settings")
django.setup()

def main():
    from store.repositories.unit_of_work import UnitOfWork
    from store.models import Store, Employee, Position, Author, Publisher, Book, Client, Purchase, PurchaseDetail, Genre

    repo = UnitOfWork()

    print("Очистка бази даних...")
    repo.clear_all()
    print(" Усі таблиці очищено!\n")

    store1 = repo.stores.create(
        name="The Book Loft",
        city="Columbus",
        address="631 South Third St.",
        phone="1234567891",
        email="info@bookloft.com")
    
    store2 = repo.stores.create(
        name="Powell's Books",
        city="Portland",
        address="1005 W Burnside St.",
        phone="1234567892",
        email="info@powells.com")

    store3 = repo.stores.create(
        name="Strand Bookstore",
        city="New York",
        address="828 Broadway",
        phone="1234567893",
        email="info@strand.com")

    store4 = repo.stores.create(
        name="City Lights Booksellers",
        city="San Francisco",
        address="261 Columbus Ave",
        phone="1234567894",
        email="info@citylights.com")

    store5 = repo.stores.create(
        name="Shakespeare and Company",
        city="Paris",
        address="37 Rue de la Bûcherie",
        phone="1234567895",
        email="info@shakespeareandcompany.com")

    position1 = repo.positions.create(
        role="Store Manager",
        salary=Decimal("2500.00"))

    position2 = repo.positions.create(
        role="Sales Assistant",
        salary=Decimal("1200.00"))

    position3 = repo.positions.create(
        role="Inventory Specialist",
        salary=Decimal("1800.00"))

    position4 = repo.positions.create(
        role="Customer Support",
        salary=Decimal("1500.00"))

    employee1 = repo.employees.create(
        first_name="John",
        last_name="Doe",
        birth_date=date(1985, 4, 12),
        phone="+1-614-555-1234",
        email="john.doe@example.com",
        position=position1,
        store=store1
    )

    employee2 = repo.employees.create(
        first_name="Emily",
        last_name="Smith",
        birth_date=date(1990, 7, 22),
        phone="+1-212-555-5678",
        email="emily.smith@example.com",
        position=position2,
        store=store1
    )

    employee3 = repo.employees.create(
        first_name="Michael",
        last_name="Johnson",
        birth_date=date(1988, 2, 5),
        phone="+44-20-555-7890",
        email="michael.johnson@example.co.uk",
        position=position3,
        store=store1
    )

    employee4 = repo.employees.create(
        first_name="Sophie",
        last_name="Brown",
        birth_date=date(1995, 11, 30),
        phone="+1-503-555-3456",
        email="sophie.brown@example.com",
        position=position4,
        store=store1
    )

    employee5 = repo.employees.create(
        first_name="Liam",
        last_name="O'Connell",
        birth_date=date(1992, 1, 15),
        phone="+1-503-555-4321",
        email="liam.o.c@example.com",
        position=position1, 
        store=store2
    )

    employee6 = repo.employees.create(
        first_name="Olivia",
        last_name="Taylor",
        birth_date=date(1998, 5, 20),
        phone="+1-503-555-8765",
        email="olivia.t@example.com",
        position=position2,
        store=store2
    )
    employee7 = repo.employees.create(
        first_name="Michael",
        last_name="Brann",
        birth_date=date(1978, 2, 5),
        phone="+44-60-555-7890",
        email="michael.brann@example.co.uk",
        position=position3,
        store=store2
    )

    employee8 = repo.employees.create(
        first_name="Anna",
        last_name="Brown",
        birth_date=date(1998, 10, 30),
        phone="+1-589-555-3456",
        email="anna.brown@example.com",
        position=position4,
        store=store2
    )

    employee9 = repo.employees.create(
        first_name="Isac",
        last_name="O'Connell",
        birth_date=date(1991, 1, 15),
        phone="+1-503-559-4321",
        email="isac.o.c@example.com",
        position=position1, 
        store=store3
    )

    employee10 = repo.employees.create(
        first_name="Mary",
        last_name="Taylor",
        birth_date=date(1988, 5, 20),
        phone="+1-593-555-8765",
        email="mary.t@example.com",
        position=position2,
        store=store3
    )
    employee11 = repo.employees.create(
        first_name="Michael",
        last_name="Brann",
        birth_date=date(1968, 2, 5),
        phone="+44-60-555-7790",
        email="michael.brann@example.co.uk",
        position=position3,
        store=store3
    )

    employee12 = repo.employees.create(
        first_name="Anna",
        last_name="Goth",
        birth_date=date(1988, 10, 30),
        phone="+1-589-556-3456",
        email="anna.goth@example.com",
        position=position4,
        store=store3
    )

    employee13 = repo.employees.create(
        first_name="Liam",
        last_name="Bond",
        birth_date=date(1998, 1, 15),
        phone="+1-533-555-4321",
        email="liam.o.c@example.com",
        position=position1, 
        store=store4
    )

    employee14 = repo.employees.create(
        first_name="Olivia",
        last_name="Taylor",
        birth_date=date(1988, 5, 20),
        phone="+1-503-575-8765",
        email="olivia.t@example.com",
        position=position2,
        store=store4
    )
    employee15 = repo.employees.create(
        first_name="Joe",
        last_name="Brann",
        birth_date=date(1978, 2, 5),
        phone="+44-60-555-7867",
        email="joe.brann@example.co.uk",
        position=position3,
        store=store4
    )

    employee16 = repo.employees.create(
        first_name="Anna",
        last_name="Stone",
        birth_date=date(1998, 10, 30),
        phone="+1-529-555-3456",
        email="anna.stone@example.com",
        position=position4,
        store=store4
    )

    employee17 = repo.employees.create(
        first_name="Liam",
        last_name="O'Connell",
        birth_date=date(1992, 1, 15),
        phone="+1-503-555-4721",
        email="liam.o.c@example.com",
        position=position1, 
        store=store5
    )

    employee18 = repo.employees.create(
        first_name="Olivia",
        last_name="Taylor",
        birth_date=date(1998, 5, 20),
        phone="+1-563-555-8765",
        email="olivia.t@example.com",
        position=position2,
        store=store5
    )
    employee19 = repo.employees.create(
        first_name="Michael",
        last_name="Brann",
        birth_date=date(1978, 2, 5),
        phone="+44-60-555-7490",
        email="michael.brann@example.co.uk",
        position=position3,
        store=store5
    )

    employee20 = repo.employees.create(
        first_name="Anna",
        last_name="Brown",
        birth_date=date(1998, 10, 30),
        phone="+1-529-555-3356",
        email="anna.brown@example.com",
        position=position4,
        store=store5
    )

    author1 = repo.authors.create(
        first_name="Agatha", last_name="Christie", pseudonym=None,
        birth_date=date(1890, 9, 15), death_date=date(1976, 1, 12), country="UK"
    )

    author2 = repo.authors.create(
        first_name="Haruki", last_name="Murakami", pseudonym=None,
        birth_date=date(1949, 1, 12), death_date=None, country="Japan"
    )

    author3 = repo.authors.create(
        first_name="George", last_name="Orwell", pseudonym=None,
        birth_date=date(1903, 6, 25), death_date=date(1950, 1, 21), country="UK"
    )

    author4 = repo.authors.create(
        first_name="Ernest", last_name="Hemingway", pseudonym=None,
        birth_date=date(1899, 7, 21), death_date=date(1976, 7, 2), country="USA"
    )

    author5 = repo.authors.create(
        first_name="J.K.", last_name="Rowling", pseudonym=None,
        birth_date=date(1965, 7, 31), death_date=None, country="UK"
    )

    author6 = repo.authors.create(
        first_name="Leo", last_name="Tolstoy", pseudonym=None,
        birth_date=date(1828, 9, 9), death_date=date(1910, 11, 20), country="Russia"
    )

    author7 = repo.authors.create(
        first_name="Jane", last_name="Austen", pseudonym=None,
        birth_date=date(1775, 12, 16), death_date=date(1817, 7, 18), country="UK"
    )

    author8 = repo.authors.create(
        first_name="Mark", last_name="Twain", pseudonym=None,
        birth_date=date(1835, 11, 30), death_date=date(1910, 4, 21), country="USA"
    )

    author9 = repo.authors.create(
        first_name="F. Scott", last_name="Fitzgerald", pseudonym=None,
        birth_date=date(1896, 9, 24), death_date=date(1940, 12, 21), country="USA"
    )

    author10 = repo.authors.create(
        first_name="Toni", last_name="Morrison", pseudonym=None,
        birth_date=date(1931, 2, 18), death_date=date(2019, 8, 5), country="USA"
    )

    author11 = repo.authors.create(
        first_name="Gabriel", last_name="García Márquez", pseudonym=None,
        birth_date=date(1927, 3, 6), death_date=date(2014, 4, 17), country="Colombia"
    )

    author12 = repo.authors.create(
        first_name="Margaret", last_name="Atwood", pseudonym=None,
        birth_date=date(1939, 11, 18), death_date=None, country="Canada"
    )

    author13 = repo.authors.create(
        first_name="Virginia", last_name="Woolf", pseudonym=None,
        birth_date=date(1882, 1, 25), death_date=date(1941, 3, 28), country="UK"
    )

    author14 = repo.authors.create(
        first_name="Chinua", last_name="Achebe", pseudonym=None,
        birth_date=date(1930, 11, 16), death_date=date(2013, 3, 21), country="Nigeria"
    )

    author15 = repo.authors.create(
        first_name="Herman", last_name="Melville", pseudonym=None,
        birth_date=date(1819, 8, 1), death_date=date(1891, 9, 28), country="USA"
    )

    author16 = repo.authors.create(
        first_name="Zadie", last_name="Smith", pseudonym=None,
        birth_date=date(1975, 10, 25), death_date=None, country="UK"
    )

    author17 = repo.authors.create(
        first_name="Albert", last_name="Camus", pseudonym=None,
        birth_date=date(1913, 11, 7), death_date=date(1960, 1, 4), country="France"
    )

    author18 = repo.authors.create(
        first_name="Isabel", last_name="Allende", pseudonym=None,
        birth_date=date(1942, 8, 2), death_date=None, country="Chile"
    )

    author19 = repo.authors.create(
        first_name="Kurt", last_name="Vonnegut", pseudonym=None,
        birth_date=date(1922, 11, 11), death_date=date(2007, 4, 11), country="USA"
    )

    author20 = repo.authors.create(
        first_name="J.R.R.", last_name="Tolkien", pseudonym=None,
        birth_date=date(1892, 1, 3), death_date=date(1973, 9, 2), country="UK"
    )

    author21 = repo.authors.create(
        first_name="Khaled", last_name="Hosseini", pseudonym=None,
        birth_date=date(1965, 3, 4), death_date=None, country="Afghanistan"
    )

    author22 = repo.authors.create(
        first_name="Octavia E.", last_name="Butler", pseudonym=None,
        birth_date=date(1947, 6, 22), death_date=date(2006, 2, 24), country="USA"
    )

    author23 = repo.authors.create(
        first_name="Kazuo", last_name="Ishiguro", pseudonym=None,
        birth_date=date(1954, 11, 8), death_date=None, country="UK"
    )

    author24 = repo.authors.create(
        first_name="Mario Vargas", last_name="Llosa", pseudonym=None,
        birth_date=date(1936, 3, 28), death_date=None, country="Peru"
    )

    author25 = repo.authors.create(
        first_name="Sylvia", last_name="Plath", pseudonym=None,
        birth_date=date(1932, 10, 27), death_date=date(1963, 2, 11), country="USA"
    )

    author26 = repo.authors.create(
        first_name="Ken", last_name="Follett", pseudonym=None,
        birth_date=date(1949, 6, 5), death_date=None, country="UK"
    )

    author27 = repo.authors.create(
        first_name="Umberto", last_name="Eco", pseudonym=None,
        birth_date=date(1932, 1, 5), death_date=date(2016, 2, 19), country="Italy"
    )

    author28 = repo.authors.create(
        first_name="Chimamanda Ngozi", last_name="Adichie", pseudonym=None,
        birth_date=date(1977, 9, 15), death_date=None, country="Nigeria"
    )

    author29 = repo.authors.create(
        first_name="Terry", last_name="Pratchett", pseudonym=None,
        birth_date=date(1948, 4, 28), death_date=date(2015, 3, 12), country="UK"
    )

    author30 = repo.authors.create(
        first_name="Jodi", last_name="Picoult", pseudonym=None,
        birth_date=date(1966, 5, 19), death_date=None, country="USA"
    )

    author31 = repo.authors.create(
        first_name="Philip K.", last_name="Dick", pseudonym=None,
        birth_date=date(1928, 12, 16), death_date=date(1982, 3, 2), country="USA"
    )

    author32 = repo.authors.create(
        first_name="Alice", last_name="Munro", pseudonym=None,
        birth_date=date(1931, 7, 10), death_date=None, country="Canada"
    )

    author33 = repo.authors.create(
        first_name="Elif", last_name="Shafak", pseudonym=None,
        birth_date=date(1971, 10, 25), death_date=None, country="Turkey"
    )

    author34 = repo.authors.create(
        first_name="Stephen", last_name="King", pseudonym=None,
        birth_date=date(1947, 9, 21), death_date=None, country="USA"
    )

    author35 = repo.authors.create(
        first_name="Ayn", last_name="Rand", pseudonym=None,
        birth_date=date(1905, 2, 2), death_date=date(1982, 3, 6), country="Russia/USA"
    )

    author36 = repo.authors.create(
        first_name="Hermann", last_name="Hesse", pseudonym=None,
        birth_date=date(1877, 7, 2), death_date=date(1962, 8, 9), country="Germany"
    )

    author37 = repo.authors.create(
        first_name="Colleen", last_name="Hoover", pseudonym=None,
        birth_date=date(1979, 12, 11), death_date=None, country="USA"
    )

    author38 = repo.authors.create(
       first_name="Ray", last_name="Bradbury", pseudonym=None,
        birth_date=date(1920, 8, 22), death_date=date(2012, 6, 5), country="USA"
    )

    author39 = repo.authors.create(
        first_name="Gillian", last_name="Flynn", pseudonym=None,
        birth_date=date(1971, 2, 24), death_date=None, country="USA"
    )

    author40 = repo.authors.create(
        first_name="Victor", last_name="Hugo", pseudonym=None,
        birth_date=date(1802, 2, 26), death_date=date(1885, 5, 22), country="France"
    )

    author41 = repo.authors.create(
        first_name="T.S.", last_name="Eliot", pseudonym=None,
        birth_date=date(1888, 9, 26), death_date=date(1965, 1, 4), country="USA/UK"
    )

    author42 = repo.authors.create(
        first_name="Michel", last_name="Houellebecq", pseudonym=None,
        birth_date=date(1956, 2, 26), death_date=None, country="France"
    )

    author43 = repo.authors.create(
        first_name="Neil", last_name="Gaiman", pseudonym=None,
        birth_date=date(1960, 11, 10), death_date=None, country="UK"
    )

    author44 = repo.authors.create(
        first_name="James", last_name="Baldwin", pseudonym=None,
        birth_date=date(1924, 8, 2), death_date=date(1987, 12, 1), country="USA"
    )

    author45 = repo.authors.create(
       first_name="Jennifer", last_name="Egan", pseudonym=None,
       birth_date=date(1962, 9, 6), death_date=None, country="USA"
    )

    author46 = repo.authors.create(
        first_name="Patrick", last_name="Rothfuss", pseudonym=None,
        birth_date=date(1973, 6, 6), death_date=None, country="USA"
    )

    author47 = repo.authors.create(
        first_name="Rupi", last_name="Kaur", pseudonym=None,
        birth_date=date(1992, 10, 4), death_date=None, country="Canada"
    )

    author48 = repo.authors.create(
        first_name="S.E.", last_name="Hinton", pseudonym=None,
        birth_date=date(1948, 7, 22), death_date=None, country="USA"
    )

    author49 = repo.authors.create(
        first_name="Zora Neale", last_name="Hurston", pseudonym=None,
        birth_date=date(1891, 1, 7), death_date=date(1960, 1, 28), country="USA"
    )

    author50 = repo.authors.create(
        first_name="Amor", last_name="Towles", pseudonym=None,
        birth_date=date(1964, 1, 1), death_date=None, country="USA"
    )

    pub1 = repo.publishers.create(
        name="Penguin", email="contact@penguin.com", phone="1234567890", address="London, UK")

    pub2 = repo.publishers.create(
        name="Random House", email="info@randomhouse.com", phone="0987654321", address="New York, USA")

    pub3 = repo.publishers.create(
        name="Knopf Publishing Group", email="info@knopf.com", phone="0979812044", address="New York, USA")

    pub4 = repo.publishers.create(
        name="Bloomsbury", email="info@bloomsbury.com", phone="01122334455", address="London, UK"
    )

    pub5 = repo.publishers.create(
        name="Vintage", email="contact@vintage.com", phone="02233445566", address="New York, USA"
    )

    pub6 = repo.publishers.create(
        name="Scribner", email="contact@scribner.com", phone="1234567896", address="New York, USA")

    pub7 = repo.publishers.create(
        name="Faber and Faber", email="info@faber.co.uk", phone="1234567897", address="London, UK")

    pub8 = repo.publishers.create(
        name="HarperCollins", email="info@harpercollins.com", phone="1234567898", address="New York, USA")

    pub9 = repo.publishers.create(
        name="Simon & Schuster", email="contact@simonandschuster.com", phone="1234567899", address="New York, USA")

    pub10 = repo.publishers.create(
        name="Hachette Book Group", email="info@hachette.com", phone="1234567800", address="Boston, USA")

    book1 = repo.books.create(name="Murder on the Orient Express",
                              isbn="9780062693662", price=Decimal("15.00"), publisher=pub2)

    book2 = repo.books.create(
        name="New Age Book", isbn="1234567890123", price=Decimal("20.00"), publisher=pub2)

    book3 = repo.books.create(
        name="Kafka on the Shore", isbn="9781400079278", price=Decimal("18.50"), publisher=pub3)

    book4 = repo.books.create(
        name="1984",
        isbn="9780451524935", price=Decimal("14.00"), publisher=pub3)

    book5 = repo.books.create(
        name="The Old Man and the Sea",
        isbn="9780684801223", price=Decimal("13.50"), publisher=pub2)
    
    book6 = repo.books.create(
        name="Harry Potter and the Philosopher's Stone",
        isbn="9780747532699", price=Decimal("19.99"), publisher=pub4
    )   

    book7 = repo.books.create(
        name="War and Peace",
        isbn="9780199232765", price=Decimal("22.00"), publisher=pub5
    )

    book8 = repo.books.create(
        name="Pride and Prejudice",
        isbn="9780141439518", price=Decimal("12.50"), publisher=pub5
    )

    book9 = repo.books.create(
        name="Adventures of Huckleberry Finn",
        isbn="9780486280615", price=Decimal("11.00"), publisher=pub5
    )

    book10 = repo.books.create(
        name="The Great Gatsby",
        isbn="9780743273565", price=Decimal("14.50"), publisher=pub5
    )

    book11 = repo.books.create(
        name="Beloved",
        isbn="9781400033416", price=Decimal("16.00"), publisher=pub6)

    book12 = repo.books.create(
        name="One Hundred Years of Solitude",
        isbn="9780060883287", price=Decimal("17.50"), publisher=pub7)

    book13 = repo.books.create(
        name="The Handmaid's Tale",
        isbn="9780385490818", price=Decimal("15.50"), publisher=pub8)

    book14 = repo.books.create(
        name="To Kill a Mockingbird",
        isbn="9780061120084", price=Decimal("10.99"), publisher=pub9)
    
    book15 = repo.books.create(
    name="Mrs. Dalloway", isbn="9780156628709", price=Decimal("13.00"), publisher=pub1)

    book16 = repo.books.create(
        name="Things Fall Apart", isbn="9780385474542", price=Decimal("14.50"), publisher=pub2)

    book17 = repo.books.create(
        name="Moby Dick", isbn="9780142437247", price=Decimal("15.99"), publisher=pub3)

    book18 = repo.books.create(
        name="White Teeth", isbn="9780375703867", price=Decimal("17.00"), publisher=pub4)

    book19 = repo.books.create(
        name="The Stranger", isbn="9780679720201", price=Decimal("11.50"), publisher=pub5)

    book20 = repo.books.create(
        name="The House of the Spirits", isbn="9780553386014", price=Decimal("19.00"), publisher=pub6)

    book21 = repo.books.create(
        name="Slaughterhouse-Five", isbn="9780385312080", price=Decimal("14.00"), publisher=pub7)

    book22 = repo.books.create(
        name="The Hobbit", isbn="9780618260233", price=Decimal("21.50"), publisher=pub8)

    book23 = repo.books.create(
        name="The Kite Runner", isbn="9781594480003", price=Decimal("18.00"), publisher=pub9)

    book24 = repo.books.create(
        name="Kindred", isbn="9780807083697", price=Decimal("15.50"), publisher=pub10)

    book25 = repo.books.create(
        name="Never Let Me Go", isbn="9781400078776", price=Decimal("16.50"), publisher=pub1)

    book26 = repo.books.create(
        name="The Feast of the Goat", isbn="9780312423924", price=Decimal("19.50"), publisher=pub2)

    book27 = repo.books.create(
        name="The Bell Jar", isbn="9780061148514", price=Decimal("12.00"), publisher=pub3)

    book28 = repo.books.create(
        name="The Pillars of the Earth", isbn="9780451488114", price=Decimal("25.00"), publisher=pub4)

    book29 = repo.books.create(
        name="The Name of the Rose", isbn="9780156006037", price=Decimal("17.50"), publisher=pub5)

    book30 = repo.books.create(
        name="Americanah", isbn="9780307455925", price=Decimal("16.00"), publisher=pub6)

    book31 = repo.books.create(
        name="Mort", isbn="9780061054815", price=Decimal("13.50"), publisher=pub7)

    book32 = repo.books.create(
        name="My Sister's Keeper", isbn="9780743454537", price=Decimal("15.00"), publisher=pub8)

    book33 = repo.books.create(
        name="Do Androids Dream of Electric Sheep?", isbn="9780345404473", price=Decimal("14.50"), publisher=pub9)

    book34 = repo.books.create(
        name="Hateship, Friendship, Courtship, Loveship, Marriage", isbn="9780375727405", price=Decimal("13.00"), publisher=pub10)

    book35 = repo.books.create(
        name="The Forty Rules of Love", isbn="9780143119117", price=Decimal("17.00"), publisher=pub1)

    book36 = repo.books.create(
        name="The Shining", isbn="9780385121675", price=Decimal("16.50"), publisher=pub2)

    book37 = repo.books.create(
        name="Atlas Shrugged", isbn="9780451191147", price=Decimal("20.50"), publisher=pub3)

    book38 = repo.books.create(
        name="Siddhartha", isbn="9780553208774", price=Decimal("11.00"), publisher=pub4)

    book39 = repo.books.create(
        name="It Ends with Us", isbn="9781501110368", price=Decimal("15.00"), publisher=pub5)

    book40 = repo.books.create(
        name="Fahrenheit 451", isbn="9781451673319", price=Decimal("13.50"), publisher=pub6)

    book41 = repo.books.create(
        name="Gone Girl", isbn="9780307588371", price=Decimal("16.00"), publisher=pub7)

    book42 = repo.books.create(
        name="Les Misérables", isbn="9780451419439", price=Decimal("24.00"), publisher=pub8)

    book43 = repo.books.create(
        name="The Waste Land and Other Poems", isbn="9780156948885", price=Decimal("12.50"), publisher=pub9)
    
    book44 = repo.books.create(
        name="Submission", isbn="9780374270118", price=Decimal("18.00"), publisher=pub10)

    book45 = repo.books.create(
        name="American Gods", isbn="9780062483867", price=Decimal("19.99"), publisher=pub1)

    book46 = repo.books.create(
        name="Go Tell It on the Mountain", isbn="9780307275338", price=Decimal("14.50"), publisher=pub2)

    book47 = repo.books.create(
        name="A Visit from the Goon Squad", isbn="9780307592835", price=Decimal("17.00"), publisher=pub3)

    book48 = repo.books.create(
        name="The Name of the Wind", isbn="9780756404741", price=Decimal("22.00"), publisher=pub4)

    book49 = repo.books.create(
        name="Milk and Honey", isbn="9781449474256", price=Decimal("11.00"), publisher=pub5)

    book50 = repo.books.create(
        name="The Outsiders", isbn="9780140385724", price=Decimal("10.50"), publisher=pub6)

    client1 = repo.clients.create(
        first_name="Yaryna", last_name="Panychevska", email="pa.yaryna@gmail.com", phone="0979812088")

    client2 = repo.clients.create(
        first_name="Yaryna", last_name="Shcherban", email="yaryna.shcherban@gmail.com", phone="0979812099"
    )

    client3 = repo.clients.create(
        first_name="Dmytro", last_name="Kovalenko", email="dmytr.kov@example.com", phone="0979812100")

    client4 = repo.clients.create(
        first_name="Olena", last_name="Moroz", email="ole.moroz@example.com", phone="0979812101")
    client5 = repo.clients.create(first_name="Ivan", last_name="Petrenko", email="ivan.petrenko@example.com", phone="0971112233")
    client6 = repo.clients.create(first_name="Natalia", last_name="Koval", email="natalia.koval@example.com", phone="0672223344")
    client7 = repo.clients.create(first_name="Oleksandr", last_name="Tkachenko", email="o.tkachenko@example.com", phone="0503334455")
    client8 = repo.clients.create(first_name="Tetyana", last_name="Lysenko", email="tetyana.l@example.com", phone="0634445566")
    client9 = repo.clients.create(first_name="Serhiy", last_name="Melnyk", email="serhiy.melnyk@example.com", phone="0995556677")
    client10 = repo.clients.create(first_name="Viktoriya", last_name="Shevchuk", email="v.shevchuk@example.com", phone="0686667788")
    client11 = repo.clients.create(first_name="Andriy", last_name="Kuzmenko", email="andriy.k@example.com", phone="0737778899")
    client12 = repo.clients.create(first_name="Iryna", last_name="Zubko", email="iryna.zubko@example.com", phone="0968889900")
    client13 = repo.clients.create(first_name="Pavlo", last_name="Klimenko", email="pavlo.klimenko@example.com", phone="0970001122")
    client14 = repo.clients.create(first_name="Halyna", last_name="Bondar", email="halyna.bondar@example.com", phone="0671113355")
    client15 = repo.clients.create(first_name="Mykola", last_name="Boyko", email="mykola.boyko@example.com", phone="0502224466")
    client16 = repo.clients.create(first_name="Yuliya", last_name="Romanenko", email="yuliya.r@example.com", phone="0633335577")
    client17 = repo.clients.create(first_name="Roman", last_name="Volkov", email="roman.volkov@example.com", phone="0994446688")
    client18 = repo.clients.create(first_name="Zlata", last_name="Sydorenko", email="zlata.s@example.com", phone="0685557799")
    client19 = repo.clients.create(first_name="Maksym", last_name="Bilous", email="maksym.bilous@example.com", phone="0736668800")
    client20 = repo.clients.create(first_name="Kateryna", last_name="Vasilenko", email="kateryna.v@example.com", phone="0967779911")
    client21 = repo.clients.create(first_name="Denys", last_name="Hrytsenko", email="denys.h@example.com", phone="0978880022")
    client22 = repo.clients.create(first_name="Oksana", last_name="Marchenko", email="oksana.marchenko@example.com", phone="0679991133")
    client23 = repo.clients.create(first_name="Vasyl", last_name="Kostenko", email="vasyl.kostenko@example.com", phone="0500002244")
    client24 = repo.clients.create(first_name="Olha", last_name="Savchuk", email="olha.savchuk@example.com", phone="0631113355")
    
    book1.author.add(author1)
    book2.author.add(author1)
    book3.author.add(author2)
    book4.author.add(author3)
    book5.author.add(author4)
    book6.author.add(author5) 
    book7.author.add(author6)  
    book8.author.add(author7)  
    book9.author.add(author8)  
    book10.author.add(author9)
    book11.author.add(author10)
    book12.author.add(author11)
    book13.author.add(author12)
    book14.author.add(author13)
    book15.author.add(author13) 
    book16.author.add(author14) 
    book17.author.add(author15) 
    book18.author.add(author16) 
    book19.author.add(author17) 
    book20.author.add(author18) 
    book21.author.add(author19) 
    book22.author.add(author20) 
    book23.author.add(author21) 
    book24.author.add(author22) 
    book25.author.add(author23) 
    book26.author.add(author24) 
    book27.author.add(author25) 
    book28.author.add(author26) 
    book29.author.add(author27)
    book30.author.add(author28) 
    book31.author.add(author29) 
    book32.author.add(author30) 
    book33.author.add(author31) 
    book34.author.add(author32) 
    book35.author.add(author33) 
    book36.author.add(author34) 
    book37.author.add(author35) 
    book38.author.add(author36) 
    book39.author.add(author37) 
    book40.author.add(author38) 
    book41.author.add(author39) 
    book42.author.add(author40) 
    book43.author.add(author41) 
    book44.author.add(author42) 
    book45.author.add(author43) 
    book46.author.add(author44) 
    book47.author.add(author45) 
    book48.author.add(author46) 
    book49.author.add(author47) 
    book50.author.add(author48) 

    genre1 = repo.genres.create(name="Fiction")
    genre2 = repo.genres.create(name="Mystery")
    genre3 = repo.genres.create(name="Classic")
    genre4 = repo.genres.create(name="Adventure")
    genre5 = repo.genres.create(name="Dystopian")
    genre6 = repo.genres.create(name="Fantasy")
    genre7 = repo.genres.create(name="Self-Help")
    genre9 = repo.genres.create(name="Historical")
    genre10 = repo.genres.create(name="Romance")
    genre11 = repo.genres.create(name="Classic Literature")
    

    book1.genres.add(genre1, genre2, genre4)
    book2.genres.add(genre1, genre7)
    book3.genres.add(genre1, genre6, genre4)
    book4.genres.add(genre1, genre3, genre5)
    book5.genres.add(genre1, genre3, genre4)
    book6.genres.add(genre6)           
    book7.genres.add(genre1, genre9, genre11)     
    book8.genres.add(genre1, genre10, genre11)     
    book9.genres.add(genre1, genre4, genre11)      
    book10.genres.add(genre1, genre3, genre11)
    book11.genres.add(genre1, genre9)
    book12.genres.add(genre1, genre3)
    book13.genres.add(genre1, genre5)
    book14.genres.add(genre1, genre3, genre11)
    book15.genres.add(genre1, genre3, genre11) 
    book16.genres.add(genre1, genre3) 
    book17.genres.add(genre1, genre3, genre4, genre11) 
    book18.genres.add(genre1) 
    book19.genres.add(genre1, genre3)
    book20.genres.add(genre1, genre6) 
    book21.genres.add(genre1, genre5) 
    book22.genres.add(genre6, genre4) 
    book23.genres.add(genre1, genre9) 
    book24.genres.add(genre1, genre6) 
    book25.genres.add(genre1, genre5) 
    book26.genres.add(genre1) 
    book27.genres.add(genre1, genre3) 
    book28.genres.add(genre1, genre9) 
    book29.genres.add(genre1, genre2, genre9) 
    book30.genres.add(genre1) 
    book31.genres.add(genre6) 
    book32.genres.add(genre1) 
    book33.genres.add(genre5, genre6) 
    book34.genres.add(genre1) 
    book35.genres.add(genre1, genre10) 
    book36.genres.add(genre1) 
    book37.genres.add(genre1) 
    book38.genres.add(genre1, genre3, genre7) 
    book39.genres.add(genre1, genre10) 
    book40.genres.add(genre5) 
    book41.genres.add(genre1, genre2) 
    book42.genres.add(genre1, genre3, genre11) 
    book43.genres.add(genre11) 
    book44.genres.add(genre1, genre5)
    book45.genres.add(genre6, genre4) 
    book46.genres.add(genre1, genre3) 
    book47.genres.add(genre1) 
    book48.genres.add(genre6, genre4) 
    book49.genres.add(genre7) 
    book50.genres.add(genre1, genre3, genre11)

    purchase1 = repo.purchases.create(
        client=client1, employee=employee2, store=store1, total_amount=Decimal("29.00"))

    purchase_detail1 = repo.purchase_details.create(
        purchase=purchase1, book=book1, quantity=1, price_at_purchase=book1.price)

    purchase_detail1_2 = repo.purchase_details.create(
        purchase=purchase1, book=book4, quantity=1, price_at_purchase=book4.price)

    purchase2 = repo.purchases.create(
        client=client2, employee=employee2, store=store1, total_amount=Decimal("33.50"))

    purchase_detail2 = repo.purchase_details.create(
        purchase=purchase2, book=book2, quantity=1, price_at_purchase=book2.price)

    purchase_detail2_1 = repo.purchase_details.create(
        purchase=purchase2, book=book5, quantity=1,
        price_at_purchase=book5.price)
    
    purchase3 = repo.purchases.create(
        client=client3, employee=employee5, store=store2, total_amount=Decimal("47.50")) 

    purchase_detail3_1 = repo.purchase_details.create(
        purchase=purchase3, book=book11, quantity=1, price_at_purchase=book11.price)

    purchase_detail3_2 = repo.purchase_details.create(
        purchase=purchase3, book=book13, quantity=2, price_at_purchase=book13.price)

    purchase4 = repo.purchases.create(
        client=client4, employee=employee6, store=store2, total_amount=Decimal("17.50"))

    purchase_detail4_1 = repo.purchase_details.create(
        purchase=purchase4, book=book12, quantity=1, price_at_purchase=book12.price)

    purchase5 = repo.purchases.create(
        client=client5, employee=employee9, store=store3, total_amount=Decimal("30.50"))
    purchase_detail5_1 = repo.purchase_details.create(
        purchase=purchase5, book=book8, quantity=1, price_at_purchase=book8.price)
    purchase_detail5_2 = repo.purchase_details.create(
        purchase=purchase5, book=book27, quantity=1, price_at_purchase=book27.price) 
    purchase_detail5_3 = repo.purchase_details.create(
        purchase=purchase5, book=book49, quantity=1, price_at_purchase=book49.price) 


    purchase6 = repo.purchases.create(
        client=client6, employee=employee10, store=store3, total_amount=Decimal("41.00"))
    purchase_detail6_1 = repo.purchase_details.create(
        purchase=purchase6, book=book29, quantity=2, price_at_purchase=book29.price) 
    purchase_detail6_2 = repo.purchase_details.create(
        purchase=purchase6, book=book9, quantity=1, price_at_purchase=book9.price) 


    purchase7 = repo.purchases.create(
        client=client7, employee=employee13, store=store4, total_amount=Decimal("38.50"))
    purchase_detail7_1 = repo.purchase_details.create(
        purchase=purchase7, book=book14, quantity=1, price_at_purchase=book14.price) 
    purchase_detail7_2 = repo.purchase_details.create(
        purchase=purchase7, book=book44, quantity=1, price_at_purchase=book44.price) 
    purchase_detail7_3 = repo.purchase_details.create(
        purchase=purchase7, book=book34, quantity=1, price_at_purchase=book34.price) 

    purchase8 = repo.purchases.create(
        client=client8, employee=employee14, store=store4, total_amount=Decimal("52.50"))
    purchase_detail8_1 = repo.purchase_details.create(
        purchase=purchase8, book=book48, quantity=2, price_at_purchase=book48.price) 
    purchase_detail8_2 = repo.purchase_details.create(
        purchase=purchase8, book=book50, quantity=1, price_at_purchase=book50.price) 

    purchase9 = repo.purchases.create(
        client=client9, employee=employee17, store=store5, total_amount=Decimal("47.49"))
    purchase_detail9_1 = repo.purchase_details.create(
        purchase=purchase9, book=book6, quantity=2, price_at_purchase=book6.price) 
    purchase_detail9_2 = repo.purchase_details.create(
        purchase=purchase9, book=book17, quantity=1, price_at_purchase=book17.price)

    purchase10 = repo.purchases.create(
        client=client10, employee=employee18, store=store5, total_amount=Decimal("31.00"))
    purchase_detail10_1 = repo.purchase_details.create(
        purchase=purchase10, book=book24, quantity=2, price_at_purchase=book24.price) 

    purchase11 = repo.purchases.create(
        client=client11, employee=employee3, store=store1, total_amount=Decimal("56.50"))
    purchase_detail11_1 = repo.purchase_details.create(
        purchase=purchase11, book=book7, quantity=2, price_at_purchase=book7.price) 
    purchase_detail11_2 = repo.purchase_details.create(
        purchase=purchase11, book=book15, quantity=1, price_at_purchase=book15.price) 

    purchase12 = repo.purchases.create(
        client=client12, employee=employee4, store=store1, total_amount=Decimal("46.00"))
    purchase_detail12_1 = repo.purchase_details.create(
        purchase=purchase12, book=book36, quantity=1, price_at_purchase=book36.price) 
    purchase_detail12_2 = repo.purchase_details.create(
        purchase=purchase12, book=book45, quantity=1, price_at_purchase=book45.price) 
    purchase_detail12_3 = repo.purchase_details.create(
        purchase=purchase12, book=book43, quantity=1, price_at_purchase=book43.price) 

    purchase13 = repo.purchases.create(
        client=client13, employee=employee5, store=store2, total_amount=Decimal("28.00"))
    purchase_detail13_1 = repo.purchase_details.create(
        purchase=purchase13, book=book16, quantity=1, price_at_purchase=book16.price) 
    purchase_detail13_2 = repo.purchase_details.create(
        purchase=purchase13, book=book19, quantity=1, price_at_purchase=book19.price) 
    purchase_detail13_3 = repo.purchase_details.create(
        purchase=purchase13, book=book50, quantity=1, price_at_purchase=book50.price) 

    purchase14 = repo.purchases.create(
        client=client14, employee=employee6, store=store2, total_amount=Decimal("41.00"))
    purchase_detail14_1 = repo.purchase_details.create(
        purchase=purchase14, book=book47, quantity=1, price_at_purchase=book47.price) 
    purchase_detail14_2 = repo.purchase_details.create(
        purchase=purchase14, book=book33, quantity=1, price_at_purchase=book33.price) 
    purchase_detail14_3 = repo.purchase_details.create(
        purchase=purchase14, book=book39, quantity=1, price_at_purchase=book39.price) 

    purchase15 = repo.purchases.create(
        client=client15, employee=employee11, store=store3, total_amount=Decimal("38.00"))
    purchase_detail15_1 = repo.purchase_details.create(
        purchase=purchase15, book=book31, quantity=1, price_at_purchase=book31.price) 
    purchase_detail15_2 = repo.purchase_details.create(
        purchase=purchase15, book=book23, quantity=1, price_at_purchase=book23.price) 
    purchase_detail15_3 = repo.purchase_details.create(
        purchase=purchase15, book=book8, quantity=1, price_at_purchase=book8.price) 

    purchase16 = repo.purchases.create(
        client=client16, employee=employee12, store=store3, total_amount=Decimal("31.00"))
    purchase_detail16_1 = repo.purchase_details.create(
        purchase=purchase16, book=book40, quantity=2, price_at_purchase=book40.price) 
    purchase_detail16_2 = repo.purchase_details.create(
        purchase=purchase16, book=book49, quantity=1, price_at_purchase=book49.price) 

    purchase17 = repo.purchases.create(
        client=client17, employee=employee15, store=store4, total_amount=Decimal("51.00"))
    purchase_detail17_1 = repo.purchase_details.create(
        purchase=purchase17, book=book26, quantity=1, price_at_purchase=book26.price) 
    purchase_detail17_2 = repo.purchase_details.create(
        purchase=purchase17, book=book42, quantity=1, price_at_purchase=book42.price) 
    purchase_detail17_3 = repo.purchase_details.create(
        purchase=purchase17, book=book14, quantity=1, price_at_purchase=book14.price) 

    purchase18 = repo.purchases.create(
        client=client18, employee=employee16, store=store4, total_amount=Decimal("46.00"))
    purchase_detail18_1 = repo.purchase_details.create(
        purchase=purchase18, book=book22, quantity=2, price_at_purchase=book22.price) 
    purchase_detail18_2 = repo.purchase_details.create(
        purchase=purchase18, book=book38, quantity=1, price_at_purchase=book38.price) 

    purchase19 = repo.purchases.create(
        client=client19, employee=employee19, store=store5, total_amount=Decimal("38.50"))
    purchase_detail19_1 = repo.purchase_details.create(
        purchase=purchase19, book=book3, quantity=1, price_at_purchase=book3.price)
    purchase_detail19_2 = repo.purchase_details.create(
        purchase=purchase19, book=book32, quantity=1, price_at_purchase=book32.price) 
    purchase_detail19_3 = repo.purchase_details.create(
        purchase=purchase19, book=book2, quantity=1, price_at_purchase=book2.price) 

    purchase20 = repo.purchases.create(
        client=client20, employee=employee20, store=store5, total_amount=Decimal("35.00"))
    purchase_detail20_1 = repo.purchase_details.create(
        purchase=purchase20, book=book10, quantity=1, price_at_purchase=book10.price)
    purchase_detail20_2 = repo.purchase_details.create(
        purchase=purchase20, book=book25, quantity=1, price_at_purchase=book25.price) 
    purchase_detail20_3 = repo.purchase_details.create(
        purchase=purchase20, book=book49, quantity=1, price_at_purchase=book49.price) 

    purchase21 = repo.purchases.create(
        client=client21, employee=employee1, store=store1, total_amount=Decimal("26.00"))
    purchase_detail21_1 = repo.purchase_details.create(
        purchase=purchase21, book=book28, quantity=1, price_at_purchase=book28.price) 
    purchase_detail21_2 = repo.purchase_details.create(
        purchase=purchase21, book=book4, quantity=1, price_at_purchase=book4.price) 

    purchase22 = repo.purchases.create(
        client=client22, employee=employee7, store=store2, total_amount=Decimal("33.00"))
    purchase_detail22_1 = repo.purchase_details.create(
        purchase=purchase22, book=book30, quantity=2, price_at_purchase=book30.price) 
    purchase_detail22_2 = repo.purchase_details.create(
        purchase=purchase22, book=book1, quantity=1, price_at_purchase=book1.price) 

    purchase23 = repo.purchases.create(
        client=client23, employee=employee9, store=store3, total_amount=Decimal("43.00"))
    purchase_detail23_1 = repo.purchase_details.create(
        purchase=purchase23, book=book37, quantity=2, price_at_purchase=book37.price) 
    purchase_detail23_2 = repo.purchase_details.create(
        purchase=purchase23, book=book19, quantity=1, price_at_purchase=book19.price) 

    purchase24 = repo.purchases.create(
        client=client24, employee=employee13, store=store4, total_amount=Decimal("50.00"))
    purchase_detail24_1 = repo.purchase_details.create(
        purchase=purchase24, book=book41, quantity=1, price_at_purchase=book41.price) 
    purchase_detail24_2 = repo.purchase_details.create(
        purchase=purchase24, book=book35, quantity=2, price_at_purchase=book35.price) 
 


def demo_queries():
    from store.repositories.unit_of_work import UnitOfWork
    repo = UnitOfWork()

    # print("\n=== Демонстрація роботи репозиторіїв ===")

    # print("\n Усі автори з Великобританії (UK):")
    # for a in repo.authors.find_by_country("UK"):
    #     print(f"  - {a.first_name} {a.last_name}")

    # print("\n Автори, які ще живі:")
    # for a in repo.authors.get_alive_authors():
    #     print(f"  - {a.first_name} {a.last_name}")

    # print("\n Книги, ціна яких нижча за 16.00:")
    # for b in repo.books.get_books_cheaper_than(16.00):
    #     print(f"  - {b.name} ({b.price} $)")

    # print("\n Книги, які видав Penguin:")
    # publisher = repo.publishers.model.objects.get(name="Penguin")
    # for b in repo.books.get_books_by_publisher(publisher.publisher_id):
    #     print(f"  - {b.name}")

    # print("\n Усі працівники магазину:")
    # for e in repo.employees.get_all():
    #     print(f"  - {e.first_name} {e.last_name}, {e.position.role}")

    # print("\n Знайти працівників за посадою 'Sales Assistant':")
    # for e in repo.employees.get_by_position("Sales Assistant"):
    #     print(f"  - {e.first_name} {e.last_name}")

    # print("\n Пошук клієнта за email:")
    # client = repo.clients.find_by_email("pa.yaryna@gmail.com")
    # print(f"  - {client.first_name} {client.last_name}")

    # print("\n Посади з окладом від 1200 до 2000:")
    # for p in repo.positions.get_salary_range(1200, 2000):
    #     print(f"  - {p.role} ({p.salary} $)")

    # print("\n Всі покупки:")
    # for purchase in repo.purchases.get_all():
    #     print(
    #         f"  - Покупка #{purchase.purchase_id}, клієнт: {purchase.client.first_name}, сума: {purchase.total_amount} $")


if __name__ == "__main__":
    main()
    demo_queries()