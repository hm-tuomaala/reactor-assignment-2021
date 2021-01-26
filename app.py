from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/gloves", methods = ['GET'])
def gloves():
    return "Gloves"

@app.route("/facemasks", methods = ['GET'])
def facemasks():
    return "Facemasks"

@app.route("/beanies", methods = ['GET'])
def beanies():
    return "Beanies"

if __name__ == '__main__':
    app.run(debug=True)
