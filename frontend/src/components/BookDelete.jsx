import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { apiRequest } from '../services/api';
import CatalogLayout from './CatalogLayout.jsx';

const BookDelete = () => {
    const { id } = useParams();
    const navigate = useNavigate();
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

    const handleDelete = async () => {
        try {
            await apiRequest(`books/${id}/`, 'DELETE');
            navigate('/books');
        } catch {
            window.alert('Помилка при видаленні книги');
        }
    };

    if (!book) return <div className="content-area">Завантаження...</div>;

    return (
        <CatalogLayout>
            <section className="user-card-detail" style={{ margin: 0, textAlign: 'center' }}>
                <h1>Видалення книги</h1>
                <p style={{ marginTop: '16px', fontSize: '16px' }}>
                    Ви впевнені, що хочете видалити:
                </p>
                <p style={{
                    fontWeight: 'bold', fontSize: '18px', color: '#2d4f3c', margin: '12px 0 24px',
                }}>
                    {book.name}
                </p>
                <div className="form-actions">
                    <button
                        type="button"
                        className="btn-danger btn-block"
                        onClick={handleDelete}
                    >
                        Так, видалити
                    </button>
                    <Link
                        to="/books"
                        className="btn-primary btn-block"
                        style={{ textAlign: 'center' }}
                    >
                        Скасувати
                    </Link>
                </div>
            </section>
        </CatalogLayout>
    );
};

export default BookDelete;
