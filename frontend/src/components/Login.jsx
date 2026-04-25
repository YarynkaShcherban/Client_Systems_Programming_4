import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { apiRequest } from '../services/api.js';

const Login = () => {
    const navigate = useNavigate();
    const [loginData, setLoginData] = useState({ email: '', password: '' });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setLoginData((prev) => ({ ...prev, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const clients = await apiRequest('clients/');
            const user = clients.find((c) => c.email.toLowerCase() === loginData.email.toLowerCase()
                && String(c.password) === String(loginData.password));

            if (user) {
                localStorage.setItem('user', JSON.stringify(user));
                navigate('/users');
            } else {
                window.alert('Невірний Email або пароль');
            }
        } catch (err) {
            window.alert('Помилка при спробі входу. Перевірте з’єднання з сервером.');
        }
    };

    return (
        <main className="main-content">
            <section className="auth-card">
                <h1>Авторизація</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Електронна пошта (Email)</label>
                        <input
                            type="email"
                            name="email"
                            value={loginData.email}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label>Пароль</label>
                        <input
                            type="password"
                            name="password"
                            value={loginData.password}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <button type="submit" className="btn-primary btn-block">Увійти</button>
                </form>
                <div className="text-center" style={{ marginTop: '20px' }}>
                    <p>Немає акаунта?</p>
                    <Link to="/register" className="btn-outline">Зареєструватися</Link>
                </div>
            </section>
        </main>
    );
};

export default Login;
