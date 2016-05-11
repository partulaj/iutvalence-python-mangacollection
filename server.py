import routes
import cherrypy
import inspect, os
from mako.template import Template
from mako.lookup import TemplateLookup
from Core.Database import Database
from models import *

try:
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
except NameError:
    __file__ = inspect.getfile(inspect.currentframe())
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
print(_curdir)

myTemplatesDir = os.path.join(_curdir, 'View/template')
myModulesDir = os.path.join(_curdir, 'View/tmp/mako_modules')
mylookup = TemplateLookup(directories=[myTemplatesDir], module_directory=myModulesDir,
                          output_encoding='utf-8',
                          encoding_errors='replace')

# ------------------------------------------------------------
# Templates HTML
# ------------------------------------------------------------
_index = mylookup.get_template("index.html")
_collection = mylookup.get_template("collection.html")
_shopping_list = mylookup.get_template("shopping_list.html")
_search = mylookup.get_template("search.html")

_manga_list = mylookup.get_template("manga_list.html")
_manga_detail = mylookup.get_template("manga_detail.html")
_manga_new = mylookup.get_template("manga_new.html")

_scenariste_list = mylookup.get_template("scenariste_list.html")
_scenariste_new = mylookup.get_template("scenariste_new.html")

_dessinateur_list = mylookup.get_template("dessinateur_list.html")
_dessinateur_new = mylookup.get_template("dessinateur_new.html")

_editeur_list = mylookup.get_template("editeur_list.html")
_editeur_new = mylookup.get_template("editeur_new.html")

_genre_list = mylookup.get_template("genre_list.html")
_genre_new = mylookup.get_template("genre_new.html")

_tome_new = mylookup.get_template("tome_new.html")
_tome_detail = mylookup.get_template("tome_detail.html")

# ------------------------------------------------------------
# Point d'entrée de l'application "MangaCollection"
# ------------------------------------------------------------

class App:
    """
    Application hébergée par CherryPy
    """

    # On autorise les sessions
    # _cp_config = { 'tools.sessions.on': True }

    @cherrypy.expose
    def index(self):
        db = Database()
        genres = db.genreChartData()
        editeurs = db.editeurChartData()
        return _index.render_unicode(genres = genres, editeurs = editeurs)

    def collection(self):
        db = Database()
        mangas = db.retrieve(Manga)
        total = 0
        for manga in mangas:
            for tome in manga.tomes:
                if tome.possede == True:
                    total+= tome.prix
        return _collection.render_unicode(mangas=mangas, total=total)

    def shopping_list(self):
        db = Database()
        mangas = db.retrieve(Manga)
        return _shopping_list.render_unicode(mangas = mangas)

class MangaController:

    @cherrypy.expose
    def manga_list(self):
        db = Database()
        mangas = db.retrieve((Manga))
        return _manga_list.render_unicode(mangas=mangas)

    @cherrypy.expose
    def manga_detail(self, id):
        db = Database()
        manga = db.retrieve(Manga, Manga.id, id)
        return _manga_detail.render_unicode(manga = manga)

    @cherrypy.expose
    def manga_delete(self, id):
        db = Database()
        manga = db.retrieve(Manga, Manga.id, id)
        db.delete(manga, Manga)
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def manga_add(self, titre, description, editeur, scenariste, dessinateur, statut, genre):
        manga = Manga(titre, description, editeur, scenariste, dessinateur, statut, genre)
        db = Database()
        db.create(manga, Manga)
        raise cherrypy.HTTPRedirect('/manga/')

    @cherrypy.expose
    def manga_new(self):
        db = Database()
        return _manga_new.render_unicode(
            scenaristes=db.retrieve(Scenariste),
            dessinateurs=db.retrieve(Dessinateur),
            editeurs=db.retrieve(Editeur),
            genres=db.retrieve(Genre)
        )

class ScenaristeController:

    @cherrypy.expose
    def scenariste_list(self):
        db = Database()
        scenaristes = db.retrieve(Scenariste)
        return _scenariste_list.render_unicode(scenaristes=scenaristes)

    @cherrypy.expose
    def scenariste_new(self):
        return _scenariste_new.render_unicode()

    @cherrypy.expose
    def scenariste_add(self, scenariste):
        db = Database()
        s = Scenariste(scenariste)
        db.create(s,Scenariste)
        raise cherrypy.HTTPRedirect('/scenariste/')

class TomeController:

    @cherrypy.expose
    def tome_detail(self, id_manga, id_tome):
        db = Database()
        tome = db.retrieveTome(id_manga,id_tome)
        return _tome_detail.render_unicode(tome = tome)

    @cherrypy.expose
    def tome_new(self):
        db = Database()
        mangas = db.retrieve(Manga)
        return _tome_new.render_unicode(mangas = mangas)

    @cherrypy.expose
    def tome_delete(self, id_manga, id_tome):
        db = Database()
        tome = db.retrieveTome(id_manga, id_tome)
        db.deleteTome(tome)
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def tome_buy(self, id_manga, id_tome):
        db = Database()
        tome = db.retrieveTome(id_manga, id_tome)
        tome.a_acheter = False
        tome.possede = True
        db.update()
        raise cherrypy.HTTPRedirect('/collection/')

    @cherrypy.expose
    def tome_cart(self, id_manga, id_tome):
        db = Database()
        tome = db.retrieveTome(id_manga, id_tome)
        tome.a_acheter = True
        db.update()
        raise cherrypy.HTTPRedirect('/shopping_list/')

    @cherrypy.expose
    def tome_sell(self, id_manga, id_tome):
        db = Database()
        tome = db.retrieveTome(id_manga, id_tome)
        tome.possede = False
        db.update()
        raise cherrypy.HTTPRedirect('/collection/')

    @cherrypy.expose
    def tome_add(self, manga_id, numero, date_parution, prix, couverture, date_achat=None, possede=None, lu=None,
                 a_acheter=None):
        tome = Tome(manga_id, numero, date_parution, possede, lu, a_acheter, float(prix), couverture, date_achat)
        db = Database()
        db.create(tome,Tome)
        raise cherrypy.HTTPRedirect('/')

class DessinateurController:
    @cherrypy.expose
    def dessinateur_list(self):
        db = Database()
        dessinateurs = db.retrieve(Dessinateur)
        return _dessinateur_list.render_unicode(dessinateurs=dessinateurs)

    @cherrypy.expose
    def dessinateur_new(self):
        return _dessinateur_new.render_unicode()

    @cherrypy.expose
    def dessinateur_add(self, dessinateur):
        db = Database()
        d = Dessinateur(dessinateur)
        db.create(d, Dessinateur)
        raise cherrypy.HTTPRedirect('/dessinateur/')

class EditeurController:
    @cherrypy.expose
    def editeur_list(self):
        db = Database()
        editeurs = db.retrieve(Editeur)
        return _editeur_list.render_unicode(editeurs=editeurs)

    @cherrypy.expose
    def editeur_new(self):
        return _editeur_new.render_unicode()

    @cherrypy.expose
    def editeur_add(self, editeur):
        db = Database()
        e = Editeur(editeur)
        db.create(e, Editeur)
        raise cherrypy.HTTPRedirect('/editeur/')

class GenreController:
    @cherrypy.expose
    def genre_list(self):
        db = Database()
        genres = db.retrieve(Genre)
        return _genre_list.render_unicode(genres=genres)

    @cherrypy.expose
    def genre_new(self):
        return _genre_new.render_unicode()

    @cherrypy.expose
    def genre_add(self, genre):
        db = Database()
        g = Genre(genre)
        db.create(g, Genre)
        raise cherrypy.HTTPRedirect('/genre/')

class SearchController:
    @cherrypy.expose
    def search(self, query):
        db = Database()
        mangas, editeurs, scenaristes, dessinateurs, genres = db.search(query)
        return _search.render_unicode(
            mangas=mangas,
            editeurs=editeurs,
            scenaristes=scenaristes,
            dessinateurs=dessinateurs,
            genres=genres
        )


if __name__ == '__main__':
    global_conf = {
        'global': {'autoreload.on': False,
                   'server.socket_host': '127.0.0.1',
                   'server.protocol_version': 'HTTP/1.1',
                   'server.thread_pool': 5,
                   'tools.encode.encoding': "Utf-8",
                   'environment': 'production',
                   'log.error_file': 'site.log',
                   'log.screen': True}}
    cherrypy.config.update(global_conf)
    app = App()
    d = cherrypy.dispatch.RoutesDispatcher()
    d.connect('default_route', '/', controller=app, action='index')
    d.connect('collection', '/collection/', controller=app, action='collection')
    d.connect('shopping_list', '/shopping_list/', controller=app, action='shopping_list')

    d.connect('manga_list', '/manga/', controller=MangaController, action="manga_list")
    d.connect('manga_new', '/manga/new/', controller=MangaController, action="manga_new")
    d.connect('manga_add', '/manga/add/', controller=MangaController, action="manga_add")
    d.connect('manga_detail', '/manga/:id/', controller=MangaController, action='manga_detail')
    d.connect('manga_delete', '/manga/delete/:id/', controller=MangaController, action='manga_delete')

    d.connect('tome_new', '/tome/new/', controller=TomeController, action="tome_new")
    d.connect('tome_add', '/tome/add/', controller=TomeController, action="tome_add")
    d.connect('tome_detail', '/manga/:id_manga/tome/:id_tome/', controller=TomeController, action='tome_detail')
    d.connect('tome_delete', '/manga/:id_manga/tome/delete/:id_tome', controller=TomeController, action='tome_delete')
    d.connect('tome_buy', '/manga/:id_manga/tome/buy/:id_tome', controller=TomeController, action='tome_buy')
    d.connect('tome_sell', '/manga/:id_manga/tome/sell/:id_tome', controller=TomeController, action='tome_sell')
    d.connect('tome_cart', '/manga/:id_manga/tome/cart/:id_tome', controller=TomeController, action='tome_cart')

    d.connect('scenariste_list','/scenariste/', controller=ScenaristeController, action="scenariste_list")
    d.connect('scenariste_new','/scenariste/new/', controller=ScenaristeController, action="scenariste_new")
    d.connect('scenariste_add','/scenariste/add/', controller=ScenaristeController, action="scenariste_add")

    d.connect('dessinateur_list','/dessinateur/', controller=DessinateurController, action="dessinateur_list")
    d.connect('dessinateur_new','/dessinateur/new/', controller=DessinateurController, action="dessinateur_new")
    d.connect('dessinateur_add','/dessinateur/add/', controller=DessinateurController, action="dessinateur_add")

    d.connect('editeur_list','/editeur/', controller=EditeurController, action="editeur_list")
    d.connect('editeur_new','/editeur/new/', controller=EditeurController, action="editeur_new")
    d.connect('editeur_add','/editeur/add/', controller=EditeurController, action="editeur_add")

    d.connect('genre_list','/genre/', controller=GenreController, action="genre_list")
    d.connect('genre_new','/genre/new/', controller=GenreController, action="genre_new")
    d.connect('genre_add','/genre/add/', controller=GenreController, action="genre_add")

    d.connect('search', '/search/', controller=SearchController, action="search")

    conf_appli = {
        '/': {'request.dispatch': d},
        '/View': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(_curdir, 'View')},
        '/View/templates': {'tools.staticdir.on': True, 'tools.staticdir.dir': myTemplatesDir},
        '/View/tmp/mako_modules': {'tools.staticdir.on': True, 'tools.staticdir.dir': myModulesDir},
        '/View/css': {
            'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(_curdir, 'View/css'),
            'tools.staticdir.content_types': {'css': 'text/css'}
        },
        '/View/images': {
            'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(_curdir, 'View/images'),
            'tools.staticdir.content_types': {'jpg': 'image/jpg'}
        },
        '/View/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(_curdir, 'View/js'),
            'tools.staticdir.content_types': {'js': 'application/javascript'}
        }}

    cherrypy.quickstart(app, config=conf_appli)
