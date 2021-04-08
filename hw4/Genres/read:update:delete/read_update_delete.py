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
    cur.execute("DELETE FROM genres WHERE genreID=%s",id)
    mysql.get_db().commit()
    return redirect('/read')

@app.route('/genre')
def genre():
    genre = {}
    genre['id'] = request.args.get('id')
    genre['name'] = request.args.get('name')  
    return render_template('genre.html', genre=genre)

@app.route('/update', methods=['POST'])
def add():
    genre = request.form
    id = genre['id']
    name = genre['Name']
    cur = mysql.get_db().cursor()
    # here question:
    #why do we have first the name an dthen the id?
    #what happens exactly with this command
    cur.execute("UPDATE genres SET name=%s WHERE genreID=%s",(name, id))


    # cur.execute ("UPDATE genres SET firstname=%s, lastname=%s WHERE genreID=%s " % (firstname, lastname, id))


    mysql.get_db().commit()
    return redirect('/read')

@app.route('/read')
def read():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM genres")
    # html = ''    
    if response > 0:
        genres = cursor.fetchall()
        return render_template('read.html', list=genres)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)

    