from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.htm') 

@app.route("/contact")
def contact(): 
    return render_template('contact.html')  

@app.route("/info",methods=['POST'])
def info():
    if request.method == "POST":
        return "<h1>POST Method</h1>Hello "+ request.args.get('user') + \
    " Your Email:"+request.args.get('email')
    
app.run(debug=True) 