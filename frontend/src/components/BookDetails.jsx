import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { apiRequest } from '../services/api';
import CatalogLayout from './CatalogLayout.jsx';

const BookDetails = () => {
    const { id } = useParams();
    const [book, setBook] = useState(null);

    useEffect(() => {
        const load = async () => {
            try {
                const data = await apiRequest(`books/${id}/`);
                setBook(data);
            } catch {
                console.error('Помилка завантаження книги');
            }
        };
        load();
    }, [id]);

    if (!book) return <div className="content-area">Завантаження...</div>;

    const genreNames = book.genre_names
        ? book.genre_names.split(',').map((g) => g.trim()).filter(Boolean)
        : [];

    return (
        <CatalogLayout>
            <section className="user-card-detail" style={{ maxWidth: '560px', margin: 0 }}>
                <h1>Деталі книги</h1>

                {book.image && (
                    <div style={{ marginBottom: '20px', textAlign: 'center' }}>
                        <img
                            src={`http://127.0.0.1:8000${book.image}`}
                            alt={book.name}
                            style={{
                                maxWidth: '200px',
                                borderRadius: '4px',
                                border: '1px solid #e0d8c3',
                            }}
                        />
                    </div>
                )}

                <article className="user-info">
                    <div className="info-group">
                        <strong>Назва:</strong>
                        {' '}
                        <span>{book.name}</span>
                    </div>
                    <div className="info-group">
                        <strong>ISBN:</strong>
                        {' '}
                        <span>{book.isbn || '—'}</span>
                    </div>
                    <div className="info-group">
                        <strong>Ціна:</strong>
                        {' '}
                        <span>{book.price ? `${book.price} грн` : '—'}</span>
                    </div>
                    <div className="info-group">
                        <strong>Видавництво:</strong>
                        {' '}
                        <span>{book.publisher_name || '—'}</span>
                    </div>
                    <div className="info-group">
                        <strong>Автори:</strong>
                        {' '}
                        <span>{book.author_names || '—'}</span>
                    </div>
                    <div className="info-group">
                        <strong>Жанри:</strong>
                        {' '}
                        <span>
                            {genreNames.length > 0
                                ? genreNames.map((g) => (
                                    <span
                                        key={g}
                                        className="role-badge role-badge-regular"
                                        style={{ marginRight: '4px' }}
                                    >
                                        {g}
                                    </span>
                                ))
                                : '—'}
                        </span>
                    </div>
                </article>

                <div className="form-actions" style={{ marginTop: '20px' }}>
                    <Link to="/books" className="btn-primary">Назад</Link>
                    <Link to={`/books/${id}/edit`} className="btn-success">Редагувати</Link>
                    <Link to={`/books/${id}/delete`} className="btn-danger">Видалити</Link>
                </div>
            </section>
        </CatalogLayout>
    );
};

export default BookDetails;
