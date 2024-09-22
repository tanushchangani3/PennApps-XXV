const fs = require('fs');
const path = require('path');
const { google } = require('googleapis');

// Path to your credentials.json file
const CREDENTIALS_PATH = path.join(__dirname, 'credentials.json');
const TOKEN_PATH = path.join(__dirname, 'token.json');

// Scopes for Gmail API access
const SCOPES = ['https://www.googleapis.com/auth/gmail.send'];

// Load client secrets from credentials file
fs.readFile(CREDENTIALS_PATH, (err, content) => {
    if (err) return console.log('Error loading client secret file:', err);
    authorize(JSON.parse(content), sendEmail);
});

// Create an OAuth2 client
function authorize(credentials, callback) {
    const { client_secret, client_id, redirect_uris } = credentials.installed;
    const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);

    // Check if token already exists
    fs.readFile(TOKEN_PATH, (err, token) => {
        if (err) return getAccessToken(oAuth2Client, callback);
        oAuth2Client.setCredentials(JSON.parse(token));
        callback(oAuth2Client);
    });
}

// Get access token if no token is available
function getAccessToken(oAuth2Client, callback) {
    const authUrl = oAuth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: SCOPES,
    });
    console.log('Authorize this app by visiting this URL:', authUrl);
    const rl = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout,
    });
    rl.question('Enter the code from that page here: ', (code) => {
        rl.close();
        oAuth2Client.getToken(code, (err, token) => {
            if (err) return console.error('Error retrieving access token', err);
            oAuth2Client.setCredentials(token);
            // Store the token for future use
            fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
                if (err) return console.error(err);
                console.log('Token stored to', TOKEN_PATH);
            });
            callback(oAuth2Client);
        });
    });
}

// Send email using Gmail API
function sendEmail(auth) {
    const gmail = google.gmail({ version: 'v1', auth });
    const email = createEmail();
    const encodedEmail = Buffer.from(email).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');

    gmail.users.messages.send({
        userId: 'me',
        resource: {
            raw: encodedEmail,
        },
    }, (err, res) => {
        if (err) return console.log('The API returned an error: ' + err);
        console.log('Email sent:', res.data);
    });
}

// Create email in RFC822 format
function createEmail() {
    const subject = 'Subject: Test Email from Node.js';
    const body = 'Hello,\n\nThis is a test email sent from a Node.js app using the Gmail API.';
    const email = [
        'From: "Your Name" <your-email@gmail.com>',
        'To: recipient@example.com',
        subject,
        'Content-Type: text/plain; charset=utf-8',
        'Content-Transfer-Encoding: 7bit',
        '',
        body,
    ].join('\n');
    return email;
}
