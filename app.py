



from flask import redirect,render_template,url_for, Flask,request, session
import datetime

app = Flask(__name__)
app.secret_key = "hello"

admin_user = "sigma"
admin_password = "1234"


def get_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]  # Strips leading/trailing whitespace

def write_line(file,line):
    with open(file, "a") as myfile:
        myfile.write(line + '\n')



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
        


@app.route("/veiw stocks", methods = ['GET','POST'])
def stoxxer():
    current_date= datetime.datetime.now()
    session['inputs'] = []
    stox_list = get_lines('stocks.txt')
    # this is the home login page 
    if request.method == "POST":
        for index,value in request.form.items():
            session['inputs'].append(value)
            print(session['inputs'])
            print(len(stox_list))
            print(stox_list)
        if 1 <= int(session['inputs'][0]) <= len(stox_list):
            print("satisfied")
            replacing_item = int(session['inputs'][0]) - 1
            print(stox_list[replacing_item])
            name,price, amount = stox_list[replacing_item].split(',')
            print(name,price,amount)
            amount = int(amount) - 1
            if amount > 0:
                stox_list[replacing_item] = f"{name},{price},{amount}"
                print('replacing')
            else:
                stox_list.pop(replacing_item)
            print("stock_list_1",stox_list)
            with open('stocks.txt', "w") as myfile:
                for line in stox_list:
                    if len(line) > 2:
                        myfile.write(line + '\n')
            stox_list = get_lines('stocks.txt')
            print("stock_list_2",stox_list)
            
            write_line('transactions.txt', name + " at " + current_date.strftime("%d-%m-%Y") )

    return render_template('veiw_stocks.html',transer = stox_list)
        


@app.route("/add_stocks", methods = ['GET','POST'])
def stox():
    session['inputs'] = []
    # this is the home login page 
    if request.method == "POST":
        for index,value in request.form.items():
            session['inputs'].append(value)
            print(session['inputs'])
        
        if 4 < len(session['inputs'][0]) < 20 and session['inputs'][1].isalnum and session['inputs'][2].isalnum:
            print("passed first test!")
            if 0 < int(session['inputs'][1]) < 250:
                print("passed second test!")
                if  0 < int(session['inputs'][2]) < 250:
                    print("passed final test!")
                    linee = session['inputs'][0] + "," + session['inputs'][1] + "," + session['inputs'][2] 
                    print(linee)
                    write_line('stocks.txt', linee  )
 
    stox_list = get_lines('stocks.txt')
    print(stox_list)
    return render_template('add_stocks.html')
        

@app.route('/add_customers' , methods = ['GET','POST'])
def add_customer():
    session['inputs'] = []
    if request.method == "POST":
        for index,value in request.form.items():
            session['inputs'].append(value)
            print(session['inputs'])
        linee = session['inputs'][0] + "," + session['inputs'][1] 
        print(linee)
        write_line('customers.txt', linee  )
    
    return render_template('add_customers.html')







if __name__ == '__main__':
    app.run(debug=True)
