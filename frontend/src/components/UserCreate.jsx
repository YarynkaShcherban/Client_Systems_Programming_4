import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { apiRequest } from '../services/api';

const UserCreate = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await apiRequest('clients/', 'POST', formData);
            navigate('/users');
        } catch (err) {
            window.alert('Помилка при створенні клієнта');
        }
    };

    return (
        <main className="main-content">
            <section className="auth-card">
                <h1>Новий клієнт</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Ім'я</label>
                        <input type="text" name="first_name" value={formData.first_name} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Прізвище</label>
                        <input type="text" name="last_name" value={formData.last_name} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Email</label>
                        <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Телефон</label>
                        <input type="text" name="phone" value={formData.phone} onChange={handleChange} required />
                    </div>
                    <div style={{ display: 'flex', gap: '10px', marginTop: '25px' }}>
                        <button type="submit" className="btn-success btn-block">Створити</button>
                        <Link to="/users" className="btn-danger btn-block" style={{ textAlign: 'center' }}>Скасувати</Link>
                    </div>
                </form>
            </section>
        </main>
    );
};

export default UserCreate;
