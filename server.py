import routes
import cherrypy
# ---------
# Les 7 lignes suivantes permettent d'exécuter ce script sous M$:
# - soit par un double click
# - soit sous "Idle" (dans ce cas la variable __file__ n'est pas définie)
# Ne vous cassez pas la tête avec ça.
import inspect, os

from Core.Database import Database
from Model.Dessinateur import Dessinateur
from Model.Editeur import Editeur
from Model.Genre import Genre
from Model.Manga import Manga
from Model.Scenariste import Scenariste
from Model.Statut import Statut

try :
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
except NameError :
    __file__ = inspect.getfile(inspect.currentframe())
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
print (_curdir)
# ---------
# ---------
# Début du code effectif :
from mako.template import Template
from mako.lookup import TemplateLookup

myTemplatesDir = os.path.join(_curdir,'View/template')
myModulesDir = os.path.join(_curdir,'View/tmp/mako_modules')
mylookup = TemplateLookup(directories=[myTemplatesDir], module_directory=myModulesDir,
                          output_encoding='utf-8',
                          encoding_errors='replace')

#------------------------------------------------------------
# Templates HTML
#------------------------------------------------------------
_page = mylookup.get_template("home.html")
_detail = mylookup.get_template("detail.html")
_new = mylookup.get_template("new.html")
#_auteur = mylookup.get_template("login.html")
#_detail = mylookup.get_template("detailMessage.html")

#------------------------------------------------------------
# Point d'entrée de l'application "MangaCollection"
#------------------------------------------------------------

class Home:
    """
    Application hébergée par CherryPy
    """
    # On autorise les sessions
    # _cp_config = { 'tools.sessions.on': True }

    @cherrypy.expose
    def index(self):
        db = Database()
        return _page.render_unicode(mangas = db.retrieve(Manga))

    @cherrypy.expose
    def detail(self,id):
        db = Database()
        return _detail.render_unicode(manga = db.retrieve(Manga,Manga.id,id) ,tomes = db.retrieveTome(id))

    @cherrypy.expose
    def new(self):
        db = Database()
        return _new.render_unicode(
            scenaristes = db.retrieve(Scenariste),
            dessinateurs = db.retrieve(Dessinateur),
            editeurs = db.retrieve(Editeur),
            genres = db.retrieve(Genre),
            statuts = db.retrieve(Statut)
        )

if __name__ == '__main__':
    # La configuration n'est plus dans un fichier, mais directement ici!
    global_conf = {
        'global': { 'autoreload.on': False,
			'server.socket_host': '127.0.0.1',
			'server.protocol_version': 'HTTP/1.1',
                            'server.thread_pool' : 5,
                            'tools.encode.encoding' : "Utf-8",
                            'environment': 'production',
                            'log.error_file': 'site.log',
                            'log.screen': True}}
    cherrypy.config.update(global_conf)

    # Création de l'instance de l'appli
    app = Home()
    # Create an instance of the dispatcher
    d = cherrypy.dispatch.RoutesDispatcher()
    d.connect('default_route', '/', controller=app, action='index')
    d.connect('some_other', '/:action/:id/',controller=app, action='detail')
    d.connect('new', '/:action/',controller=app, action='new')

    conf_appli = {
        '/': {'request.dispatch': d},
        '/View': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(_curdir, 'View')},
        '/View/templates': {'tools.staticdir.on': True, 'tools.staticdir.dir': myTemplatesDir},
        '/View/tmp/mako_modules': {'tools.staticdir.on': True,'tools.staticdir.dir': myModulesDir},
        '/View/css': {
            'tools.staticdir.on': True,'tools.staticdir.dir': os.path.join(_curdir, 'View/css'),
            'tools.staticdir.content_types': {'css': 'text/css'}
        },
        '/View/images': {
            'tools.staticdir.on': True,'tools.staticdir.dir': os.path.join(_curdir, 'View/images'),
            'tools.staticdir.content_types': {'jpg': 'image/jpg'}
        },
        '/View/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(_curdir, 'static/js'),
            'tools.staticdir.content_types': {'js': 'application/javascript'}
        }}

    cherrypy.quickstart(app, config=conf_appli)
