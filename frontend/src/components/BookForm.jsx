import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { apiRequest } from '../services/api';
import CatalogLayout from './CatalogLayout.jsx';

const BookForm = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const isEdit = Boolean(id);

    const [formData, setFormData] = useState({
        name: '',
        isbn: '',
        price: '',
        publisher: '',
        authors: [],
        genres: [],
    });
    const [publishers, setPublishers] = useState([]);
    const [allAuthors, setAllAuthors] = useState([]);
    const [allGenres, setAllGenres] = useState([]);

    useEffect(() => {
        const loadOptions = async () => {
            try {
                const [pubData, authData, genData] = await Promise.all([
                    apiRequest('publishers/'),
                    apiRequest('authors/'),
                    apiRequest('genres/'),
                ]);
                setPublishers(pubData);
                setAllAuthors(authData);
                setAllGenres(genData);
            } catch {
                console.error('Помилка завантаження даних форми');
            }
        };
        loadOptions();
    }, []);

    useEffect(() => {
        if (!isEdit) return;
        const loadBook = async () => {
            try {
                const data = await apiRequest(`books/${id}/`);
                setFormData({
                    name: data.name || '',
                    isbn: data.isbn || '',
                    price: data.price || '',
                    publisher: data.publisher || '',
                    authors: (data.author_list || []).map((a) => a.id),
                    genres: (data.genre_list || []).map((g) => g.id),
                });
            } catch {
                console.error('Помилка завантаження книги');
            }
        };
        loadBook();
    }, [id, isEdit]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const handleMultiCheck = (field, itemId) => {
        setFormData((prev) => {
            const current = prev[field];
            const updated = current.includes(itemId)
                ? current.filter((v) => v !== itemId)
                : [...current, itemId];
            return { ...prev, [field]: updated };
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const payload = {
            name: formData.name,
            isbn: formData.isbn || null,
            price: formData.price || null,
            publisher: formData.publisher || null,
            authors: formData.authors,
            genres: formData.genres,
        };
        try {
            if (isEdit) {
                await apiRequest(`books/${id}/`, 'PATCH', payload);
            } else {
                await apiRequest('books/', 'POST', payload);
            }
            navigate('/home');
        } catch {
            window.alert('Помилка при збереженні книги');
        }
    };

    return (
        <CatalogLayout>
            <section className="auth-card" style={{ margin: 0 }}>
                <h1>{isEdit ? 'Редагувати книгу' : 'Нова книга'}</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Назва</label>
                        <input
                            type="text"
                            name="name"
                            value={formData.name}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label>ISBN</label>
                        <input
                            type="text"
                            name="isbn"
                            value={formData.isbn}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="form-group">
                        <label>Ціна (грн)</label>
                        <input
                            type="number"
                            name="price"
                            value={formData.price}
                            onChange={handleChange}
                            step="0.01"
                            min="0"
                        />
                    </div>
                    <div className="form-group">
                        <label>Видавництво</label>
                        <select
                            name="publisher"
                            value={formData.publisher}
                            onChange={handleChange}
                        >
                            <option value="">— Оберіть —</option>
                            {publishers.map((p) => (
                                <option key={p.publisher_id} value={p.publisher_id}>
                                    {p.name}
                                </option>
                            ))}
                        </select>
                    </div>
                    <div className="form-group">
                        <label>Автори</label>
                        <div className="checkbox-group">
                            {allAuthors.map((a) => (
                                <label key={a.author_id} className="checkbox-label">
                                    <input
                                        type="checkbox"
                                        checked={formData.authors.includes(a.author_id)}
                                        onChange={() => handleMultiCheck('authors', a.author_id)}
                                        style={{ width: 'auto', height: 'auto', display: 'inline' }}
                                    />
                                    {' '}
                                    {a.first_name}
                                    {' '}
                                    {a.last_name}
                                </label>
                            ))}
                        </div>
                    </div>
                    <div className="form-group">
                        <label>Жанри</label>
                        <div className="checkbox-group">
                            {allGenres.map((g) => (
                                <label key={g.genre_id} className="checkbox-label">
                                    <input
                                        type="checkbox"
                                        checked={formData.genres.includes(g.genre_id)}
                                        onChange={() => handleMultiCheck('genres', g.genre_id)}
                                        style={{ width: 'auto', height: 'auto', display: 'inline' }}
                                    />
                                    {' '}
                                    {g.name}
                                </label>
                            ))}
                        </div>
                    </div>
                    <div style={{ display: 'flex', gap: '10px', marginTop: '25px' }}>
                        <button type="submit" className="btn-success btn-block">
                            {isEdit ? 'Зберегти зміни' : 'Створити'}
                        </button>
                        <Link
                            to="/home"
                            className="btn-danger btn-block"
                            style={{ textAlign: 'center' }}
                        >
                            Скасувати
                        </Link>
                    </div>
                </form>
            </section>
        </CatalogLayout>
    );
};

export default BookForm;
