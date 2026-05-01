from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://makmakky013_db_user:77f9Tz0uygG5iuf2@cluster0.0wu8hlk.mongodb.net/?appName=Cluster0")
db = client["assignment3"]
collection = db["submissions"]

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    collection.insert_one({"name": name, "email": email})
    return render_template('success.html')

@app.route('/view')
def view():
    submissions = list(collection.find())
    return render_template('view.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
