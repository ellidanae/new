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
    cur.execute("DELETE FROM publishers WHERE publisherID=%s",id)
    mysql.get_db().commit()
    return redirect('/read')

@app.route('/publisher')
def publisher():
    publisher = {}
    publisher['id'] = request.args.get('id')
    publisher['name'] = request.args.get('name')  
    publisher['address'] = request.args.get('address')    
    publisher['phone'] = request.args.get('phone')
    return render_template('publisher.html', publisher=publisher)

@app.route('/update', methods=['POST'])
def add():
    publisher = request.form
    id = publisher['id']
    name = publisher['Name']
    address = publisher['Address']
    phone = publisher['Phone']
    cur = mysql.get_db().cursor()
    # here question:
    #why do we have first the name an dthen the id?
    #what happens exactly with this command
    cur.execute("UPDATE publishers SET name=%s WHERE publisherID=%s",(name, id))
    cur.execute("UPDATE publishers SET address=%s WHERE publisherID=%s",(address, id))
    cur.execute("UPDATE publishers SET phone=%s WHERE publisherID=%s",(phone, id))

    # cur.execute ("UPDATE publishers SET firstname=%s, lastname=%s WHERE publisherID=%s " % (firstname, lastname, id))


    mysql.get_db().commit()
    return redirect('/read')

@app.route('/read')
def read():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM publishers")
    # html = ''    
    if response > 0:
        publishers = cursor.fetchall()
        return render_template('read.html', list=publishers)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)

    