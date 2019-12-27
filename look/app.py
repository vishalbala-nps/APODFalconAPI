import falcon
from .get_img import Resource

application = falcon.API()

apod_img = Resource()
application.add_route('/get_img', apod_img)