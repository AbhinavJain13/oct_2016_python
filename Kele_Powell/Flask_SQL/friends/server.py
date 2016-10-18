from flask import Flask, render_template, redirect, request, session
from mysqlconnection import MySQLConnector
app= Flask(__name__)
app.secret_key="peanut_buddah"
mysql=MySQLConnector(app,'full_friends')


@app.route('/')
def index():
    query= "select* from friends order by created_at DESC"
    friends=mysql.query_db(query)

    return render_template("index.html",friends=friends)

@app.route('/data', methods=['post'])
def create():
    session['first']=request.form['first']
    session['last']=request.form['last']
    session['email']=request.form['email']
    query= "INSERT INTO friends (first_name,last_name ,email, created_at, updated_at)VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data={
    "first_name":session['first'],
    "last_name":session['last'],
    "email": session['email']
    }
    mysql.query_db(query, data)
    return redirect ('/')

@app.route('/friend/<id>/edit')
def edit(id):
    print('hello')
    query= "SELECT * from friends WHERE id=:id"
    data={
    'id':id
    }

    friends= mysql.query_db(query,data)

    return render_template('friends.html', id=id,friends=friends)
@app.route('/friend/<id>', methods=['post'])
def update(id):
        session['first']=request.form['first']
        session['last']=request.form['last']
        session['email']=request.form['email']

        query="UPDATE friends Set first_name=:first,last_name=:last,email=:email, updated_at=NOW() WHERE id=:id"
        data={
        "first":session['first'],
        "last":session['last'],
        "email": session['email'],
        "id":id
        }
        print (data)

        mysql.query_db(query, data)
        return redirect('/')

@app.route('/friend/<id>/delete')
def destroy(id):
    query= "delete from friends where id=:id"
    data= {
    'id':id
    }
    mysql.query_db(query, data)
    return redirect ('/')




app.run(debug=True)
