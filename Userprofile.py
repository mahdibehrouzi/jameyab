import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class PageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('profile.html', you=noun1, userName=noun2, weight=noun3, age=verb)

if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/profile', PageHandler)
        ],
        template_path="template")
    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

