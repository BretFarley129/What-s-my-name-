from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/process', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    return render_template("process.html", name = name)
    return redirect("/")



app.run(debug = True)