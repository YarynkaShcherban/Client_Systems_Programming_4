import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home.jsx';
import UserList from './components/UserList.jsx';
import UserDetails from './components/UserDetails.jsx';
import UserCreate from './components/UserCreate.jsx';
import UserEdit from './components/UserEdit.jsx';
import Login from './components/Login.jsx';
import Register from './components/Register.jsx';
import BookList from './components/BookList.jsx';
import BookDetails from './components/BookDetails.jsx';
import BookForm from './components/BookForm.jsx';
import BookDelete from './components/BookDelete.jsx';
import BookStats from './components/BookStats.jsx';
import './css/main.css';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/home" element={<Home />} />
                <Route path="/register" element={<Register />} />
                <Route path="/login" element={<Login />} />
                <Route path="/users" element={<UserList />} />
                <Route path="/users/create" element={<UserCreate />} />
                <Route path="/users/:id" element={<UserDetails />} />
                <Route path="/users/:id/edit" element={<UserEdit />} />
                <Route path="/books" element={<BookList />} />
                <Route path="/books/stats" element={<BookStats />} />
                <Route path="/books/create" element={<BookForm />} />
                <Route path="/books/:id" element={<BookDetails />} />
                <Route path="/books/:id/edit" element={<BookForm />} />
                <Route path="/books/:id/delete" element={<BookDelete />} />
                <Route path="*" element={<Home />} />
            </Routes>
        </Router>
    );
}

export default App;
