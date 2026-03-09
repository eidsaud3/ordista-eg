from flask import Flask, render_template , request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/account', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Here you can add code to validate the email and password
        # For example, you can check if they match a predefined set of credentials
        if email == 'admin@example.com' and password == 'password':
            return render_template('account.html', email=email)
        else:
            error_message = 'Invalid email or password. Please try again.'
            return render_template('index.html', error=error_message)



if __name__ == '__main__':
    app.run(debug=True)