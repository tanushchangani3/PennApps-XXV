import json
import textwrap
import csv
import pandas as pd
import json
import requests
# Replace resume data as needed
def generate_networking_email(resume, grade, school, area_of_interest, first_name, last_name, linkedin_profile_id):
    stream = False
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": "sk-tune-FJdgWoOuqe9o7GjRvzOPq0q1G9QDm87K1FO",
        "Content-Type": "application/json",
    }

    linkedin_profiles = pd.read_csv(r"linkedin_data.csv")
    filtered_profiles = linkedin_profiles[linkedin_profiles['profile_id'] == linkedin_profile_id].to_dict(orient='records')
    user_content = {}
    if len(filtered_profiles) > 0:
        user_content = filtered_profiles[0]
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
            "position_groups": user_content.get("position_groups")
        }
    else:
        print(f"No profile found for LinkedIn ID: {linkedin_profile_id}")
        return None

    data = {
      "temperature": 0.9,
        "messages":  [
            {
                "role": "system",
                "content": f"You are specializing in professional communication, tasked with composing a networking-focused cold email from a student, {first_name} {last_name}. Given the data from the professional and the student's resume, your mission is to land a coffee chat. Personal Information about the student: {grade} at {school} Interested in {area_of_interest}. Make the networking email personalized to the receiver’s work experience, preferences, and interests provided by the data. The text must sound authentic and human. Keep the email short, 100 to 200 words is ideal."
            },
            {
                "role": "user",
                "content": "Professional LinkedIn Data: " + json.dumps(user_content, indent=4) + "\nStudent Resume: " + resume
            }
        ],
        "model": "sutharsikakumar/NYU-Stern-model-zrndbtz8",
        "stream": stream,
        "frequency_penalty":  0.2,
        "max_tokens": 900,
    }
    response = requests.post(url, headers=headers, json=data)
    if stream:
        email_text = ""
        for line in response.iter_lines():
            if line:
                l = line[6:]
                if l != b'[DONE]':
                    email_text += json.loads(l)
        return email_text
    else:
        return response.json()['choices'][0]['message']['content']

# Example usage
resume = """
1

Sutharsika Kumar
sutharsika.kumar07@gmail.com
Mobile: +1 980-358-1146
LinkedIn: https://tinyurl.com/2pys7skm
Website: N/A
Home Address:
119 Glade Valley Avenue,
Mooresville, NC, 28117
Education
University of North Carolina at Chapel-Hill — Chapel-Hill, NC May 2028
B.S. Computer Science & Mathematics
North Carolina School of Science and Mathematics — Durham, NC May 2024
High School Diploma
Relevant Experience
The Wang Lab - Duke University July 2024 – Present
● Integrated LLM with ML for unsupervised learning; end goal of automating an optical microscope for detection of
monolayer crystal growth in integrated circuit applications
● Collaborated with my lab members, postdocs, and PI to produce significant results
ClimateCardinals August 2023 – June 2024
● Director for Artificial Intelligence
● Created applications using artificial intelligence for translation service provided by ClimateCardinals
● Managed communications among the team; developed easy access to resources for new members
Research in Physics October 2022 – December 2023
● Developed a novel protocol for Quantum ESPRESSO modeling of perovskite crystals
● Published a paper on the effectiveness of machine learning in detecting coal ash and other contaminants
using publicly available mineral data; A geospatial investigation
Environmental Initiatives July 2021 – Present
● Designed an app that gamified the idea of trash collection for the purpose of promoting environmental pollution
awareness
● Built a partnership with Sustain Charlotte through outreach initiatives and understanding their agenda for
environmental improvement in the Charlotte area.
Skills
● Programming in Python, Java, HTML, CSS, R
● Courses: Multivariable Calculus, Numerical Analysis, Graph Theory, Combinators & Game Theory, AP Computer
Science A, Generative AI, Prompt-Engineering
Awards
● 1st Place North Carolina Student Academy of Science
● 3rd Place NCSEF ISEF Affiliated Fair 2024
● 2x NCSEF Finalist
● Conrad Challenge National Hackathon 2nd Place Winner 2021
● Envirothon State 4th Place 2023
● 3rd Place State INSPIRE Award FIRST Technology Challenge, Team: FTC 22377 SigmaCorns
"""
grade = "Sophomore"
school = "Harvard"
area_of_interest = "Data Science"
first_name = "John"
last_name = "Doe"
linkedin_profile_id = "lei-jiang-836109b9"


form_data = []

with open('formData.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Strip the newline character and add to the array
        form_data.append(line.strip())
first_name = form_data[0]
last_name = form_data[1]

lines_array = []

# Open the file and read the lines
with open('emailAddress.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Strip the newline character and add to the array
        lines_array.append(line.strip())
linkedin_profile_id = lines_array[1]
print("linkedin: "+linkedin_profile_id)

email_text = generate_networking_email(resume, grade, school, area_of_interest, first_name, last_name, linkedin_profile_id)
print("making file")
print(email_text)

with open('email.txt', 'w') as text_file:
            text_file.write(email_text)

print("made file")
