import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        self.render("index.html", list_info = {11, 22, 33})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)

''' settings
'''
settings = {
    "template_path" : "views",            # html文件
    "static_path": "static",              # 静态文件路径（css，js，img）
    "static_url_prefix" : "/static/",     # 静态文件前缀
}

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()