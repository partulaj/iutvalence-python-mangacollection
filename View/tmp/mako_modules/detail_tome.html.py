# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462205650.967347
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/detail_tome.html'
_template_uri = 'detail_tome.html'
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
        manga = context.get('manga', UNDEFINED)
        tome = context.get('tome', UNDEFINED)
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
        manga = context.get('manga', UNDEFINED)
        tome = context.get('tome', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<section>\r\n    <article>\r\n        <h1>')
        __M_writer(str(manga.titre))
        __M_writer(' - Tome ')
        __M_writer(str(tome.numero))
        __M_writer('</h1>\r\n        <a href="/manga/')
        __M_writer(str(manga.id))
        __M_writer('/tome/')
        __M_writer(str(tome.numero))
        __M_writer('/delete/"><h2>Delete</h2></a>\r\n    </article>\r\n    <article>\r\n    </article>\r\n</section>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "detail_tome.html", "line_map": {"68": 62, "27": 0, "36": 1, "46": 2, "54": 2, "55": 5, "56": 5, "57": 5, "58": 5, "59": 6, "60": 6, "61": 6, "62": 6}, "source_encoding": "ascii", "filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/detail_tome.html"}
__M_END_METADATA
"""
