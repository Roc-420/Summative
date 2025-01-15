



from flask import redirect,render_template,url_for, Flask,request


app = Flask(__name__)
app.secret_key = "hello"





@app.route("/")
def start():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)
