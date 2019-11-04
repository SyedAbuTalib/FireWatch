import sys
import csv
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
            for datap in heatmap:
                  links = links + datap[0] + "|||"
            links = links + "000|||"
            for datap in heatmap:
                  links = links + datap[1] + "|||"
            links = links + "000|||"
            for datap in heatmap:
                  links = links + datap[2] + "|||"
            print(links)
            return links

def getData(lat, lng):
    #data = getMartinsData(lat,lng)
    data = []
    data.append(['https://twitter.com/cnnbrk/status/1190272548887498753','-119.068','34.3558','2019-11-02 04:55:17'])
    data.append(['https://twitter.com/SuaveHabibi/status/1188803056667770886','-120.088','34.6119','2019-11-02 02:24:50']);

    for i in range(30):
        data.append(["https://twitter.com/tweeter/status/489879052157595649?ref_src=twsrc%5Etfw", str(float(lat) - 0.5 + random.random()), str(float(lng) - 0.5 + random.random()), i])
    
    heatmap = ericMethod(data)
    return data, heatmap

def ericMethod(data):
    return [['34.36930492706232', '-119.10185276526958', '1'], ['34.368365960097414', '-119.135715155373', '2'], ['34.36631810673867', '-119.16958717304676', '3'], ['34.36915429839143', '-119.2034688210281', '4']];

    #heatmap = []
    #for x in range(3):
    #    for line in data:
    #        heatmap.append([str(float(line[1]) - 0.05 + random.random()/10), str(float(line[2]) - 0.05 + random.random()/10), str(line[1] + line[2])])
    #return    

def getMartinsData(lat, lng):
    return [['https://twitter.com/cnnbrk/status/1190272548887498753',
  '-119.068',
  '34.3558',
  '2019-11-02 04:55:17'],
 ['https://twitter.com/SuaveHabibi/status/1188803056667770886',
  '-120.088',
  '34.6119',
  '2019-11-02 02:24:50'],
 ['https://twitter.com/SuaveHabibi/status/1188803056667770886',
  '-119.068',
  '34.3558',
  '2019-11-02 00:29:21'],
  ['https://twitter.com/i/web/status/1190354874724241409',
  '-119.068',
  '34.3558',
  '2019-11-01 19:48:12'],
 ['https://www.instagram.com/p/B4V6x1enFuf/?igshid=1l3iqpsfixb8y',
  '-119.07023461',
  '34.21165938',
  '2019-11-02 00:12:01'],
 ['https://twitter.com/i/web/status/1190403872247955456',
  '-119.068',
  '34.3558',
  '2019-11-01 23:02:54'],
 ['https://twitter.com/i/web/status/1190391756384280576',
  '-119.068',
  '34.3558',
  '2019-11-01 22:14:45'],
 ['https://www.instagram.com/p/B4VdNP4AOD9/?igshid=1xib49vf776ms',
  '-119.068',
  '34.3558',
  '2019-11-01 19:55:07'],
 ['https://www.instagram.com/p/B4VWXDflRYN/?igshid=15zv3b3bw58mk',
  '-119.0391',
  '34.2231',
  '2019-11-01 18:54:32'],
 ['https://twitter.com/i/web/status/1190317838306828288',
  '-119.13599',
  '34.38263',
  '2019-11-01 17:21:02'],
 ['https://twitter.com/i/web/status/1190308350015131650',
  '-119.0391',
  '34.2231',
  '2019-11-01 16:43:20'],
 ['https://twitter.com/i/web/status/1190277558857682945',
  '-118.997115',
  '34.302212',
  '2019-11-01 14:40:58'],
 ['https://twitter.com/i/web/status/1190245740569694208',
  '-118.997115',
  '34.302212',
  '2019-11-01 12:34:32'],
 ['https://twitter.com/i/web/status/1190219423614820352',
  '-119.068',
  '34.3558',
  '2019-11-01 10:49:58'],
 ['https://twitter.com/i/web/status/1190206073430392833',
  '-119.182',
  '34.1913',
  '2019-11-01 09:56:55'],
 ['https://twitter.com/i/web/status/1190198568826658816',
  '-119.0391',
  '34.2231',
  '2019-11-01 09:27:06'],
 ['https://twitter.com/i/web/status/1190143035616612352',
  '-118.997115',
  '34.302212',
  '2019-11-01 05:46:26'],
 ['https://twitter.com/i/web/status/1190119129048465410',
  '-118.997115',
  '34.302212',
  '2019-11-01 04:11:26'],
 ['https://www.instagram.com/p/B4Tm8Nql9PN/?igshid=1wi67my54b55w',
  '-119.0391',
  '34.2231',
  '2019-11-01 02:40:17']];
