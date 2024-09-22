// const fs = require('fs');

// Sample JSON data
const alumniData = [
    {
        "name": "John Doe",
        "role": "Senior Consultant",
        "company": "ABC Corp",
        "interests": ["Networking", "Consulting", "Finance"],
        "experience": "3-5 years",
        "email": "example@example.com"
    },
    {
        "name": "Jane Smith",
        "role": "Project Manager",
        "company": "XYZ Ltd",
        "interests": ["Leadership", "Consulting", "Marketing"],
        "experience": "5-10 years",
        "email": "example@example.com"
    },
    {
        "name": "Michael Brown",
        "role": "Data Analyst",
        "company": "DataTech",
        "interests": ["Analytics", "Big Data", "Finance"],
        "experience": "1-3 years",
        "email": "example@example.com"
    },
    {
        "name": "Jane Smith",
        "role": "Project Manager",
        "company": "XYZ Ltd",
        "interests": ["Leadership", "Consulting", "Marketing"],
        "experience": "5-10 years",
        "email": "example@example.com"
    },
    {
        "name": "Jane Smith",
        "role": "Project Manager",
        "company": "XYZ Ltd",
        "interests": ["Leadership", "Consulting", "Marketing"],
        "experience": "5-10 years",
        "email": "example@example.com"
    },
];

// Function to create alumni cards dynamically
function createAlumniCards(alumniData) {
    const alumniContainer = document.getElementById('alumni-container');

    alumniData.forEach(alumni => {
        const card = document.createElement('div');
        card.className = 'alumni-card';

        // Add profile placeholder
        const profilePlaceholder = document.createElement('div');
        profilePlaceholder.className = 'profile-placeholder';
        profilePlaceholder.innerHTML = alumni.name.charAt(0);  // First letter of the name
        card.appendChild(profilePlaceholder);

        // Add name, role, and company
        const name = document.createElement('h4');
        name.textContent = alumni.name;
        card.appendChild(name);

        const role = document.createElement('p');
        role.textContent = alumni.role;
        card.appendChild(role);

        const company = document.createElement('p');
        company.textContent = alumni.company;
        card.appendChild(company);

        // Add interests as tags
        alumni.interests.slice(0, 2).forEach(interest => {
            const tag = document.createElement('span');
            tag.className = 'tag';
            tag.textContent = interest;
            card.appendChild(tag);
        });        

        // Add experience as a tag
        const experienceTag = document.createElement('span');
        experienceTag.className = 'experience-tag tag';
        experienceTag.textContent = alumni.experience;
        card.appendChild(experienceTag);

        // Add save button
        const saveBtn = document.createElement('button');
        saveBtn.className = 'save-btn';
        saveBtn.textContent = 'Send Email';
        saveBtn.onclick = function () {
            // When clicked, save email to file and trigger python script and Node.js
            sendEmail(alumni.email);
        };
        card.appendChild(saveBtn);



        // Append card to alumni container
        alumniContainer.appendChild(card);
    });
}

function sendEmail(email) {
    fetch('http://localhost:3002/send-email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email })
    })
    .then(response => response.json())
    .then(data => console.log('Email sent:', data.message))
    .catch(err => console.error('Error sending email:', err));
}

// Call the function to generate alumni cards
createAlumniCards(alumniData);
