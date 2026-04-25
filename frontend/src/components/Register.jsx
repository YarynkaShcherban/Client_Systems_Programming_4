import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { apiRequest } from '../services/api.js';

const Register = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        password: '',
        confirm: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (formData.password !== formData.confirm) {
            window.alert('Паролі не збігаються');
            return;
        }

        try {
            await apiRequest('clients/', 'POST', {
                first_name: formData.first_name,
                last_name: formData.last_name,
                email: formData.email,
                phone: formData.phone,
                password: formData.password,
            });
            window.alert('Реєстрація успішна!');
            navigate('/login');
        } catch (err) {
            window.alert('Помилка при реєстрації. Перевірте дані.');
        }
    };

    return (
        <main className="main-content">
            <section className="auth-card">
                <h1>Реєстрація</h1>
                <p className="auth-description">Заповніть форму для створення профілю</p>
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
                        <label>Електронна пошта</label>
                        <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Номер телефону</label>
                        <input type="text" name="phone" value={formData.phone} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Пароль</label>
                        <input type="password" name="password" value={formData.password} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Підтвердження пароля</label>
                        <input type="password" name="confirm" value={formData.confirm} onChange={handleChange} required />
                    </div>
                    <button type="submit" className="btn-primary btn-block">Зареєструватися</button>
                </form>
                <Link to="/login" className="auth-link" style={{ display: 'block', textAlign: 'center', marginTop: '15px' }}>
                    Вже є акаунт? Увійти
                </Link>
            </section>
        </main>
    );
};

export default Register;
