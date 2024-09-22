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
    "Authorization": "sk-tune-FJdgWoOuqe9o7GjRvzOPq0q1G9QDm87K1FO",
    "Content-Type": "application/json",
}
resume = input("Enter the resume of the student: ")
grade = input("Enter the grade of the student: ")
school = input("Enter the school of the student: ")
area_of_interest = input("Enter the area of interest of the student: ")
first_name = input("Enter the first name of the student: ")
last_name = input("Enter the last name of the student: ")

# Initialize linkedin_profile_ids as a list of strings
linkedin_profile = input("Enter the LinkedIn profile ID of the professional: ")
linkedin_profiles = pd.read_csv(r"linkedin_data.csv")
filtered_profiles = linkedin_profiles[linkedin_profiles['profile_id'] == linkedin_profile].to_dict(orient='records')
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
    print(f"No profile found for LinkedIn ID: {linkedin_profile}")

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
    for line in response.iter_lines():
        if line:
            l = line[6:]
            if l != b'[DONE]':
              print(json.loads(l))
else:
  print(response.json())
