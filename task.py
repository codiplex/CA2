from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<div style="background-color: skyblue; text-align: center;"><h1 style="color: green;">Hello World</h1></div>'

app.run(host='0.0.0.0', port=81)