import gdata.photos.service
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.2')
import logging
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
      username = 'cherny.berbesi@gmail.com'
      password = '22,e6G1x'
      source = 'AlvaroGreenSite'
      if self.request.get('album'):
        album = self.request.get('album')
      else:
        album = 'sociales'
      gd_client = gdata.photos.service.PhotosService()
      gd_client.email = username
      gd_client.password = password
      gd_client.source = source
      gd_client.ProgrammaticLogin()
      albums_entry = gd_client.GetUserFeed()
      photos = list()
      i = 0
      for album_entry in albums_entry.entry:
        if album_entry.title.text == album:
          photos_entry = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (username, album_entry.gphoto_id.text))
          for photo_entry in photos_entry.entry:
            photos.append({
              'albumId' : photo_entry.albumid.text,
              'photoId' : photo_entry.gphoto_id.text,
              'thumbnailUrl' : photo_entry.media.thumbnail[0].url,
              'url' : photo_entry.content.src
            })
            i += 0
        logging.info('title: %s, number of photos: %s, id: %s' % (album_entry.title.text, album_entry.numphotos.text, album_entry.gphoto_id.text))
      logging.info(str(photos))
      templates_values = { 'album' : album , 'photos' : photos}
      path = os.path.join(os.path.dirname(__file__), 'templates/gallery.html')
      self.response.out.write(template.render(path, templates_values))

application = webapp.WSGIApplication([('/gallery', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
