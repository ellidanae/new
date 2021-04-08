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
    book = request.form
    prise = book['prise']
    title = book['title']
    date = book['date']
    genreID = book['genreID']
    publisherID = book['publisherID']

    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO books(Prise, Title, Date, GenreID, PublisherID) VALUES(%s, %s, %s,%s, %s)",(prise,title,date,genreID, publisherID))

    mysql.get_db().commit()
    return redirect('/books')

@app.route('/books')
def books():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM books")
    # html = ''    
    if response > 0:
        books = cursor.fetchall()
        return render_template('books.html', list=books)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)

    # http://localhost:3000