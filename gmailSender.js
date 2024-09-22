const express = require('express');
const app = express();
const { google } = require('googleapis');
const fs = require('fs');
const path = require('path');

const CREDENTIALS_PATH = path.join(__dirname, 'credentials.json');
const TOKEN_PATH = path.join(__dirname, 'token.json');

const SCOPES = ['https://www.googleapis.com/auth/gmail.send'];

let email_text

fetch('data.json')
            .then(response => response.json())
            .then(data => {
                console.log("Python Variable from JSON:", data.python_variable);
            });


fs.readFile(CREDENTIALS_PATH, (err, content) => {
    if (err) return console.log('Error loading client secret file:', err);
    authorize(JSON.parse(content), sendEmail());
});

function authorize(credentials, callback) {
    const { client_secret, client_id, redirect_uris } = credentials.web;
    const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);

    fs.readFile(TOKEN_PATH, (err, token) => {
        if (err) return getAccessToken(oAuth2Client, callback);
        oAuth2Client.setCredentials(JSON.parse(token));
        callback(oAuth2Client);
    });
}

function getAccessToken(oAuth2Client, callback) {
    const authUrl = oAuth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: SCOPES,
    });
    console.log('Authorize this app by visiting this URL:', authUrl);

    app.get('/', (req, res) => {
        const code = req.query.code;
        if (code) {
            oAuth2Client.getToken(code, (err, token) => {
                if (err) return res.send('Error retrieving access token: ' + err);
                oAuth2Client.setCredentials(token);
                fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
                    if (err) console.error(err);
                    console.log('Token stored to', TOKEN_PATH);
                });
                callback(oAuth2Client);
                res.send('Authorization successful! You can close this tab.');
            });
        }
    });
}

function sendEmail(auth) {
    const gmail = google.gmail({ version: 'v1', auth });
    const email = createEmail();
    const encodedEmail = Buffer.from(email).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');

    gmail.users.messages.send({
        userId: 'me',
        resource: { raw: encodedEmail },
    }, (err, res) => {
        if (err) return console.log('The API returned an error: ' + err);
        console.log('Email sent:', res.data);
    });
}

function createEmail(emailText) {
    return [
        'From: "Your Name" <your-email@gmail.com>',
        'To: recipient@example.com',
        'Subject: Test Email from Node.js',
        'Content-Type: text/plain; charset=utf-8',
        '',
        emailText
    ].join('\n');
}

app.listen(3000, () => {
    console.log('Server started on http://localhost:3000');
});
