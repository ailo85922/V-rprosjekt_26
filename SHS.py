from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template('SHS.html'))

@app.route("/contact")
def contact():
    return(render_template('kontaktoss.html'))

@app.route("/products")
def products():
    return(render_template('produkter.html'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
