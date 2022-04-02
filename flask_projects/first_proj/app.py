from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['']

@app.route('/')
def hello_python():
    return render_template('index.html')
    # return "Hello, Sagar"

@app.route('/products')
def get_products():
    return "Products are available."

if __name__  == "__main__":
    app.run(debug=True, port=4000)
