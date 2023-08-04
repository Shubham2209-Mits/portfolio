from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder='D:/shubham_portfolio')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
   

    # Connect to the SQLite database
    conn = sqlite3.connect('mydatabase.sqlite')
    cursor = conn.cursor()

    # Insert data into the database
    cursor.execute('INSERT INTO form_data (name, email ,message) VALUES (?, ?, ?)', (name, email, message ))
    conn.commit()

    # Close the database connection
    conn.close()

    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
