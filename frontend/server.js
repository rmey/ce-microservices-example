const express = require('express');
const axios = require('axios');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 8080;
const SERVICE_URL = process.env.BACKEND_SERVICE_URL;

app.use(express.static(path.join(__dirname, '/public')));

app.get('/api/call-service', async (req, res) => {
    try {
        const response = await axios.get(SERVICE_URL);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ message: 'Backend is not reachable' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
