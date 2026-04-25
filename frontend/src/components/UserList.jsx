import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { apiRequest } from '../services/api.js';

const UserList = () => {
    const [users, setUsers] = useState([]);
    const navigate = useNavigate();

    const loadUsers = async () => {
        try {
            const data = await apiRequest('clients/');
            setUsers(data);
        } catch (error) {
            console.error('Не вдалося завантажити користувачів');
        }
    };

    const handleDelete = async (id) => {
        if (window.confirm('Видалити користувача?')) {
            await apiRequest(`clients/${id}/`, 'DELETE');
            loadUsers();
        }
    };

    const handleLogout = () => {
        localStorage.removeItem('user');
        navigate('/home');
    };

    useEffect(() => {
        loadUsers();
    }, []);

    return (
        <div className="container-wrapper">
            <header className="container header-bar">
                <div className="logo">bookstore</div>
                <button
                    type="button"
                    onClick={handleLogout}
                    className="btn-danger header-btn"
                    style={{ cursor: 'pointer', border: 'none' }}
                >
                    Вийти
                </button>
            </header>

            <main className="container">
                <section className="management-wrapper">
                    <header className="management-header" style={{ marginTop: '20px' }}>
                        <h1>Управління користувачами</h1>
                        <Link to="/users/create" className="btn-success">
                            + Новий користувач
                        </Link>
                    </header>

                    <table className="user-table">
                        <thead>
                            <tr>
                                <th>Логін (Ім'я та Прізвище)</th>
                                <th>Роль</th>
                                <th>Дії</th>
                            </tr>
                        </thead>
                        <tbody>
                            {users.map((user) => (
                                <tr key={user.client_id}>
                                    <td>{`${user.first_name} ${user.last_name}`}</td>
                                    <td>
                                        <span className="role-badge role-badge-regular">
                                            Клієнт
                                        </span>
                                    </td>
                                    <td>
                                        <div className="action-buttons">
                                            <Link
                                                to={`/users/${user.client_id}`}
                                                className="btn-primary"
                                            >
                                                Деталі
                                            </Link>
                                            <Link
                                                to={`/users/${user.client_id}/edit`}
                                                className="btn-success"
                                            >
                                                Редагувати
                                            </Link>
                                            <button
                                                type="button"
                                                className="btn-danger"
                                                onClick={() => handleDelete(user.client_id)}
                                            >
                                                Видалити
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </section>
            </main>
        </div>
    );
};

export default UserList;
