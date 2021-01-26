from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def root():
    return "This is the root of the endpoint"

@app.route("/gloves", methods = ['GET'])
def gloves():
    return "Gloves"

@app.route("/facemasks", methods = ['GET'])
def root():
    return "Facemasks"

@app.route("/beanies", methods = ['GET'])
def root():
    return "Beanies"

if __name__ == '__main__':
    app.run(debug=True)
