# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462628715.873544
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
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
        scenaristes = context.get('scenaristes', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
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
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
        scenaristes = context.get('scenaristes', UNDEFINED)
        def container():
            return render_container(context)
        genres = context.get('genres', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<form method="post" action="/manga/add/">\r\n    <input type="text" name="titre">\r\n    <textarea name="description"></textarea>\r\n    <select name="scenariste">\r\n')
        for scenariste in scenaristes:
            __M_writer('        <option value="')
            __M_writer(str(scenariste.scenariste))
            __M_writer('">')
            __M_writer(str(scenariste.scenariste))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="dessinateur">\r\n')
        for dessinateur in dessinateurs:
            __M_writer('        <option value="')
            __M_writer(str(dessinateur.dessinateur))
            __M_writer('">')
            __M_writer(str(dessinateur.dessinateur))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="editeur">\r\n')
        for editeur in editeurs:
            __M_writer('        <option value="')
            __M_writer(str(editeur.editeur))
            __M_writer('">')
            __M_writer(str(editeur.editeur))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="statut">\r\n        <option value="En cours">En cours</option>\r\n        <option value="En pause">En pause</option>\r\n        <option value="Terminé">Terminé</option>\r\n    </select>\r\n    <select name="genre">\r\n')
        for genre in genres:
            __M_writer('        <option value="')
            __M_writer(str(genre.genre))
            __M_writer('">')
            __M_writer(str(genre.genre))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <input type="submit" value="Ajouter ce manga">\r\n</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 9, "65": 11, "66": 13, "67": 14, "68": 14, "69": 14, "70": 14, "71": 14, "72": 16, "73": 18, "74": 19, "75": 19, "76": 19, "77": 19, "78": 19, "79": 21, "80": 28, "81": 29, "82": 29, "83": 29, "84": 29, "85": 29, "86": 31, "27": 0, "92": 86, "38": 2, "48": 3, "58": 3, "59": 8, "60": 9, "61": 9, "62": 9, "63": 9}, "uri": "manga_new.html", "filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/manga_new.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
