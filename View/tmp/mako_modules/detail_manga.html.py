# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462216203.09647
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/detail_manga.html'
_template_uri = 'detail_manga.html'
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
        manga = context.get('manga', UNDEFINED)
        genre = context.get('genre', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
        tomes = context.get('tomes', UNDEFINED)
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
        manga = context.get('manga', UNDEFINED)
        genre = context.get('genre', UNDEFINED)
        def container():
            return render_container(context)
        tomes = context.get('tomes', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<section>\r\n    <article>\r\n        <h1>')
        __M_writer(str(manga.titre))
        __M_writer('</h1>\r\n        <a href="/manga/')
        __M_writer(str(manga.id))
        __M_writer('/delete/"><h2>Delete</h2></a>\r\n        <p>\r\n            ')
        __M_writer(str(genre.genre))
        __M_writer('\r\n        </p>\r\n    </article>\r\n    <article>\r\n        <ul>\r\n')
        for tome in tomes:
            if tome.possede == True:
                __M_writer('                <a href="/manga/')
                __M_writer(str(manga.id))
                __M_writer('/tome/')
                __M_writer(str(tome.numero))
                __M_writer('/"><li>')
                __M_writer(str(manga.titre))
                __M_writer(' Tome ')
                __M_writer(str(tome.numero))
                __M_writer('</li>\r\n')
            else:
                __M_writer('                <li style="color:red">')
                __M_writer(str(manga.titre))
                __M_writer(' Tome ')
                __M_writer(str(tome.numero))
                __M_writer('</li>\r\n')
        __M_writer('        </ul>\r\n    </article>\r\n</section>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "detail_manga.html", "filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/detail_manga.html", "line_map": {"64": 14, "65": 15, "66": 15, "67": 15, "68": 15, "69": 15, "70": 15, "71": 15, "72": 15, "73": 15, "74": 16, "75": 17, "76": 17, "77": 17, "78": 17, "79": 17, "80": 20, "86": 80, "27": 0, "37": 1, "47": 2, "56": 2, "57": 5, "58": 5, "59": 6, "60": 6, "61": 8, "62": 8, "63": 13}}
__M_END_METADATA
"""
