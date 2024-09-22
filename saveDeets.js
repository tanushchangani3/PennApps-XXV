const express = require('express');
const fs = require('fs');
const { exec } = require('child_process');
const cors = require('cors'); // Import the cors package

const app = express();
app.use(express.json());

// Enable CORS for all routes
app.use(cors());  // This enables CORS for all requests from any origin

// Endpoint to save the email and trigger the Python and Node.js scripts
app.post('/save-deets', (req, res) => {
    const email = req.body.answer+"\n";
    console.log("writing saveDeets.txt");
    // Save email to emailAddress.txt
    // const content = email+"\n"+{name};
    fs.appendFile('saveDeets.txt', email, (err) => {
        if (err) {
            console.error('Error writing to saveDeets.txt:', err);
            return res.status(500).json({ message: 'Error saving email' });
        }
        });
});

// Start the server
app.listen(3005, () => {
    console.log('Server running on http://localhost:3005');
});
