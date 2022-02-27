from django.http import HttpRequest
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/mydatabase' #whichdatabase you use and connect


db = SQLAlchemy(app) #initialaization

class Data1(db.Model): #class define database   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(150), nullable=False)
    


@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        name =  request.form['name']
        email =  request.form['email']
        message=  request.form['message']
        entry = Data1(name=name,email=email,message=message)
        
        db.session.add(entry) #Place an object in the Session.
        db.session.commit() #Flushing - push changes
        return("Thanks for contacting")
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)