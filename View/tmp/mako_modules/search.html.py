# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463637606.782917
_enable_loop = True
_template_filename = 'G:/public_html/iutvalence-python-mangacollection/View/template/search.html'
_template_uri = 'search.html'
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
        scenaristes = context.get('scenaristes', UNDEFINED)
        genres = context.get('genres', UNDEFINED)
        mangas = context.get('mangas', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        len = context.get('len', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
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
        scenaristes = context.get('scenaristes', UNDEFINED)
        genres = context.get('genres', UNDEFINED)
        mangas = context.get('mangas', UNDEFINED)
        def container():
            return render_container(context)
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        len = context.get('len', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <ul class="nav nav-tabs" role="tablist">\r\n        <li role="presentation" class="active"><a href="#mangas" aria-controls="mangas" role="tab"\r\n                                                  data-toggle="tab">Mangas</a></li>\r\n        <li role="presentation"><a href="#editeurs" aria-controls="editeurs" role="tab" data-toggle="tab">Editeurs</a>\r\n        </li>\r\n        <li role="presentation"><a href="#scenaristes" aria-controls="scenaristes" role="tab" data-toggle="tab">Scénaristes</a>\r\n        </li>\r\n        <li role="presentation"><a href="#dessinateurs" aria-controls="dessinateurs" role="tab" data-toggle="tab">Dessinateurs</a>\r\n        </li>\r\n        <li role="presentation"><a href="#genres" aria-controls="genres" role="tab" data-toggle="tab">Genres</a>\r\n        </li>\r\n    </ul>\r\n\r\n    <!-- Tab panes -->\r\n    <div class="tab-content">\r\n        <div role="tabpanel" class="tab-pane active" id="mangas">\r\n')
        for manga in mangas:
            __M_writer('            <a href="/manga/')
            __M_writer(str(manga.id))
            __M_writer('/" class="list-group-item">\r\n                <div class="row">\r\n                    <h4 class="list-group-item-heading col-lg-3">')
            __M_writer(str(manga.titre))
            __M_writer('</h4>\r\n                    <p class="list-group-item-text col-lg-2">\r\n                        ')
            __M_writer(str(manga.editeur))
            __M_writer('\r\n                    </p>\r\n                    <p class="list-group-item-text col-lg-2">\r\n                        ')
            __M_writer(str(manga.genre))
            __M_writer('\r\n                    </p>\r\n                    <p class="list-group-item-text col-lg-3">\r\n')
            if manga.dessinateur==manga.scenariste:
                __M_writer('                        ')
                __M_writer(str(manga.dessinateur))
                __M_writer('\r\n')
            else:
                __M_writer('                        ')
                __M_writer(str(manga.dessinateur))
                __M_writer(' / ')
                __M_writer(str(manga.scenariste))
                __M_writer('\r\n')
            __M_writer('                    </p>\r\n                    <p class="list-group-item-text col-lg-2">\r\n                        ')
            t = len(manga.tomes) 
            
            __M_writer('\r\n                        ')
            __M_writer(str(t))
            __M_writer(' tomes\r\n                    </p>\r\n                </div>\r\n            </a>\r\n')
        __M_writer('        </div>\r\n        <div role="tabpanel" class="tab-pane" id="editeurs">\r\n            <div class="list-group">\r\n')
        for editeur in editeurs:
            __M_writer('                <div class="list-group-item" role="button">\r\n                    <h4 class="list-group-item-heading">')
            __M_writer(str(editeur.editeur))
            __M_writer('</h4>\r\n                    <p class="list-group-item-text">\r\n\r\n                    </p>\r\n                </div>\r\n')
        __M_writer('            </div>\r\n        </div>\r\n        <div role="tabpanel" class="tab-pane" id="scenaristes">\r\n            <div class="list-group">\r\n')
        for scenariste in scenaristes:
            __M_writer('                <div class="list-group-item" role="button">\r\n                    <h4 class="list-group-item-heading">')
            __M_writer(str(scenariste.scenariste))
            __M_writer('</h4>\r\n                    <p class="list-group-item-text">\r\n\r\n                    </p>\r\n                </div>\r\n')
        __M_writer('            </div>\r\n        </div>\r\n        <div role="tabpanel" class="tab-pane" id="dessinateurs">\r\n            <div class="list-group">\r\n')
        for dessinateur in dessinateurs:
            __M_writer('                <div class="list-group-item" role="button">\r\n                    <h4 class="list-group-item-heading">')
            __M_writer(str(dessinateur.dessinateur))
            __M_writer('</h4>\r\n                    <p class="list-group-item-text">\r\n\r\n                    </p>\r\n                </div>\r\n')
        __M_writer('            </div>\r\n        </div>\r\n        <div role="tabpanel" class="tab-pane" id="genres">\r\n            <div class="list-group">\r\n')
        for genre in genres:
            __M_writer('                <div class="list-group-item" role="button">\r\n                    <h4 class="list-group-item-heading">')
            __M_writer(str(genre.genre))
            __M_writer('</h4>\r\n                    <p class="list-group-item-text">\r\n\r\n                    </p>\r\n                </div>\r\n')
        __M_writer('            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "G:/public_html/iutvalence-python-mangacollection/View/template/search.html", "line_map": {"27": 0, "40": 2, "50": 3, "62": 3, "63": 21, "64": 22, "65": 22, "66": 22, "67": 24, "68": 24, "69": 26, "70": 26, "71": 29, "72": 29, "73": 32, "74": 33, "75": 33, "76": 33, "77": 34, "78": 35, "79": 35, "80": 35, "81": 35, "82": 35, "83": 37, "84": 39, "86": 39, "87": 40, "88": 40, "89": 45, "90": 48, "91": 49, "92": 50, "93": 50, "94": 56, "95": 60, "96": 61, "97": 62, "98": 62, "99": 68, "100": 72, "101": 73, "102": 74, "103": 74, "104": 80, "105": 84, "106": 85, "107": 86, "108": 86, "109": 92, "115": 109}, "uri": "search.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
