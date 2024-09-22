const express = require('express');
const fs = require('fs');
const { exec } = require('child_process');
const cors = require('cors'); // Import the cors package

const app = express();
app.use(express.json());

// Enable CORS for all routes
app.use(cors());  // This enables CORS for all requests from any origin

// Endpoint to save the email and trigger the Python and Node.js scripts
app.post('/send-email', (req, res) => {
    const email = req.body.email;
    console.log("writing emailAddress.txt");
    // Save email to emailAddress.txt
    // const content = email+"\n"+{name};
    fs.writeFile('emailAddress.txt', email, (err) => {
        if (err) {
            console.error('Error writing to emailAddress.txt:', err);
            return res.status(500).json({ message: 'Error saving email' });
        }

        // Run the Python script to generate the email text
        setTimeout(()=>{}, 2000)
        console.log("exec python");
        exec('python prompt_maker.py', (error, stdout, stderr) => {
            if (error) {
                console.error(`Error running Python script: ${stderr}`);
                return res.status(500).json({ message: 'Error generating email content' });
            }

            // Add a delay before sending the email
            setTimeout(() => {
                // Run the Node.js script to send the email
                console.log("exec node");
                exec('node gmailSender.js', (error, stdout, stderr) => {
                    if (error) {
                        console.error(`Error running gmailSender.js: ${stderr}`);
                        return res.status(500).json({ message: 'Error sending email' });
                    }

                    console.log('Email sent successfully:', stdout);
                    res.json({ message: 'Email sent successfully' });
                });
            }, 2000);  // 2 second delay
        });
    });
});

// Start the server
app.listen(3002, () => {
    console.log('Server running on http://localhost:3002');
});
