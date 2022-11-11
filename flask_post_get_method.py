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
        return "<h1>Response Submitted through GET!</h1><b>Dear "+ request.args.get('user')+" ."+ \
    " Your response against e-mail: "+request.args.get('email') + \
    " has been submitted successfully"
    else:
        return "<h1>Response Submitted through POST!</h1><b>Dear "+ request.form['user']+" ." + \
    " Your response against e-mail: "+request.form['email']  + \
    " has been submitted successfully!"       

if __name__ == '__main__': 
    app.run(debug=True) 