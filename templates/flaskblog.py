from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Your login logic here
        login_successful = check_login(username, password)

        if login_successful:
            return render_template('ana.html')
        else:
            return redirect('/')
    else:
        # Handle GET request for the /home route
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
