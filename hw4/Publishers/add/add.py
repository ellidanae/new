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
    publisher = request.form
    name = publisher['name']
    address = publisher['address']
    phone = publisher['phone']
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO publishers(Name, Address, Phone) VALUES(%s, %s, %s)",(name,address, phone))
    mysql.get_db().commit()
    return redirect('/publishers')

@app.route('/publishers')
def publishers():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM publishers")
    # html = ''    
    if response > 0:
        publishers = cursor.fetchall()
        return render_template('publishers.html', list=publishers)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)

    # http://localhost:3000