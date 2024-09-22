import json
import textwrap

resume = resume_data = textwrap.dedent("\n Student Resume Data: " + """
PRANJAY KUMAR | pranjay.kumar@stern.nyu.edu | New York, NY | (908) 380-6875
EDUCATION
New York University, Leonard N. Stern School of Business, New York, NY
BS in Business Administration (Finance & Accounting) / MS in Accounting, Minor in Creative Writing Sep 2022 - May 2026
▪ GPA: 3.94/4.00 (Major GPA: 4.0) | Honors: Dean’s List (4x) | ACT: 35/36
▪ Extracurriculars: Venture Society (Tech Writer), Accounting Society (Outreach Dir.), Slam Poetry (Performer)
▪ Relevant coursework: Business & Society, Statistics, Organizational Communications, The Financial Service Industry
PROFESSIONAL EXPERIENCE
Citadel Securities, New York, NY
Incoming Fall Operations Intern, Expected Sep 2024
Latam Links (B2B Consulting Startup, Pre-Revenue Stage), Mexico City, MX
Head of Business Development, Jan 2024 - Present
▪ Driving digital marketing initiatives to link Mexican apparel manufacturers with domestic clothing retailers and distributors
▪ Developing CRM-based sales pipeline that reached 10k+ leads and utilized large language models and proprietary scrapers
▪ Overseeing a 5-person business development team, increasing productivity by 50% using RPA, LLMs, and CRM systems
Wiss & Company (Top 100 Accounting Firm), Florham Park, NJ
CFO Advisory Intern, Jun 2024 - Aug 2024
▪ Enhanced financial operations with 200+ financial reconciliations for $100M+ clients in Real Estate, CPG & Engineering
▪ Developed a resume review tool in collaboration with the tech advisory team using LLMs, cutting review time by 90%
▪ Created a Power BI financial dashboard utilizing Power Query and Power Pivot to enhance the decision-making process
Pulsar (E-Commerce Business Broker), New York, NY
Business Analyst Intern, Jan 2023 - Sep 2023
▪ Utilized NLP to analyze 40k+ fintech startups, differentiating offerings, leading to a 50% increase in signed mandates
▪ Led M&A analyst program, onboarding ten individuals to enhance post-transaction value through diverse perspectives
▪ Collaborated closely on CIM & financial model development for five e-commerce clients with EBITDA between $1-5M
New York City Office of the Comptroller (Pension Fund), New York, NY
Asset Management Operations Intern, Jun 2023 - Aug 2023
▪ Devised AI operation plan with Bureau of Asset Management executives, targeting 50% potential productivity increases
▪ Directed audits on 2k+ individual accounts, ensuring 99.8% accuracy in public data for investments valued at $255B
▪ Performed due diligence for Private Equity Funds (AUM $22B), pinpointing disparities and initiating resolutions with GPs
LEADERSHIP AND EXTRACURRICULAR ACTIVITIES
Stern School of Business, World Well-Being Project (LLM Research), New York, NY
Research Assistant, Jun 2023 - Present
▪ Analyzing 4 TB of conversational data using ML to create a custom dataset of 10M+ conversations for LLM fine-tuning
▪ Engineering versatile article web scraper with a 90% success rate, efficiently capturing 500k+ articles across 3,000+ sites
▪ Optimized RoBERTa, LLaMA, and OpenAI LLMs for empathy scoring on a curated dataset, targeting a 0.8 correlation
Stern School of Business, Turing Gardens (ML Research), New York, NY
Research Assistant, Jan 2023 - Jun 2023
▪ Worked with team of 5 individuals to create & optimize a secure, efficient article sharing platform for STEM professionals
▪ Developed a Q-learning greedy recommendation algorithm, achieving a 75% increase in recommendation subject diversity
▪ Improved accuracy and personalization by 60%, incorporating user history and reading time in recommendation algorithm
SKILLS & INTERESTS
Skills: Powerpoint, Excel, SQL, Java, Python, C++, Tableau, PowerBi, Power Query, Power Automate, Quickbooks, CapIQ
Interests: Flash Fiction, Slam Poetry, Weightlifting, Financial Literacy Education, Empathy-Driven Chatbots, Running
Certifications: Alteryx Designer Core
                """)
# Load the JSON file
with open('trainingData.json', 'r', encoding='utf-8') as f:
    profiles = json.load(f)

# Initialize an empty list to store the new format
formatted_data = []

# Iterate over each profile and transform the data
for profile in profiles:
    user_content = {
        "first_name": profile.get("first_name"),
        "last_name": profile.get("last_name"),
        "sub_title": profile.get("sub_title"),
        "location": profile.get("location"),
        "industry": profile.get("industry"),
        "current_company_name": profile.get("current_company_name"),
        "current_company_position": profile.get("current_company_position"),
        "skills": profile.get("skills"),
        "education": profile.get("education"),
        "position_groups": profile.get("position_groups"),
    }
    
    # Create the formatted message
    formatted_message = {
        "conversations": [
            {
                "role": "system",
                "content": (
                    "You are specializing in professional communication, tasked with composing a networking-focused cold email "
                    "from a student, Pranjay. Given the data from the professional and the student's resume, "
                    "your mission is to land a coffee chat. Personal Information about the student: Junior at NYU Stern Interested in Consulting. Make the networking email personalized to the receiver’s work experience, "
                    "preferences, and interests provided by the data. The text must sound authentic and human. Keep the email short, "
                    "100 to 200 words is ideal."
                )
            },
            {
                "role": "user",
                "content": "Professional LinkedIn Data: " + json.dumps(user_content, indent=4) + "\n\n" + resume
            },
            {
                "role": "assistant",
                "content": profile.get("email_text", "")  # Add the email text content here
            }
        ]
    }
    
    # Append to the formatted data list
    formatted_data.append(formatted_message)

# Save the formatted data to a new JSON file with UTF-8 encoding
with open('formatted_output.json', 'w', encoding='utf-8') as outfile:
    json.dump(formatted_data, outfile, indent=4, ensure_ascii=False)

print("Data successfully formatted and saved to 'formatted_output.json'")
