import json
import falcon
class Resource(object):
    def get_img(self, request, response):
        url = "google.com"
        desc  "Google"
        rvalue = '{"img_url": "'+url+'", desc: "'+desc+'"'