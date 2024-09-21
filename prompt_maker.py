import json
import textwrap
import csv
import pandas as pd
import json
import requests
# Replace resume data as needed

stream = False
url = "https://proxy.tune.app/chat/completions"
headers = {
    "Authorization": "sk-tune-VphHayIWwMO9sbqJYAlm3pvjeaXRYIgcelb",
    "Content-Type": "application/json",
}
resume = textwrap.dedent("\n Student Resume Data: " + """
PRANJAYKUMAR
 pranjay.kumar@stern.nyu.edu | New York, NY | (908) 380-6875
 EDUCATION
 NewYork University, Leonard N. Stern School of Business
 BS in Business Administration (Finance & Accounting) / MS in Accounting, Minor in Creative Writing
 ▪ GPA:3.94/4.00 (Major GPA: 4.0) | Honors: Dean’s List (4x) | ACT: 35/36
 NewYork, NY
 Sep 2022- May 2026
 ▪ Extracurriculars: Venture Society (Tech Writer), Accounting Society (Outreach Dir.), Slam Poetry (Performer)
 ▪ Relevant coursework: Business & Society, Statistics, Organizational Communications, The Financial Service Industry
 PROFESSIONALEXPERIENCE
 Citadel Securities
 NewYork, NY
 Incoming Fall Operations Intern
 Latam Links (B2B Consulting Startup, Pre-Revenue Stage)
 Head of Business Development
 Expected Sep 2024
 Mexico City, MX
 Jan 2024- Present
 ▪ Driving digital marketing initiatives to link Mexican apparel manufacturers with domestic clothing retailers and distributors
 ▪ Developing CRM-based sales pipeline that reached 10k+ leads and utilized large language models and proprietary scrapers
 ▪ Overseeing a 5-person business development team, increasing productivity by 50% using RPA, LLMs, and CRM systems
 Wiss & Company (Top 100 Accounting Firm)
 CFOAdvisory Intern
 Florham Park, NJ
 Jun 2024- Aug 2024
 ▪ Enhanced financial operations with 200+ financial reconciliations for $100M+ clients in Real Estate, CPG & Engineering
 ▪ Developed a resume review tool in collaboration with the tech advisory team using LLMs, cutting review time by 90%
 ▪ Created a Power BI financial dashboard utilizing Power Query and Power Pivot to enhance the decision-making process
 Pulsar (E-Commerce Business Broker)
 Business Analyst Intern
 NewYork, NY
 Jan 2023- Sep 2023
 ▪ Utilized NLP to analyze 40k+ fintech startups, differentiating offerings, leading to a 50% increase in signed mandates
 ▪ LedM&Aanalyst program, onboarding ten individuals to enhance post-transaction value through diverse perspectives
 ▪ Collaborated closely on CIM & financial model development for five e-commerce clients with EBITDA between $1-5M
 NewYork City Office of the Comptroller (Pension Fund)
 Asset Management Operations Intern
 NewYork, NY
 Jun 2023- Aug 2023
 ▪ Devised AI operation plan with Bureau of Asset Management executives, targeting 50% potential productivity increases
 ▪ Directed audits on 2k+ individual accounts, ensuring 99.8% accuracy in public data for investments valued at $255B
 ▪ Performed due diligence for Private Equity Funds (AUM $22B), pinpointing disparities and initiating resolutions with GPs
 LEADERSHIPANDEXTRACURRICULARACTIVITIES
 Stern School of Business, World Well-Being Project (LLM Research)
 Research Assistant
 NewYork, NY
 Jun 2023- Present
 ▪ Analyzing 4 TB of conversational data using ML to create a custom dataset of 10M+ conversations for LLM fine-tuning
 ▪ Engineering versatile article web scraper with a 90% success rate, efficiently capturing 500k+ articles across 3,000+ sites
 ▪ Optimized RoBERTa, LLaMA, and OpenAI LLMs for empathy scoring on a curated dataset, targeting a 0.8 correlation
 Stern School of Business, Turing Gardens (ML Research)
 Research Assistant
 NewYork, NY
 Jan 2023- Jun 2023
 ▪ Workedwith team of 5 individuals to create & optimize a secure, efficient article sharing platform for STEM professionals
 ▪ Developed a Q-learning greedy recommendation algorithm, achieving a 75% increase in recommendation subject diversity
 ▪ Improved accuracy and personalization by 60%, incorporating user history and reading time in recommendation algorithm
 SKILLS &INTERESTS
 Skills: Powerpoint, Excel, SQL, Java, Python, C++, Tableau, PowerBi, Power Query, Power Automate, Quickbooks, CapIQ
 Interests: Flash Fiction, Slam Poetry, Weightlifting, Financial Literacy Education, Empathy-Driven Chatbots, Running
 Certifications: Alteryx Designer Core
""")

# Initialize linkedin_profile_ids as a list of strings
linkedin_profile = input("Enter the LinkedIn profile ID of the professional: ")
linkedin_profiles = pd.read_csv(r"linkedin_data.csv")
user_content = linkedin_profiles[linkedin_profiles['profile_id'] == linkedin_profile].to_dict(orient='records')[0]
user_content = {
    "first_name": user_content.get("first_name"),
    "last_name": user_content.get("last_name"),
    "sub_title": user_content.get("sub_title"),
    "location": user_content.get("location"),
    "industry": user_content.get("industry"),
    "current_company_name": user_content.get("current_company_name"),
    "current_company_position": user_content.get("current_company_position"),
    "skills": user_content.get("skills"),
    "education": user_content.get("education"),
    "position_groups": user_content.get("position_groups")}

data = {
  "temperature": 0.9,
    "messages":  [
        {
            "role": "system",
            "content": "You are specializing in professional communication, tasked with composing a networking-focused cold email from a student, Pranjay. Given the data from the professional and the student's resume, your mission is to land a coffee chat. Make the networking email personalized to the receiver’s work experience, preferences, and interests provided by the data. The text must sound authentic and human. Keep the email short, 100 to 200 words is ideal."
        },
        {
            "role": "user",
            "content": "Professional LinkedIn Data: " + json.dumps(user_content, indent=4) + "\n\n" + resume
        }
    ],
    "model": "Pranjay/Email-v2-model-jf2brymr",
    "stream": stream,
    "frequency_penalty":  0.2,
    "max_tokens": 900,
}
response = requests.post(url, headers=headers, json=data)
if stream:
    for line in response.iter_lines():
        if line:
            l = line[6:]
            if l != b'[DONE]':
              print(json.loads(l))
else:
  print(response.json())