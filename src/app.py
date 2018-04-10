import tornado.ioloop
import tornado.web


import base64
import collections
import hashlib
import os
import struct
import tornado.escape
import tornado.web
import tornado.websocket
import zlib



class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("Hello, world")
        self.finish()



class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/ws', WebSocketHandler),
        (r'/index', IndexPageHandler),
        (r'/(favicon.ico)', tornado.web.StaticFileHandler, {'path': '../'}),
        (r'/(rest_api_example.png)', tornado.web.StaticFileHandler, {'path': './'}),
    ])




if __name__ == "__main__":
    app = make_app() #"ws://localhost:8888/websocket"
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
