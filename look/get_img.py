import json
import falcon
import requests

class Resource(object):
    def on_get(self, req, resp):
        apod_url = "https://api.nasa.gov/planetary/apod?api_key=DlArxIrdbCsDiAB2mA6Jo4m0PBFrWut8VSnkAQDe"
        apod_resp = requests.get(apod_url)
        apod_resp = json.loads(apod_resp.text)

        url = apod_resp['url']
        desc = apod_resp['explanation']
        rvalue = '{"img_url": "'+url+'", "desc": "'+desc+'"'+"}"
        resp.status = falcon.HTTP_200
        resp.body = rvalue
        