const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');  // Add this line
const app = express();

// Enable CORS for all requests
app.use(cors());

// Middleware to parse JSON bodies
app.use(express.json());

// Route to handle form submission
app.post('/save-form', (req, res) => {
    const { firstName, lastName, email, password, linkedin } = req.body;

    // Format the data as a string
    const formData = `${firstName}\n${lastName}\n${email}\n${password}\n${linkedin}`;

    // Path to save the text file
    const filePath = path.join(__dirname, 'formData.txt');

    // Append form data to the file
    fs.appendFile(filePath, formData, (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            return res.status(500).json({ message: 'Error saving form data' });
        }

        console.log('Form data saved to formData.txt');
        res.json({ message: 'Form data saved successfully' });
    });
});

// Start the server
app.listen(3003, () => {
    console.log('Server is running on http://localhost:3003');
});
