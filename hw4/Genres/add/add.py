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
    genre = request.form
    name = genre['name']
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO genres(Name) VALUES(%s)",(name))
    mysql.get_db().commit()
    return redirect('/genres')

@app.route('/genres')
def genres():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM genres")
    # html = ''    
    if response > 0:
        genres = cursor.fetchall()
        return render_template('genres.html', list=genres)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)

    # http://localhost:3000