import React from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';

const CatalogLayout = ({ children }) => {
    const navigate = useNavigate();
    const location = useLocation();

    const handleLogout = () => {
        localStorage.removeItem('user');
        navigate('/home');
    };

    const isActive = (path) => location.pathname === path;

    return (
        <>
            <header className="header-bar">
                <div className="logo">bookstore</div>
                <div className="auth-nav">
                    <button
                        type="button"
                        onClick={handleLogout}
                        className="btn-danger"
                        style={{ cursor: 'pointer', border: 'none' }}
                    >
                        Вийти
                    </button>
                </div>
            </header>

            <div className="main-layout">
                <aside className="sidebar">
                    <nav>
                        <div className="sidebar-title">Каталог</div>
                        <ul className="sidebar-nav">
                            <li className="sidebar-nav-item">
                                <Link
                                    to="/books"
                                    className={`sidebar-nav-link${isActive('/books') ? ' sidebar-nav-link-active' : ''}`}
                                >
                                    Список книг
                                </Link>
                            </li>
                            <li className="sidebar-nav-item">
                                <Link
                                    to="/books/create"
                                    className={`sidebar-nav-link${isActive('/books/create') ? ' sidebar-nav-link-active' : ''}`}
                                >
                                    Додати книгу
                                </Link>
                            </li>
                            <li className="sidebar-nav-item">
                                <Link
                                    to="/books/stats"
                                    className={`sidebar-nav-link${isActive('/books/stats') ? ' sidebar-nav-link-active' : ''}`}
                                >
                                    Статистика
                                </Link>
                            </li>
                        </ul>

                        <div className="sidebar-title" style={{ marginTop: '30px' }}>Адміністрування</div>
                        <ul className="sidebar-nav">
                            <li className="sidebar-nav-item">
                                <Link
                                    to="/users"
                                    className={`sidebar-nav-link${location.pathname.startsWith('/users') ? ' sidebar-nav-link-active' : ''}`}
                                >
                                    Користувачі
                                </Link>
                            </li>
                            <li className="sidebar-nav-item">
                                <Link to="/home" className="sidebar-nav-link">
                                    На головну
                                </Link>
                            </li>
                        </ul>
                    </nav>
                </aside>

                <main className="content-area">
                    {children}
                </main>
            </div>
        </>
    );
};

export default CatalogLayout;
