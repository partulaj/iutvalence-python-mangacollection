# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462205765.705864
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/new.html'
_template_uri = 'new.html'
_source_encoding = 'ascii'
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
        editeurs = context.get('editeurs', UNDEFINED)
        mangas = context.get('mangas', UNDEFINED)
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        scenaristes = context.get('scenaristes', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
        genres = context.get('genres', UNDEFINED)
        statuts = context.get('statuts', UNDEFINED)
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
        editeurs = context.get('editeurs', UNDEFINED)
        mangas = context.get('mangas', UNDEFINED)
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        scenaristes = context.get('scenaristes', UNDEFINED)
        def container():
            return render_container(context)
        genres = context.get('genres', UNDEFINED)
        statuts = context.get('statuts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<form method="post" action="/add/manga/">\r\n    <input type="text" name="titre">\r\n    <textarea name="description"></textarea>\r\n    <select name="scenariste">\r\n')
        for scenariste in scenaristes:
            __M_writer('        <option value="')
            __M_writer(str(scenariste.id))
            __M_writer('">')
            __M_writer(str(scenariste.scenariste))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="dessinateur">\r\n')
        for dessinateur in dessinateurs:
            __M_writer('        <option value="')
            __M_writer(str(dessinateur.id))
            __M_writer('">')
            __M_writer(str(dessinateur.dessinateur))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="editeur">\r\n')
        for editeur in editeurs:
            __M_writer('        <option value="')
            __M_writer(str(editeur.id))
            __M_writer('">')
            __M_writer(str(editeur.editeur))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="statut">\r\n')
        for statut in statuts:
            __M_writer('        <option value="')
            __M_writer(str(statut.id))
            __M_writer('">')
            __M_writer(str(statut.statut))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="genre">\r\n')
        for genre in genres:
            __M_writer('        <option value="')
            __M_writer(str(genre.id))
            __M_writer('">')
            __M_writer(str(genre.genre))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <input type="submit" value="Ajouter ce manga">\r\n</form>\r\n<form method="post" action="/add/tome/">\r\n    <input type="number" name="numero">\r\n    <select name="manga">\r\n')
        for manga in mangas:
            __M_writer('        <option value="')
            __M_writer(str(manga.id))
            __M_writer('">')
            __M_writer(str(manga.titre))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <input type="text" name="date_parution">\r\n    <input type="text" name="date_achat">\r\n    <input type="checkbox" name="possede" value="1">\r\n    <input type="checkbox" name="a_acheter" value="1">\r\n    <input type="checkbox" name="lu" value="1">\r\n    <input type="text" name="prix">\r\n    <input type="text" name="couverture">\r\n    <input type="submit" value="Ajouter ce tome">\r\n</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "40": 1, "50": 2, "62": 2, "63": 7, "64": 8, "65": 8, "66": 8, "67": 8, "68": 8, "69": 10, "70": 12, "71": 13, "72": 13, "73": 13, "74": 13, "75": 13, "76": 15, "77": 17, "78": 18, "79": 18, "80": 18, "81": 18, "82": 18, "83": 20, "84": 22, "85": 23, "86": 23, "87": 23, "88": 23, "89": 23, "90": 25, "91": 27, "92": 28, "93": 28, "94": 28, "95": 28, "96": 28, "97": 30, "98": 36, "99": 37, "100": 37, "101": 37, "102": 37, "103": 37, "104": 39, "110": 104}, "uri": "new.html", "filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/new.html"}
__M_END_METADATA
"""
