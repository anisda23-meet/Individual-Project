from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

config = {
  "apiKey": "AIzaSyDVsGa1CLaT0RZbQ1IsZjf9ABW4wAPzoEc",
  "authDomain": "individual-project-1dcc9.firebaseapp.com",
  "databaseURL": "https://individual-project-1dcc9-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "individual-project-1dcc9",
  "storageBucket": "individual-project-1dcc9.appspot.com",
  "messagingSenderId": "1052631649320",
  "appId": "1:1052631649320:web:299fbf4a40fecfb20d791d",
  "measurementId": "G-KQ54J2GDB2",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route("/", methods = ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('main'))
        except:
            error = "Authentication failed"
            return redirect(url_for('signin'))
    else:
        return render_template("style.html")

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        user = {"email" : email, "username" : username, "password" : password}
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            db.child('Users').child(login_session['user']['localId']).set(user)
        except:
           error = "Authentication failed"
        return redirect(url_for('main'))
    else:
        return render_template("signup.html")

@app.route("/main", methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        user = {"email" : email, "username" : username, "password" : password}
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            db.child('Users').child(login_session['user']['localId']).set(user)
        except:
           error = "Authentication failed"
        return redirect(url_for('main'))
    else:
        return render_template("main.html")
#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)