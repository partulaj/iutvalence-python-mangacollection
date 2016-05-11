# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462461182.072107
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/home.html'
_template_uri = 'home.html'
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
        def container():
            return render_container(context._locals(__M_locals))
        mangas = context.get('mangas', UNDEFINED)
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
        mangas = context.get('mangas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="row">\r\n\r\n    <div class="list-group">\r\n')
        for manga in mangas:
            __M_writer('        <a href="/manga/')
            __M_writer(str(manga.id))
            __M_writer('/" class="list-group-item">\r\n            <h4 class="list-group-item-heading">')
            __M_writer(str(manga.titre))
            __M_writer('</h4>\r\n            <p class="list-group-item-text">')
            __M_writer(str(manga.description))
            __M_writer('</p>\r\n        </a>\r\n')
        __M_writer('    </div>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/home.html", "line_map": {"35": 1, "45": 2, "27": 0, "67": 61, "52": 2, "53": 7, "54": 8, "55": 8, "56": 8, "57": 9, "58": 9, "59": 10, "60": 10, "61": 13}, "uri": "home.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
