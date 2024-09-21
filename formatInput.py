import json

# Load the JSON file
with open('trainingData.json', 'r') as f:
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
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are specializing in professional communication, tasked with composing a networking-focused cold email "
                    "from an input {student, alumni, professional}, name {your_name}. Given the data from the receiver {student, alumni, professional}, "
                    "your mission is to land a coffee chat. Make the networking text {email, message} personalized to the receiver’s work experience, "
                    "preferences, and interests provided by the data. The text must sound authentic and human. Keep the text {email, message} short, "
                    "100 to 200 words is ideal."
                )
            },
            {
                "role": "user",
                "content": json.dumps(user_content, indent=4)  # Combine category info into a single string
            },
            {
                "role": "assistant",
                "content": profile.get("email_text", "")  # Add the email text content here
            }
        ]
    }
    
    # Append to the formatted data list
    formatted_data.append(formatted_message)

# Save the formatted data to a new JSON file
with open('formatted_output.json', 'w') as outfile:
    json.dump(formatted_data, outfile, indent=4)

print("Data successfully formatted and saved to 'formatted_output.json'")
