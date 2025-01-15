



from flask import redirect,render_template,url_for, Flask,request, session


app = Flask(__name__)
app.secret_key = "hello"

admin_user = "sigma"
admin_password = "1234"


def get_lines(l): # converts maze txt into array
    lister = []
    line=""
    txt = open(l,'r')
    content = txt.readlines()
    txt.close()
    for row in content:
        for item in row:
            line = line + item
        lister.append(line)
        line = ""
    
    return lister




@app.route("/", methods = ['GET','POST'])
def initial():
    session['inputs'] = []
    # this is the home login page 
    if request.method == "POST":
        for index,value in request.form.items():
            session['inputs'].append(value)
            print(session['inputs'])

        if session['inputs'][0] == admin_user and session['inputs'][1] == admin_password:
            print("correct login!!!")
            return redirect(url_for('start'))
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')
    

@app.route("/start") # this is the home page with all the things
def start():
    return render_template('start_page.html')    


@app.route("/transactions")
def trans():
    transaction_records =get_lines('transactions.txt')
    print(transaction_records)
    return render_template('transactions.html',transer = transaction_records)
        


@app.route("/customers")
def cust():
    customers_records =get_lines('customers.txt')
    print(customers_records)
    return render_template('customers.html',transer = customers_records)
        













if __name__ == '__main__':
    app.run(debug=True)
