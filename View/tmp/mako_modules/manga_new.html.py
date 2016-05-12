# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463041302.373863
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/manga_new.html'
_template_uri = 'manga_new.html'
_source_encoding = 'utf-8'
_exports = ['container']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def container():
            return render_container(context._locals(__M_locals))
        scenaristes = context.get('scenaristes', UNDEFINED)
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
        genres = context.get('genres', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'container'):
            context['self'].container(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def container():
            return render_container(context)
        scenaristes = context.get('scenaristes', UNDEFINED)
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
        genres = context.get('genres', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <form method="post" action="/manga/add/">\r\n\r\n        <div class="form-group">\r\n            <label for="titre">Titre</label>\r\n            <input class="form-control" type="text" name="titre" id="titre" required>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="description">Description</label>\r\n            <textarea class="form-control" name="description" id="description"></textarea>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="scenariste">Scenariste</label>\r\n            <select class="form-control" name="scenariste" id="scenariste"  required>\r\n')
        for scenariste in scenaristes:
            __M_writer('                <option value="')
            __M_writer(str(scenariste.scenariste))
            __M_writer('">')
            __M_writer(str(scenariste.scenariste))
            __M_writer('</option>\r\n')
        __M_writer('            </select>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="dessinateur">Name</label>\r\n            <select class="form-control" name="dessinateur" id="dessinateur" required>\r\n')
        for dessinateur in dessinateurs:
            __M_writer('                <option value="')
            __M_writer(str(dessinateur.dessinateur))
            __M_writer('">')
            __M_writer(str(dessinateur.dessinateur))
            __M_writer('</option>\r\n')
        __M_writer('            </select>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="editeur">Editeur</label>\r\n            <select class="form-control" name="editeur" id="editeur" required>\r\n')
        for editeur in editeurs:
            __M_writer('                <option value="')
            __M_writer(str(editeur.editeur))
            __M_writer('">')
            __M_writer(str(editeur.editeur))
            __M_writer('</option>\r\n')
        __M_writer('            </select>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="statut">Statut</label>\r\n            <select class="form-control" name="statut" id="statut" required>\r\n                <option value="En cours">En cours</option>\r\n                <option value="En pause">En pause</option>\r\n                <option value="Terminé">Terminé</option>\r\n            </select>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="genre">Genre</label>\r\n            <select class="form-control" name="genre" id="genre" required>\r\n')
        for genre in genres:
            __M_writer('                <option value="')
            __M_writer(str(genre.genre))
            __M_writer('">')
            __M_writer(str(genre.genre))
            __M_writer('</option>\r\n')
        __M_writer('            </select>\r\n        </div>\r\n        <input type="submit" class="btn btn-success block-center" value="Ajouter ce manga">\r\n    </form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/manga_new.html", "uri": "manga_new.html", "line_map": {"64": 19, "65": 21, "66": 26, "67": 27, "68": 27, "69": 27, "70": 27, "71": 27, "72": 29, "73": 34, "74": 35, "75": 35, "76": 35, "77": 35, "78": 35, "79": 37, "80": 50, "81": 51, "82": 51, "83": 51, "84": 51, "85": 51, "86": 53, "27": 0, "92": 86, "38": 2, "48": 3, "58": 3, "59": 18, "60": 19, "61": 19, "62": 19, "63": 19}}
__M_END_METADATA
"""
