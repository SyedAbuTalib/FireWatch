import os, random

from flask import Flask, render_template, url_for, request, Markup, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('base.html')


@app.route('/analysis/<lat>/<lng>', methods=['GET'])
def ana(lat, lng):
    # getData gets a 2D array
    # data[i][0] = url
    # data[i][1] = lat
    # data[i][2] = lng
	  if request.method == 'GET':
            data, heatmap = getData(lat, lng)
            links = ""
            for datapoint in data:
                links = links + datapoint[0] + "|||"
            links = links + "000|||"
            for datapoint in data:
                links = links + datapoint[1] + "|||"
            links = links + "000|||"
            for datapoint in data:
                  links = links + datapoint[2] + "|||"
            links = links + "000|||"
            for datapoint in heatmap:
                  links = links + datapoint[0] + "|||"
            links = links + "000|||"
            for datapoint in heatmap:
                  links = links + datapoint[1] + "|||"
            links = links + "000|||"
            for datapoint in heatmap:
                  links = links + datapoint[2] + "|||"
            return links

def getData(lat, lng):
    data = []
    for i in range(30):
        data.append(["https://twitter.com/tweeter/status/489879052157595649?ref_src=twsrc%5Etfw", str(float(lat) - 0.5 + random.random()), str(float(lng) - 0.5 + random.random()), i])
    heatmap = ericMethod(data)
    
    return data, heatmap

def ericMethod(data):
    heatmap = []
    for x in range(3):
        for line in data:
            heatmap.append([str(float(line[1]) - 0.05 + random.random()/10), str(float(line[2]) - 0.05 + random.random()/10), str(line[1] + line[2])])
    return heatmap

