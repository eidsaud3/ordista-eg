from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# usrer - > json file
# product - > json file
# order - > json file
# cart - > json file
@app.route('/account')
def account():
    return render_template('account.html')
if __name__ == '__main__':
    app.run(debug=True)