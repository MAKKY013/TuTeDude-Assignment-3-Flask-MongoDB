# TuTeDude-Assignment-3-Flask-MongoDB
Assignment 3 combining Flask API and MongoDB Atlas form submission for TuTeDude DevOps course
TuTeDude Assignment 3 – Flask + MongoDB Atlas
Project Overview
This project demonstrates integration of a Flask web application with MongoDB Atlas.
It includes:

A form (form.html) to collect user details (name and email).

A backend (app.py) that inserts submissions into MongoDB Atlas.

A success page (success.html) confirming data submission.

(Optional) A view page (view.html) to list all submissions directly in Flask.

Repository Structure
Code
├── app.py
├── templates/
│   ├── form.html
│   ├── success.html
│   └── view.html   (optional)
└── README.md

Setup Instructions
Clone the repository

bash
git clone https://github.com/MAKKY013/TuTeDude-Assignment-3-Flask-MongoDB.git
cd TuTeDude-Assignment-3-Flask-MongoDB
Install dependencies

bash
pip install flask pymongo
Configure MongoDB Atlas

Ensure your Atlas cluster is running.

Update the connection string in app.py with your credentials.

Run the Flask app

bash
python app.py
Access the app

Open http://127.0.0.1:5000/ in your browser.

Submit test data via the form.

Check Atlas → assignment3 → submissions → Browse Collections.

Screenshots
Form Page – User enters name and email.

Success Page – Confirmation message after submission.

Atlas Collection – Shows stored documents with _id, name, and email.

Commit History (for tutor reference)
Add app.py with Flask-MongoDB integration

Add form.html template for data entry

Add success.html template for confirmation

Add view.html template to list submissions (optional)

Add README.md with setup instructions

Notes
Use http:// not https:// when running locally.

The /submit route only accepts POST requests (via the form).

The /view route is optional but useful for listing submissions directly in Flask.
