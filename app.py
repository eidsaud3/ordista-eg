from flask import Flask , render_template as template
app = Flask(__name__)
@app.route('/')
def home():
    return template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
