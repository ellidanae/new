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
    cur.execute("DELETE FROM authors WHERE authorID=%s",id)
    mysql.get_db().commit()
    return redirect('/read')

@app.route('/author')
def author():
    author = {}
    author['id'] = request.args.get('id')
    author['firstname'] = request.args.get('firstname')  
    author['lastname'] = request.args.get('lastname')   
    author['address'] = request.args.get('address')    
    author['phone'] = request.args.get('phone')
    return render_template('author.html', author=author)

@app.route('/update', methods=['POST'])
def add():
    author = request.form
    id = author['id']
    firstname = author['FirstName']
    lastname = author['LastName']
    address = author['Address']
    phone = author['Phone']
    cur = mysql.get_db().cursor()
    # here question:
    #why do we have first the name an dthen the id?
    #what happens exactly with this command
    cur.execute("UPDATE authors SET firstname=%s WHERE authorID=%s",(firstname, id))
    cur.execute("UPDATE authors SET lastname=%s WHERE authorID=%s",(lastname, id))
    cur.execute("UPDATE authors SET address=%s WHERE authorID=%s",(address, id))
    cur.execute("UPDATE authors SET phone=%s WHERE authorID=%s",(phone, id))

    # cur.execute ("UPDATE authors SET firstname=%s, lastname=%s WHERE authorID=%s " % (firstname, lastname, id))


    mysql.get_db().commit()
    return redirect('/read')

@app.route('/read')
def read():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM authors")
    # html = ''    
    if response > 0:
        authors = cursor.fetchall()
        return render_template('read.html', list=authors)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)

    