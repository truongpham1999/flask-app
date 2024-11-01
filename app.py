from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_mysqldb import MySQL

# create the Flask application
app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskdb'

mysql = MySQL(app)

# Set the secret key for session management
app.secret_key = '90328dksalowki1282'  # Replace with a strong random key

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/table_list')
def table_list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_document")
    documents = cur.fetchall()
    cur.close()

    return render_template('table.html', documents=documents)

@app.route('/add_document', methods=['GET', 'POST'])
def add_document():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_document (title, description, status) VALUES (%s, %s, %s)",
                    (title, description, status))
        mysql.connection.commit()
        cur.close()

        flash('Document added successfully!')
        return redirect(url_for('table_list'))

    return render_template('add_document.html')  # Create a separate HTML form for adding a document

@app.route('/create-database')
def create_database():
    cur = mysql.connection.cursor()
    cur.execute("CREATE TABLE tbl_document (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), description VARCHAR(255), status INT)")
    mysql.connection.commit()
    cur.close()
    return 'Database created'


if __name__ == '__main__':
    app.run()
