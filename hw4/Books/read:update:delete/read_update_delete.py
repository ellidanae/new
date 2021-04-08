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
    return redirect('/read')

@app.route('/delete')
def delete():
    id = request.args.get('id')
    cur = mysql.get_db().cursor()
    cur.execute("DELETE FROM books WHERE bookID=%s",id)
    mysql.get_db().commit()
    return redirect('/read')

@app.route('/book')
def book():
    book = {}
    book['id'] = request.args.get('id')
    book['prise'] = request.args.get('prise')   
    book['title'] = request.args.get('title')   
    book['date'] = request.args.get('date')   
    book['genreID'] = request.args.get('genreID')    
    book['publisherID'] = request.args.get('publisherID')
    return render_template('book.html', book=book)

@app.route('/update', methods=['POST'])
def add():
    book = request.form
    id = book['id']
    prise = book['Prise']
    title = book['Title']
    date = book['Date']
    genreID = book['GenreID']
    publisherID = book['PublisherID']
    cur = mysql.get_db().cursor()
    # here question:
    #why do we have first the name an dthen the id?
    #what happens exactly with this command
    cur.execute("UPDATE books SET prise=%s WHERE bookID=%s",(prise, id))
    cur.execute("UPDATE books SET title=%s WHERE bookID=%s",(title, id))
    cur.execute("UPDATE books SET date=%s WHERE bookID=%s",(date, id))
    cur.execute("UPDATE books SET genreID=%s WHERE bookID=%s",(genreID, id))
    cur.execute("UPDATE books SET publisherID=%s WHERE bookID=%s",(publisherID, id))

    # cur.execute ("UPDATE books SET firstname=%s, lastname=%s WHERE bookID=%s " % (firstname, lastname, id))


    mysql.get_db().commit()
    return redirect('/read')

@app.route('/read')
def read():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM books")
    # html = ''    
    if response > 0:
        books = cursor.fetchall()
        return render_template('read.html', list=books)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)

    