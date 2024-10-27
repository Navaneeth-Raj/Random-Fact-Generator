<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# Life's Most Useless Facts - A Random Fact Generator 🎯


## Basic Details
### Team Name: INNOVATEX


### Team Members
- Team Lead: Sidharth P Krishnan - SCMS School of Engineering and Technology
- Member 2: Navaneeth Raj R - SCMS School of Engineering and Technology
- Member 3: Pranav Varma - SCMS School of Engineering and Technology

### Project Description
"Life’s Most Useless Facts - A Random Fact Generator" is here to fill your day with the most irrelevant, mind-boggling trivia you’ll never actually need! With just a click, discover facts so random they’ll make you wonder, “Why do I know this now?”

### The Problem (that doesn't exist)
"Life's Most Useless Facts" solves the pressing issue of not having random, pointless trivia to brighten up dull moments or start the most bizarre conversations. It's the ultimate solution for anyone who needs a quick mental break, a quirky icebreaker, or just a laugh from the sheer absurdity of knowledge we don’t need but love to know!

### The Solution (that nobody asked for)
The solution is built using a Python backend to fetch random, quirky facts from an external API, then delivers them to a playful HTML/CSS frontend with just a button click. Facts are stored in a MySQL database, where users can rate the "uselessness" of each fact, letting the app highlight the most absurd facts for future enjoyment!

## Technical Details
### Technologies/Components Used
For Software:
- Languages Used : HTML/CSS, Python, MySQL
- Frameworks Used : Flask
- Libraries Used : Flask, requests

For Hardware:
- Device : Any modern device that can support a web browser.
- Memory : Recommended RAM of 2GB
- Storage : Free space of 2MB

### Implementation
The Fact Generator uses Flask to handle routes and API requests. Facts are fetched from an external API (https://uselessfacts.jsph.pl/random.json) and displayed in the browser. Users can view a weekly fact and request additional random facts with a button click.
# Installation
On Command Prompt :  
git clone https://github.com/Navaneeth-Raj/Random-Fact-Generator  
pip install requests  
pip install Flask  

# Run
On command prompt:  
cd Random-Fact-Generator  
flask run  

### Project Documentation
For Software:https://github.com/Navaneeth-Raj/Random-Fact-Generator/blob/main/Useless%20Facts%20Generator%20Project.docx

# Screenshots (Add at least 3)
Home page with the random generated fact.
<img width="1280" alt="about" src="https://github.com/Navaneeth-Raj/Navaneeth-Raj/raw/main/Home.png">


Highlights page with the generated fact for the week.
<img width="1280" alt="about" src="https://github.com/Navaneeth-Raj/Navaneeth-Raj/raw/main/Highlight.png">


About page shows the details of the project and team members.
<img width="1280" alt="about" src="https://github.com/Navaneeth-Raj/Navaneeth-Raj/raw/main/About.png">

# Diagrams
<img width="1280" alt="about" src="https://github.com/Navaneeth-Raj/Random-Fact-Generator/raw/main/static/images/WorkFlow.jpeg">
The Random Fact Generator project workflow starts with the user clicking a button in their browser (HTML & CSS), which triggers JavaScript to request a fact from the Flask backend. Flask, running on Python, either fetches the fact from an external API or retrieves it from a database (if used). The fact is then sent back and displayed on the browser, completing the interaction.

### Project Demo
# Video
Video URL : https://github.com/Navaneeth-Raj/Navaneeth-Raj/blob/main/Video%20Demo.mp4
The Video demonstrates the three pages of the Fact Generator Project. Home page features the button which on click, produces the Fact. Highlights page shows the Fact for the Week and About page shows some details of the project and team members.

## Team Contributions
- Sidharth P Krishnan : Development on Home, Highlights Pages and Javascript Functions.
- Pranav Varma : Creative Lead, Development on About Page.
- Navaneeth Raj R : Development on Flask Backend.

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)
