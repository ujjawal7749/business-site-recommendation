from flask import Flask, render_template, request
from flask import *
import modelpart
import suggestion
import contactsave

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/contact',methods=['POST'])
def contactform():
    name=request.form.get('cname')
    email=request.form.get('email')
    message=request.form.get('message')
    contactsave.saver1(name,email,message)
    return render_template('contact.html',submit=True)

@app.route('/templates', methods=['POST'])
def handleinput():
    searchbox = request.form.get('searchbox')
    if searchbox in suggestion.suggestion:
        tab_arr= modelpart.create_map(searchbox)
        return render_template("mapview.html",days=tab_arr,xx=searchbox)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

    