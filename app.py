from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_BASE = "https://bad-api-assignment.reaktor.com"

@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/gloves", methods = ['GET'])
def gloves():
    r = requests.get(API_BASE + "/v2/products/gloves")
    if r.status_code == 200:
        data = r.json()
        return render_template("gloves.html", items = data)



@app.route("/facemasks", methods = ['GET'])
def facemasks():
    return "Facemasks"

@app.route("/beanies", methods = ['GET'])
def beanies():
    return "Beanies"

if __name__ == '__main__':
    app.run(debug=True)
