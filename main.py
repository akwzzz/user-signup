from flask import Flask, request, redirect, render_template
import cgi
import os
 
app = Flask(__name__)
app.config['DEBUG'] = True

   
 

@app.route("/")
def display_form():   
    username_error = request.args.get('username_error')
    password_error = request.args.get('password_error')
    email_error = request.args.get('email_error')
    
    return render_template('index.html', username_error = '', password_error='', email_error='')

  


    

    

@app.route("/welcome", methods=['post'])
def validate_info():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
                        
    if username.strip() == "":
        username_error = "Please enter a Username"
        return render_template('index.html', username_error=username_error)
        
    else:
        if len(username) > 20 or len(username) < 3:
            username_error = "Please create a Username between 3-20 characters in length"    
            return render_template('index.html', username_error=username_error)

        else:
            if " " in username:
                username_error = "Please do not include spaces in your Username"
                return render_template('index.html', username_error=username_error)

            else: username_error = ''

    if password != verify_password:
        password_error = "Please make sure your passwords match!" 
        return render_template('index.html', password_error=password_error)
    else:
        if password.strip() == "":
            password_error = "Please enter a password"  
            return render_template('index.html', password_error=password_error)
        else:
            if verify_password.strip() == "":
                password_error = "Please verify your password"
                return render_template('index.html', password_error=password_error) 
            else:
                if len(password) > 20 or len(password) < 3:
                    password_error = "Please create a password between 3-20 characters in length"    
                    return render_template('index.html', password_error=password_error)

                else: password_error = ''

    if email:

        if len(email) > 20 or len(email) < 3:
            email_error = "Please enter a valid email"    
            return render_template('index.html', email_error=email_error) 
        else:
            if "@" not in email:
                email_error = "Please enter a valid email"
                return render_template('index.html', email_error=email_error) 
            else:
                if "." not in email:
                    email_error = "Please enter a valid email"
                    return render_template('index.html', email_error=email_error)   
                else:
                    if " " in email:
                        email_error = "Please do not include spaces in your email"
                        return render_template('index.html', email_error=email_error) 

                    else: email_error = ''
    else:
        email_error = False 

    if not username_error and not password_error and not email_error: 
        return welcome_message()
    else:
        return render_template ("index.html", username=username, email=email, username_error=username_error, password_error=password_error, email_error=email_error)    

def welcome_message():
    username = request.form['username']
    return render_template('greeting.html', name=username)





app.run()