from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # needed for flash messages

# MongoDB Setup
client = MongoClient(os.getenv("MONGO_URI"))
db = client['flaskAppDB']
collection = db['formData']

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            data = {
                'name': request.form['name'],
                'email': request.form['email']
            }
            collection.insert_one(data)
            return redirect(url_for('success'))
        except Exception as e:
            flash(f"Error occurred: {str(e)}")
            return render_template('form.html')
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')


@app.route("/submittodoitem", methods=['POST'])
def submittodoitem():
    

    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    collection.insert_one({'itemName': item_name, 'itemDescription': item_description})

    return ("Todo item submitted successfully!")

if __name__ == '__main__':
    app.run(debug=True)
