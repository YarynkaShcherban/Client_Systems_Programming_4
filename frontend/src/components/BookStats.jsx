import React, { useState, useEffect } from 'react';
import { apiRequest } from '../services/api';
import CatalogLayout from './CatalogLayout.jsx';

const BookStats = () => {
    const [stats, setStats] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const load = async () => {
            try {
                const data = await apiRequest('books/stats/');
                setStats(data);
            } catch (err) {
                setError('Не вдалося завантажити статистику. Перевірте що endpoint /api/books/stats/ існує на бекенді.');
                console.error('Помилка завантаження статистики', err);
            }
        };
        load();
    }, []);

    if (error) {
        return (
            <CatalogLayout>
                <section className="management-wrapper">
                    <h1 style={{ marginBottom: '20px', color: '#2d4f3c', fontWeight: 400 }}>
                        Статистика книг
                    </h1>
                    <p style={{ color: '#c0392b' }}>{error}</p>
                </section>
            </CatalogLayout>
        );
    }

    if (!stats) {
        return (
            <CatalogLayout>
                <section className="management-wrapper">
                    <p>Завантаження...</p>
                </section>
            </CatalogLayout>
        );
    }

    return (
        <CatalogLayout>
            <section className="management-wrapper">
                <h1 style={{ marginBottom: '30px', color: '#2d4f3c', fontWeight: 400 }}>
                    Статистика книг
                </h1>

                <div className="stats-overview">
                    <div className="stat-card">
                        <div className="stat-value">{stats.overall?.total_books ?? '—'}</div>
                        <div className="stat-label">Книг усього</div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-value">
                            {stats.overall?.avg_price
                                ? `${parseFloat(stats.overall.avg_price).toFixed(2)} грн`
                                : '—'}
                        </div>
                        <div className="stat-label">Середня ціна</div>
                    </div>
                </div>

                <h2 className="stats-section-title">По жанрах</h2>
                <table className="user-table">
                    <thead>
                        <tr>
                            <th>Жанр</th>
                            <th>Кількість книг</th>
                            <th>Середня ціна</th>
                        </tr>
                    </thead>
                    <tbody>
                        {stats.genres && stats.genres.length > 0
                            ? stats.genres.map((g) => (
                                <tr key={g.name}>
                                    <td>{g.name}</td>
                                    <td>{g.num_books}</td>
                                    <td>
                                        {g.avg_price
                                            ? `${parseFloat(g.avg_price).toFixed(2)} грн`
                                            : '—'}
                                    </td>
                                </tr>
                            ))
                            : (
                                <tr>
                                    <td colSpan="3" style={{ textAlign: 'center' }}>Немає даних</td>
                                </tr>
                            )}
                    </tbody>
                </table>

                <h2 className="stats-section-title" style={{ marginTop: '40px' }}>По видавцях</h2>
                <table className="user-table">
                    <thead>
                        <tr>
                            <th>Видавець</th>
                            <th>Кількість книг</th>
                            <th>Середня ціна</th>
                        </tr>
                    </thead>
                    <tbody>
                        {stats.publishers && stats.publishers.length > 0
                            ? stats.publishers.map((p) => (
                                <tr key={p.name}>
                                    <td>{p.name}</td>
                                    <td>{p.num_books}</td>
                                    <td>
                                        {p.avg_price
                                            ? `${parseFloat(p.avg_price).toFixed(2)} грн`
                                            : '—'}
                                    </td>
                                </tr>
                            ))
                            : (
                                <tr>
                                    <td colSpan="3" style={{ textAlign: 'center' }}>Немає даних</td>
                                </tr>
                            )}
                    </tbody>
                </table>
            </section>
        </CatalogLayout>
    );
};

export default BookStats;
