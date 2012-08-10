import tornado.ioloop
import tornado.web
from tornado.template import Loader
import os

from local_settings import *

from serverdensity.api import SDApi, SDServiceError

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = Loader("../templates")

        api = SDApi(
            URL,
            USERNAME,
            PASSWORD,
            API_KEY
        )

        alerts = api.alerts.getLast()
        devices = api.devices.list()
        self.write(loader.load("index.html").generate(devices=devices['data']['devices'], alerts=alerts['data']['alerts']))

def run():
    static_path = os.path.join(os.path.dirname(__file__), '../..', 'static')
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], static_path=static_path)
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()