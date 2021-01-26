from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
import requests
import time

app = Flask(__name__)

API_BASE = "https://bad-api-assignment.reaktor.com"

@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/gloves", methods = ['GET'])
def gloves():

    makers = set()
    ret_data = []

    r = requests.get(API_BASE + "/v2/products/gloves")
    if r.status_code != 200:
        return "ERROR"
    data = r.json()

    # for item in data:
    #     makers.add(item["manufacturer"])
    #
    # for maker in makers:
    #     if maker not in MA.keys():
    #         req = requests.get(API_BASE + "/v2/availability/" + maker)
    #         MA[maker] = {}
    #         for prod in req.json()["response"]:
    #             MA[maker][prod["id"]] = prod["DATAPAYLOAD"]
    #
    # for item in data:
    #     product = item
    #     product["availability"] = ET.fromstring(MA[product["manufacturer"]][product["id"]]).find("INSTOCKVALUE").text
    #     ret_data.append(item)


    return render_template("gloves.html", items = data)


@app.route('/background_process_test/<id>/<manufacturer>')
def background_process_test(id, manufacturer):
    print(id, manufacturer)
    
    return id


@app.route("/facemasks", methods = ['GET'])
def facemasks():
    return "Facemasks"

@app.route("/beanies", methods = ['GET'])
def beanies():
    return "Beanies"

if __name__ == '__main__':
    app.run(debug=True)
