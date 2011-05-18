import gdata.photos.service
from gdata.service import BadAuthentication
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'alvarezgreen.settings'

from google.appengine.dist import use_library
use_library('django', '1.2')
import logging
from google.appengine.api import mail
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
      username = 'cherny.berbesi@seiteca.com'
      password = '22,e6G1x'
      source = 'AlvaroGreenSite'
      if self.request.get('album'):
        if '-' in self.request.get('album'):
          _category, _album = self.request.get('album').split('-')
        else:
          _category, _album = [self.request.get('album'), None]
      else:
        _category, _album = ['inicio', 'inicio']
      gd_client = gdata.photos.service.PhotosService()
      gd_client.email = username
      gd_client.password = password
      gd_client.source = source
      try:
        gd_client.ProgrammaticLogin()
      except BadAuthentication:
        self.response.out.write('Problema de autenticaci&oacute;n')
        mail.send_mail(sender="cherny.berbesi@gmail.com>",
                       to="Cherny D. C. Berbes&iacute; I. <cherny.berbesi@gmail.com>",
                       subject="Problema con la pagina Web alvarezgreen.com",
                       body="""Esta recibiendo este correo porque cambio su contrasena de Google y altero el servicio de picasa""")
        return
      albums_entry = gd_client.GetUserFeed()
      photos = list()
      i = 0
      albums = list()
      photo_selected = None
      for album_entry in albums_entry.entry:
        if album_entry.title.text != 'inicio':
          category, album = album_entry.title.text.split('-')
        else:
          category, album = ['inicio', 'inicio']
        if category == _category:
          albums.append({'category' : category, 'album' : album})
          if _album is None:
            _album = album
          if album_entry.title.text == str(_category + "-" + _album) or _category == 'inicio':
            photos_entry = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (username, album_entry.gphoto_id.text))
            for photo_entry in photos_entry.entry:
              photo = {
                'albumId' : photo_entry.albumid.text,
                'photoId' : photo_entry.gphoto_id.text,
                'thumbnailUrl' : photo_entry.media.thumbnail[0].url,
                'url' : photo_entry.content.src
              }
              if photo_selected is None:
                photo_selected = photo
              photos.append(photo)
              i += 0
#        logging.info('title: %s, number of photos: %s, id: %s' % (album_entry.title.text, album_entry.numphotos.text, album_entry.gphoto_id.text))
      templates_values = { 'album_selected' : _album , 'photos' : photos, 'albums' : albums, 'photo_selected' : photo_selected}
      path = os.path.join(os.path.dirname(__file__), 'templates/gallery.html')
      self.response.out.write(template.render(path, templates_values))

application = webapp.WSGIApplication([('/gallery', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()