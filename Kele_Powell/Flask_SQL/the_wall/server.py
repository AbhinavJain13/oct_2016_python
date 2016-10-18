from flask import Flask, render_template, redirect,request, session, flash
import re
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app=Flask(__name__)
app.secret_key="goldfish"
bcrypt= Bcrypt(app)
mysql=MySQLConnector(app,'the_wall')
def email_query():
    email_check='select* from users where email=:email'
    emails={
    'email':session['email']
    }
    email=mysql.query_db(email_check,emails)
    return email

@app.route('/')
def index():
    if 'email' not in session:
        session['email']=""
    if 'first' not in session:
        session['first']=""
    if 'last' not in session:
        session['last']=""
    return render_template("index.html")




@app.route('/register',methods=['POST'])
def register():
    count=0
    session['email']=request.form['email']
    session['first']=request.form['first']
    session['last']=request.form['last']

    email_check= "SELECT email from users"
    emails=mysql.query_db(email_check)
    for email in emails:
        if email['email']==request.form['email']:
            flash(u"email already taken",'error')
            count=1

    if not EMAIL_REGEX.match(request.form['email'] or len(request.form['email'])>3 ):
        flash(u"Need a valid Email",'error')
        count=1
    if not len(request.form['first'])> 1 or request.form['first'].isalpha():
        flash(u"Please enter a valid first name",'error')
        count=1
    if not len(request.form['last'])> 1 or request.form['last'].isalpha():
        flash(u"Please enter a valid Last Name",'error')
        count=1
    if len(request.form['pass'])< 7:
        flash(u"Please enter a password",'error')
        count=1
    if len(request.form['repass'])< 7:
        flash(u"Please confirm your password",'error')
        count=1
    if request.form['repass'] !=request.form['pass']:
        flash(u"Passwords Do not Match!",'error')
        count=1
    if count==1:
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pass'])

    query= "INSERT INTO users (email, first_name, last_name, password, created_at, updated_at) VALUES (:email, :first_name, :last_name, :password, NOW(), NOW())"
    data={
    "email":session['email'],
    "first_name":session['first'],
    "last_name":session['last'],
    "password":pw_hash,
    }
    mysql.query_db(query,data)
    flash(u"successfully registered!",'success')
    return redirect('/main')

@app.route('/login',methods=['POST'])
def login():
    verify=1
    count=0
    session['email']=request.form['email']
    email_check= "SELECT email from users"
    emails=mysql.query_db(email_check)
    for email in emails:
        if   email['email']==request.form['email']:
            verify=0
            continue
        else:
            pass
    if verify==1:
        flash(u"Email and password do not match. please try again",'error')
        return redirect('/')

    if len(request.form['email'])<3:
        flash(u"Email too short",'error')
        count=1
    if not EMAIL_REGEX.match(request.form['email']):
        flash(u"Need a valid Email",'error')
        count=1
    if len(request.form['pass'])< 7:
        flash(u"Please enter a password",'error')
        count=1
    if count==1:
        return redirect('/')
    query="Select * from users where email=:email LIMIT 1"
    data={
    "email":request.form['email']
    }

    user=mysql.query_db(query,data)
    if bcrypt.check_password_hash(user[0]['password'],request.form['pass']):
        session['first']=user[0]['first_name']
        session['last']=user[0]['last_name']
        return redirect('/main')
    else:
        flash(u"Email and password do not match. please try again",'error')
        return redirect('/')

@app.route('/main')
def test():
    users=email_query()
    message_list='''SELECT concat(first_name," ", last_name)as name,messages.id,messages.user_id,messages.message,messages.updated_at
    from messages
    left join users on users.id=messages.user_id
    ORDER BY updated_at DESC'''
    messages=mysql.query_db(message_list)

    comments_list='''SELECT concat(first_name," ", last_name)as name,comments.message_id,comments.id, comments.user_id,comments.comment,comments.updated_at
    from users
    left join comments on users.id=comments.user_id
    ORDER BY updated_at DESC'''
    comments=mysql.query_db(comments_list)
    return render_template('main.html',users=users,messages=messages, comments=comments)

@app.route('/message',methods=['post'])
def post_message():
    if len(request.form['name'])>1:
        try:
            email=email_query()
            messages='INSERT INTO messages (message, created_at, updated_at, user_id)values(:message, NOW(),NOW(),:user)'
            message={
            'message':request.form['name'],
            'user':email[0]['id']
            }
            mysql.query_db(messages,message)
        except IndexError:
            flash("please login or register to continue","error")
            return redirect('/')
    return redirect('/main')
@app.route("/main/comment/<message_id>",methods=['post'])
def post_comment(message_id):
    if len(request.form['comm'])>1:
        try:
            email= email_query()
            comments='INSERT INTO comments (comment, created_at, updated_at, user_id, message_id)values(:comment, NOW(),NOW(),:user,:message)'
            comment={
            'comment':request.form['comm'],
            'user':email[0]['id'],
            'message':message_id,
            }
            mysql.query_db(comments,comment)
        except IndexError:
            flash("please login or register to continue","error")
            return redirect('/')
    return redirect('/main')
@app.route('/delete/message/<id>')
def delete_message (id):
    query= "delete from comments where message_id=:id"
    data={
    'id':id
    }
    mysql.query_db(query, data)
    query= "delete from messages where id=:id"
    data={
    'id':id
    }
    mysql.query_db(query, data)
    return redirect ('main')
@app.route('/edit_message/<id>')
def edit_mess(id):
    users=email_query()
    message_list='SELECT * from messages where id=:id'
    data= {
    'id':id
    }

    messages=mysql.query_db(message_list,data)
    return render_template ('edit.html',users=users,messages=messages)
@app.route('/edit_comment/<id>')
def edit_comm(id):
    users=email_query()
    comment_list='SELECT * from comments where id=:id'
    data= {
    'id':id
    }
    comments=mysql.query_db(comment_list,data)
    comments_list='SELECT * from comments where id=:id'

    return render_template ('edit.html',users=users, comments=comments)
@app.route('/edit/messages/<id>', methods=['post'])
def edit_message (id):
    query= "UPDATE messages set message=:message, updated_at=NOW() where id=:id"
    data={
    'message':request.form['edit_message'],
    'id':id
    }
    mysql.query_db(query,data)
    return redirect ('/main')
@app.route('/edit/comment/<id>', methods=['post'])
def edit_comment (id):
    query= "UPDATE comments set comment=:comment, updated_at=NOW() where id=:id"
    data={
    'comment':request.form['edit_comment'],
    'id':id
    }
    mysql.query_db(query,data)
    return redirect ('/main')
@app.route('/delete/comment/<id>')
def delete_comment (id):
    query= "delete from comments where id=:id"
    data={
    'id':id
    }
    mysql.query_db(query, data)
    return redirect ('main')


@app.route('/logout')
def logout():
        session.clear()
        flash(u'succesfully logged out!',"success")
        return redirect('/')
app.run(debug=True)
