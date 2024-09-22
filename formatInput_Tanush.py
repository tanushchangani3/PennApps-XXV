import json
import textwrap

resume = resume_data = textwrap.dedent("\n Student Resume Data: " + """
1

TANUSH DEEPAK CHANGANI tanushchangani3@gmail.com • +852 63378509 • linkedin.com/in/tchangani/ • github.com/tanushchangani3 
 
EDUCATION 
City University of Hong Kong | Hong Kong SAR             Sep 2021 - June 2025 
Bachelor of Engineering in Computer and Data Engineering      
Relevant Coursework: Intro to Computer Programming (Python), Computer Programming (C++), Data Structures & Algorithms (Worked with C++), 
Modelling Techniques (Worked with R), Intro to Finance, Java Programming & Applications, Data Engineering & Learning Systems 
Activities & Societies: Model United Nations, CityHack, Indian Student’s Association, CityU Google Student Developer Club, EE Student Representative 
Drexel University | Philadelphia, Pennsylvania, United States               Sep 2023 - Dec 2023 
Academic Semester Exchange, Computer Science                   
Relevant Coursework: Systems Architecture (Worked with Assembly), Database Systems (Worked with SQL), Human-Computer Interaction 
Activities & Societies: Drexel Finance and Investment Group, Drexel South Asian Student Association Big-Little 
YMCA of Hong Kong Christian College | Hong Kong SAR                            Sep 2015 - June 2021 
GCE Advanced Level and International GCSE                                                 
A Levels in Physics, Mathematics and Religious Studies 
Leadership: Student Council President, Head Organiser of Charity Fashion Show, Student Ambassador Team Leader, JA Company Program 
 
WORK EXPERIENCE 
Platform & DevOps Summer Intern - Asia Enterprise Technology | Manulife | Hong Kong SAR                                       June 2024 - Aug 2024         
• Managed end-to-end development and deployment processes for a Python framework application through the SDLC for development teams across 
Asia to support micro services in Kubernetes clusters in East Asia/Emerging Markets, deploying through a Jenkins CICD pipeline. 
• Designed and executed a robust filtering system within the Python configuration management framework, resulting in a 92% reduction in irrelevant 
data retrieved from the configuration server. 
• Worked with cross-functional teams to implement encryption algorithms to develop a secure encryption and decryption tool using Google Tink, 
resulting in a 95% decrease in data breach incidents within the config server data files. 
• Packaged Python framework application into Docker image, improving scalability for remote deployment and enhancing product usability by 80%. 
Technology Summer Intern | Preface | Hong Kong SAR             June 2023 - Aug 2023         
• Conducted analysis and migrated notes management system from legacy portal to new web application using REST APIs, Ruby on Rails (backend) 
and React.js/Next.js (frontend) reducing loading times and enhanced UX with 15% increase in overall system responsiveness and accessibility. 
• Implemented an efficient machine learning model using Python with my team to automatically predict tags for specific texts in a dataset, improving 
model performance and resulting in 90% reduction in manual tag generation time. 
• Spearheaded idea for a comprehensive analytics dashboard, creating UX/UI designs to track and visualise client learning progress. Incorporated 
gamification concepts to communicate data insights, resulting in a predicted 40% improvement in client engagement and retention rates. 
Digital Marketing Intern | Xccelerate | Hong Kong SAR               July 2020 - Aug 2020          
• Partnered with the Head of Data Science on creating educational videos on Data Visualisation, Business Intelligence (Tableau) & Machine Learning 
for up skilling HSBC employees. 
• Utilised design skills to tailor marketing strategies to effectively communicate key technological messages of tech startups from Xccelerate. 
 
PROJECTS & OTHER EXPERIENCES 
GBA Fintech Talent Initiative (Fellowship) | Bloomberg LP | Hong Kong SAR                      Feb 2023 - March 2023 
• Analysed GM US Equity using Bloomberg Terminal to develop buy-side investment ideas presented to the Data Analytics team, resulting in a 10% 
portfolio return increase through extensive research and collaboration. 
• Visited trading floors and workshops at Bank of America and J.P. Morgan 
• Selected as one of three students the South China Morning Post interviewed on the GBA Fintech space and its potential. Leveraged research and 
analytical skills to provide valuable insights, resulting in a well-received and informative article. (http://bit.ly/3P3S9kR) 
Co-Founder | Spat!al | Hong Kong SAR                 Jan 2022 - Aug 2023 
• Developed a software that aims to elevate virtual learning experience allowing students and professors to interact with each other effectively using 
OpenCV models for anonymous facial tracking for attention-span class analytics and AudioContext API for spatial audio technology. 
• Received an offer of HK$100,000 seed funding from CityU HKTech 300 for winning the City University of Hong Kong Annual Hackathon 
(CityHack) 2022 competing with over 50 teams. Shortlisted to the finalist stage at the Microsoft sponsored Hong Kong Techathon 2023. 
Team Lead | Smart Solar Panel Powered Traffic Light System | Hong Kong SAR          Jan 2024 - April 2024 
• Utilising Python and Arduino Programming to program the Arduino board’s temperature, image and pressure sensors and OLED display powered by a 
solar panel to operate a smart adaptive traffic light system.  
 
SKILLS 
Technical: Python, C++, Java, R Programming, SQL, MIPS, Node.js, React.js, Jira, Jenkins, Kubernetes, DevOps, CI/CD, Ruby on Rails, REST APIs, 
Git, Machine Learning, UXUI Design (Adobe XD/Figma), Bloomberg Terminal, Final Cut Pro X, Microsoft Suite, Agile Methodologies 
Language: English (Native, IELTS: 8.0/9.0), Mandarin (Limited Working Proficiency), Hindi (Limited Working Proficiency) 
         AWARDS A ND ACHIEVEMENTS 
• Morgan Stanley Tech X Challenge 2023 2nd Runner Up 
• CityHack 2022 Awards: Champion Award and Most Creative Award 
• PolyHack 2022 Honourable Mention Award 
• Peter Ho Scholarship for Student Council President """)
# Load the JSON file
with open('tech_emails.json', 'r', encoding='utf-8') as f:
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
                    "from a student, Tanush. Given the data from the professional and the student's resume, "
                    "your mission is to land a coffee chat. Personal Information about the student: Senior at City University of Hong Kong  Interested in Tech. Make the networking email personalized to the receiver’s work experience, "
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
with open('formatted_output_tanush.json', 'w', encoding='utf-8') as outfile:
    json.dump(formatted_data, outfile, indent=4, ensure_ascii=False)

print("Data successfully formatted and saved to 'formatted_output.json'")
