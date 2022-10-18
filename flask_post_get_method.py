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

@app.route("/info",methods=['GET','POST'])
def info():
    if request.method == "GET":
        return "<h1>GET Method</h1>Hello "+ request.args.get('user') + \
    " Your Email:"+request.args.get('email')
    else:
        return "<h1>POST Method</h1>Hello "+ request.form['user'] + \
    " Your Email:"+request.form['email']

if __name__ == '__main__': 
    app.run(debug=True) 