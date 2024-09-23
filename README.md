# 🎉 CoffeeStarter: Your Personal Networking Agent 🚀

Team:
- Sutharsika Kumar, University of North Carolina - Chapel Hill
- Pranjay Kumar, New York University Stern School of Business
- Tanush Changani, City University of Hong Kong
- Aarav Jindal, PRISM Princeton University

Welcome to **CoffeeStarter**, a cutting-edge tool designed to revolutionize personal networking by connecting you with alumni from your school's network effortlessly. Perfect for hackathons and beyond, CoffeeStarter blends advanced technology with user-friendly features to help you build meaningful professional relationships.

---

## 🌟 Inspiration

In a world where connections matter more than ever, we envisioned a tool that bridges the gap between ambition and opportunity. **CoffeeStarter** was born out of the desire to empower individuals to effortlessly connect with alumni within their school's network, fostering meaningful relationships that propel careers forward.

---

## 🛠️ What It Does

CoffeeStarter leverages the power of a fine-tuned **LLaMA** model to craft **personalized emails** tailored to each alumnus in your school's network. Here's how it transforms your networking experience:

- **📧 Personalized Outreach:** Generates authentic, customized emails using your resume to highlight relevant experiences and interests.
- **🔍 Smart Alumnus Matching:** Identifies and connects you with alumni that align with your professional preferences and career goals.
- **🔗 Seamless Integration:** Utilizes your existing data to ensure every interaction feels genuine and impactful.

---

## 🏗️ How We Built It

Our robust technology stack ensures reliability and scalability:

- **🗄️ Database:** Powered by **SQLite** for flexible and efficient data management.
- **🐍 Machine Learning:** Developed using **Python** to handle complex ML tasks with precision.
- **⚙️ Fine-Tuning:** Employed **Tune** for meticulous model fine-tuning, ensuring optimal performance and personalization.

---

## ⚔️ Challenges We Faced

Building CoffeeStarter wasn't without its hurdles:

- **🔒 SQLite Integration:** Navigating the complexities of SQLite required innovative solutions.
- **🚧 Firewall Obstacles:** Overcoming persistent firewall issues to maintain seamless connectivity.
- **📉 Model Overfitting:** Balancing the model to avoid overfitting while ensuring high personalization.
- **🌐 Diverse Dataset Creation:** Ensuring a rich and varied dataset to support effective networking outcomes.
- **API Integration:** Working with various API's to get as diverse a dataset and functionality as possible.

---

## 🏆 Accomplishments We're Proud Of

- **🌈 Diverse Dataset Development:** Successfully created a comprehensive and diverse dataset that enhances the accuracy and effectiveness of our networking tool.
- Authentic messages that reflect user writing styles which contributes to personalization.

---

## 📚 What We Learned

The journey taught us invaluable lessons:

- **🤝 The Complexity of Networking:** Understanding that building meaningful connections is inherently challenging.
- **🔍 Model Fine-Tuning Nuances:** Mastering the delicate balance between personalization and generalization in our models.
- **💬 Authenticity in Automation:** Ensuring our automated emails resonate as authentic and genuine, without echoing our training data.

---

## 🔮 What's Next for CoffeeStarter

We're just getting started! Future developments include:

- **🔗 Enhanced Integrations:** Expanding data integrations to provide even more personalized networking experiences and actionable recommendations for enhancing networking effectiveness.
- **🧠 Advanced Fine-Tuned Models:** Developing additional models tailored to specific networking needs and industries.
- **🤖 Smart Choosing Algorithms:** Implementing intelligent algorithms to optimize alumnus matching and connection strategies.

---

## 📂 Submission Details for PennApps XXV

### 📝 Prompt

You are specializing in professional communication, tasked with composing a networking-focused cold email from an input `{student, alumni, professional}`, name `{your_name}`. Given the data from the receiver `{student, alumni, professional}`, your mission is to land a coffee chat. Make the networking text `{email, message}` personalized to the receiver’s work experience, preferences, and interests provided by the data. The text must sound authentic and human. Keep the text `{email, message}` short, 100 to 200 words is ideal.

### 📄 Version Including Resume

You are specializing in professional communication, tasked with composing a networking-focused cold email from an input `{student, alumni, professional}`, name `{your_name}`. The student's resume is provided as an upload `{resume_upload}`. Given the data from the receiver `{student, alumni, professional}`, your mission is to land a coffee chat. Use the information from the given resume of the sender and their interests from `{website_survey}` and information of the receiver to make this message personalized to the intersection of both parties. Talk specifically about experiences that `{student, alumni, professional}` would find interesting about the receiver `{student, alumni, professional}`. Compare the resume and other input `{information}` to find commonalities and make a positive impression. Make the networking text `{email, message}` personalized to the receiver’s work experience, preferences, and interests provided by the data. The text must sound authentic and human. Keep the text `{email, message}` short, 100 to 200 words is ideal. Once completed with the email, create a **1 - 10 score** with **1** being a very generic email and **10** being a very personalized email. Write this score at the bottom of the email.



## 🧑‍💻 Technologies Used

- **Frameworks & Libraries:**
  - **Python:** For backend development and machine learning tasks.
  - **SQLite:** As our primary database for managing user data.
  - **Tune:** Utilized for fine-tuning our LLaMA3 model.

- **External/Open Source Resources:**
  - **LLaMA Model:** Leveraged for generating personalized emails.
  - **Various Python Libraries:** Including Pandas for data processing and model training.
 
## Notes on running our application
node emailMiddle.js
node UserDataTransfer.js
node saveDeets.js
node uniSave.js
node savePDF.js

Run page1.html

