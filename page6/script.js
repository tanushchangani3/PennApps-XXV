// Sample JSON data
const alumniData = [
    {
        "name": "Hao Mack Yang L.",
        "role": "Fullstack Developer",
        "company": "Qiskit",
        "interests": ["Quantum Computing", "Freelance", "Math/Physics Teacher"],
        "experience": "3-5 years"
        "email": "hao.mack.yang@gmail.com"
    },
    {
        "name": "Birks Sachdev",
        "role": "Software Engineer",
        "company": "Salesforce",
        "interests": ["Entreprenuership", "Management", "Technology"],
        "experience": "2-3 years"
        "email": "bsachdev10@gmail.com"
    },
    {
        "name": "Dimple Bhanushali",
        "role": "Director of Operations",
        "company": "Freelance",
        "interests": ["Supply Chain Scientice", "Finance", "Sustainability"],
        "experience": "1-3 years"
        "email": "dimplebhanushali224@gmail.com"
    },
    {
        "name": "Nifasath A",
        "role": "Software Engineer",
        "company": "Agilent",
        "interests": ["Early-stage Ventures", "AI", "Technology"],
        "experience": "5-10 years"
        "email": "nifasathsa@gmail.com"
    },
    {
        "name": "Twinkle Mohan",
        "role": "Project Designer",
        "company": "Freedom Mortgage",
        "interests": ["Branding", "Products", "Designs"],
        "experience": "4-5 years"
        "email": "twinkle18mohan@gmail.com"
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
        card.appendChild(saveBtn);

        // Append card to alumni container
        alumniContainer.appendChild(card);
    });
}

// Call the function to generate alumni cards
createAlumniCards(alumniData);
