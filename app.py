from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html") 

@app.route('/re', methods=["GET", "POST"])
def index():
    return render_template("index.html")
@app.route('/result', methods=["GET","POST"])
def result():
    text = request.form.get("text")
    regex = request.form.get("regex")
    matches = re.findall(regex, text)
    return render_template("index.html",matches=matches)


@app.route('/email', methods=["GET", "POST"])
def email():
    return render_template("email.html")

@app.route('/emailvalid', methods=["GET","POST"])
def emailvalid():
    email = request.form.get("email")
    regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        match="Valid Email adress"
    else:
        match="Invalid Email address"
    return render_template("email.html",match=match)
    
if __name__ == '__main__':
    app.run(debug=True)