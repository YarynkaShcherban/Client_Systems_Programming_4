import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { apiRequest } from '../services/api';

const UserDetails = () => {
    const { id } = useParams();
    const [client, setClient] = useState(null);

    useEffect(() => {
        const loadDetails = async () => {
            try {
                const data = await apiRequest(`clients/${id}/`);
                setClient(data);
            } catch (err) {
                console.error('Помилка завантаження');
            }
        };
        loadDetails();
    }, [id]);

    if (!client) return <div className="container">Завантаження...</div>;

    return (
        <main className="main-content">
            <section className="user-card-detail">
                <h1>Профіль клієнта</h1>
                <span className="role-badge role-badge-regular">Постійний клієнт</span>
                <article className="user-info">
                    <div className="info-group">
                        <strong>Ім'я:</strong> <span>{client.first_name}</span>
                    </div>
                    <div className="info-group">
                        <strong>Прізвище:</strong> <span>{client.last_name}</span>
                    </div>
                    <div className="info-group">
                        <strong>Електронна пошта:</strong> <span>{client.email}</span>
                    </div>
                    <div className="info-group">
                        <strong>Номер телефону:</strong> <span>{client.phone}</span>
                    </div>
                </article>

                <div className="form-actions" style={{ marginTop: '20px', display: 'flex', gap: '10px' }}>
                    <Link to="/users" className="btn-primary">Назад до списку</Link>
                    <Link to={`/users/${id}/edit`} className="btn-success">Редагувати дані</Link>
                </div>
            </section>
        </main>
    );
};

export default UserDetails;
