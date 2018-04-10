from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")

def display_form():
    return render_template('index.html')



Global_username =[]

@app.route("/welcome", methods=['POST' , 'GET'])

def success():
    username = request.args.get('username')
    return render_template('welcome.html', username= username)


@app.route("/error" , methods=['POST'])

def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    empty_field_error = ''
    username_error = ''
    password_error = ''
    match_error = ''
    empty_email_error = ''
    email_error = ''


    if username.strip()==''or password.strip()=='' or verify.strip()=='':
        empty_field_error ='You cannot leave required fields empty. Please try again.'


    if (len(username) < 2) or (len(username) > 19) and username.isalpha() == False:
        username_error = 'Your username must consist of 3 to 20 more alphabetical characters only. Please try again.'
        username = ''
    
    if (len(password) < 2) or (len(password) > 19) and password.isalpha() == False:
        password_error = 'Your password must consist of 3 to 20 more alphabetical characters only. Please try again.'

    
    if password != verify:
        match_error = 'Your password entry must match your Verify Password entry exactly. Please try again.'


    if email == '':
        empty_email_error = "technically you dont have to enter an email but... dont you want to anyway?"


    if email and ((len(email) < 2) or (len(email) > 19) or (email.count("@") > 1) or (email.count("@") < 1) or (email.count(".") > 1) or (email.count(".") < 1) or (email.count(" ") >= 1)):
        email_error = 'Your email is terrible!'

        
    if (not empty_field_error) and (not username_error) and (not password_error) and (not match_error) and not (email_error):
        username_supreme = username
        return redirect('/welcome?username={0}'.format(username_supreme))

    else:
        return render_template('index.html', empty_field_error = empty_field_error, username = username, username_error=username_error, password_error= password_error, match_error=match_error, email = email, email_error=email_error, empty_email_error = empty_email_error)

app.run()