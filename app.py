from flask import  Flask, request, render_template

app = Flask( __name__ )

@app.route('/', methods=['GET','POST'])
def index():
    return  render_template('home.html')

@app.route('/login', methods=['GET','POST'] )
def login():
    if request.method == 'POST':
        pass

    return render_template("faculictylogin.html")
    
if __name__ == "__main__":
        app.run(debug = True)