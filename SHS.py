from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template('SHS.html'))

@app.route("/")
def home():
    return(render_template('kontaktoss.html'))

@app.route("/")
def home():
    return(render_template('produkter.html'))

if __name__ == "__main__":
    app.run(debug=True)
