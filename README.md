# The Bitcoin Test App

#### Video Demo: https://youtu.be/Htj2o58bnuw

#### Description:
The Bitcoin Test App is a web application designed to help users learn about Bitcoin and test their understanding through interactive quizzes and auto-generated certificates. The app features a Learn section where users can read beginner-friendly yet comprehensive lessons on Bitcoin’s fundamentals—such as what Bitcoin is, how it works, mining, and economic implications. At the end of each lesson, users complete a short quiz containing both multiple-choice and free-text questions to reinforce their understanding.

Once they feel prepared, users can proceed to the Test section, where they choose between two levels: the regular Bitcoin Test and the Advanced Bitcoin Test. These tests draw questions at random from a database, ensuring that each session is unique. After completion, the app immediately displays the user’s score. If the user passes, they are prompted to enter their name, which will appear on a downloadable PDF certificate. This certificate includes their name, test score, and date of completion, formatted and generated automatically using ReportLab.

The design of the application emphasizes simplicity and clarity. The UI includes smooth transitions and animations to provide a polished user experience across devices. Anti-cheating measures are in place: right-clicking and copying are disabled via JavaScript, and Flask sessions are used to ensure that users cannot retake the same test or skip ahead to the certificate without completing the test.

From a technical standpoint, the app is built using Flask (a Python web framework), with Jinja2 for templating and SQLite for persistent storage of quiz data. The app uses standard HTML, CSS, and a bit of JavaScript for interactivity. It was deployed using GitHub and Render, making it accessible to anyone who knows the app’s URL. The structure of the code is clean and modular, separating templates, static files, and Python logic for maintainability.

This project reflects my interest in web development and crypto-related technologies. It also demonstrates my ability to build and deploy a full-stack application from scratch, including designing the UI/UX, handling data flow, managing user sessions, and integrating third-party libraries like ReportLab for PDF generation. It was both a challenging and rewarding experience.

# The structure of this function was inspired by suggestions from ChatGPT.

### File Overview

- `app.py`
  Main Flask application. Handles routing, user sessions, test logic, result calculation, and certificate generation.

- `templates/`
  Contains all Jinja2 HTML templates, such as `index.html`, `learn.html`, `test.html`, `result.html`, and `certificate.html`.

- `static/`
  Includes CSS stylesheets (`styles.css`) and JavaScript (`script.js`) for UI design and interactivity.

- `questions.db`
  SQLite database storing quiz questions for both regular and advanced Bitcoin tests.

- `project.zip`
  Contains all source code and assets for the application, except for `README.md`.

- `README.md`
  This documentation file describing the project, including its structure, usage, and purpose.
