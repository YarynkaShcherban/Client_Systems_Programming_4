import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { apiRequest } from '../services/api';

const BOOKS_PER_PAGE = 8;

const Home = () => {
    const [books, setBooks] = useState([]);
    const [genres, setGenres] = useState([]);
    const [selectedGenre, setSelectedGenre] = useState(null);
    const [currentPage, setCurrentPage] = useState(1);
    const navigate = useNavigate();

    const user = JSON.parse(localStorage.getItem('user') || 'null');

    const loadData = async () => {
        try {
            const [booksData, genresData] = await Promise.all([
                apiRequest('books/'),
                apiRequest('genres/'),
            ]);
            setBooks(booksData);
            setGenres(genresData);
        } catch {
            console.error('Помилка завантаження даних');
        }
    };

    useEffect(() => {
        loadData();
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('user');
        navigate('/home');
    };

    const filtered = selectedGenre
        ? books.filter((b) => b.genre_ids && b.genre_ids.includes(selectedGenre))
        : books;

    const totalPages = Math.ceil(filtered.length / BOOKS_PER_PAGE);
    const paginated = filtered.slice(
        (currentPage - 1) * BOOKS_PER_PAGE,
        currentPage * BOOKS_PER_PAGE,
    );

    const handleGenreChange = (genreId) => {
        setSelectedGenre(genreId);
        setCurrentPage(1);
    };

    return (
        <>
            <header className="header-bar">
                <div className="logo">bookstore</div>
                <div className="auth-nav">
                    {user ? (
                        <button
                            type="button"
                            onClick={handleLogout}
                            className="btn-danger"
                            style={{ cursor: 'pointer', border: 'none' }}
                        >
                            Вийти
                        </button>
                    ) : (
                        <>
                            <Link to="/register" className="btn-outline">Зареєструватись</Link>
                            <Link to="/login" className="btn-primary" style={{ width: 'auto' }}>Увійти</Link>
                        </>
                    )}
                </div>
            </header>

            <div className="main-layout">
                <aside className="sidebar">
                    <nav>
                        <div className="sidebar-title">Каталог</div>
                        <ul className="sidebar-nav">
                            <li className="sidebar-nav-item">
                                <Link to="/home" className="sidebar-nav-link">Всі книги</Link>
                            </li>
                            <li className="sidebar-nav-item">
                                <Link to="/books/create" className="sidebar-nav-link">Додати книгу</Link>
                            </li>
                            <li className="sidebar-nav-item">
                                <Link to="/books/stats" className="sidebar-nav-link">Статистика</Link>
                            </li>
                        </ul>

                        <div className="sidebar-title" style={{ marginTop: '30px' }}>Адміністрування</div>
                        <ul className="sidebar-nav">
                            <li className="sidebar-nav-item">
                                <Link to="/users" className="sidebar-nav-link">Користувачі</Link>
                            </li>
                        </ul>
                    </nav>
                </aside>

                <main className="content-area">
                    <div className="management-wrapper">
                        <header className="management-header">
                            <h1>
                                {selectedGenre
                                    ? `Книги жанру: ${genres.find((g) => g.genre_id === selectedGenre)?.name}`
                                    : 'Список усіх книг'}
                            </h1>
                            <Link to="/books/create" className="btn-success">
                                + Додати нову книгу
                            </Link>
                        </header>

                        <div className="genre-filter">
                            <button
                                type="button"
                                className={`genre-chip${!selectedGenre ? ' genre-chip-active' : ''}`}
                                onClick={() => handleGenreChange(null)}
                            >
                                Усі
                            </button>
                            {genres.map((g) => (
                                <button
                                    key={g.genre_id}
                                    type="button"
                                    className={`genre-chip${selectedGenre === g.genre_id ? ' genre-chip-active' : ''}`}
                                    onClick={() => handleGenreChange(g.genre_id)}
                                >
                                    {g.name}
                                </button>
                            ))}
                        </div>

                        {paginated.length === 0 ? (
                            <p className="catalog-empty">Не знайдено книг за цими критеріями.</p>
                        ) : (
                            <div className="book-grid">
                                {paginated.map((book) => (
                                    <div key={book.book_id} className="book-card">
                                        {book.image ? (
                                            <img
                                                src={`http://127.0.0.1:8000${book.image}`}
                                                alt={book.name}
                                                className="book-card-img"
                                            />
                                        ) : (
                                            <div className="book-card-no-img">
                                                <span>Немає фото</span>
                                            </div>
                                        )}
                                        <div className="book-card-body">
                                            <h5 className="book-card-title">{book.name}</h5>
                                            <p className="book-card-meta">
                                                <strong>Автор:</strong>
                                                {' '}
                                                {book.author_names || '—'}
                                            </p>
                                            <p className="book-card-meta">
                                                <strong>Ціна:</strong>
                                                {' '}
                                                {book.price ? `${book.price} грн` : '—'}
                                            </p>
                                            <p className="book-card-meta">
                                                <strong>Видавництво:</strong>
                                                {' '}
                                                {book.publisher_name || '—'}
                                            </p>
                                            <p className="book-card-meta">
                                                <strong>ISBN:</strong>
                                                {' '}
                                                {book.isbn || '—'}
                                            </p>
                                            <div className="action-buttons" style={{ marginTop: '12px' }}>
                                                <Link to={`/books/${book.book_id}`} className="btn-primary">
                                                    Деталі
                                                </Link>
                                                <Link to={`/books/${book.book_id}/edit`} className="btn-success">
                                                    Редагувати
                                                </Link>
                                                <Link to={`/books/${book.book_id}/delete`} className="btn-danger">
                                                    Видалити
                                                </Link>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}

                        {totalPages > 1 && (
                            <div className="pagination">
                                <button
                                    type="button"
                                    className={`page-btn${currentPage === 1 ? ' page-btn-disabled' : ''}`}
                                    onClick={() => setCurrentPage((p) => Math.max(1, p - 1))}
                                    disabled={currentPage === 1}
                                >
                                    «
                                </button>
                                {Array.from({ length: totalPages }, (_, i) => i + 1).map((num) => (
                                    <button
                                        key={num}
                                        type="button"
                                        className={`page-btn${currentPage === num ? ' page-btn-active' : ''}`}
                                        onClick={() => setCurrentPage(num)}
                                    >
                                        {num}
                                    </button>
                                ))}
                                <button
                                    type="button"
                                    className={`page-btn${currentPage === totalPages
                                        ? ' page-btn-disabled' : ''}`}
                                    onClick={
                                        () => setCurrentPage((p) => Math.min(totalPages, p + 1))
                                    }
                                    disabled={currentPage === totalPages}
                                >
                                    »
                                </button>
                            </div>
                        )}
                    </div>
                </main>
            </div>
        </>
    );
};

export default Home;
