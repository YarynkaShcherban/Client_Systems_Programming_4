const API_URL = 'http://127.0.0.1:8000/api';

export async function apiRequest(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
        },
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    const response = await fetch(`${API_URL}/${endpoint}`, options);

    if (response.status === 204) return true;
    if (!response.ok) throw new Error('Помилка мережі');

    return response.json();
}
