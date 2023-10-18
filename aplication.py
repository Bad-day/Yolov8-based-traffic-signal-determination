from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def start_page():
    print("start_page")
    return 'start page'

@app.route('/main')
def main_page():
    print("activated")
    return render_template("index.html")

app.run(host='0.0.0.0')