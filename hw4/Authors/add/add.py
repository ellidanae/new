# imports
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

# web application
app = Flask(__name__)

# connect to db
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'e4l7l9i7!'
app.config['MYSQL_DATABASE_DB'] = 'book_industry'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/add', methods=['POST'])
def add():
    # Fetch form data
    author = request.form
    firstname = author['firstname']
    lastname = author['lastname']
    address = author['address']
    phone = author['phone']
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO authors(FirstName, LastName, Address, Phone) VALUES(%s, %s, %s, %s)",(firstname,lastname,address, phone))
    mysql.get_db().commit()
    return redirect('/authors')

@app.route('/authors')
def authors():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM authors")
    # html = ''    
    if response > 0:
        authors = cursor.fetchall()
        return render_template('authors.html', list=authors)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)

    # http://localhost:3000