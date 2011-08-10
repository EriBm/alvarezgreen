import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'cherny-alvarezgreen.settings'

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.redirect('/gallery?album=inicio')

class BiographyPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/biography.html')
        self.response.out.write(template.render(path, None))

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/biography', BiographyPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()