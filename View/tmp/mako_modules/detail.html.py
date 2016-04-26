# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1461677991.843799
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/detail.html'
_template_uri = 'detail.html'
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
        def container():
            return render_container(context)
        tomes = context.get('tomes', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<section>\r\n    <article>\r\n        <h1>')
        __M_writer(str(manga.titre))
        __M_writer('</h1>\r\n    </article>\r\n    <article>\r\n        <ul>\r\n')
        for tome in tomes:
            if tome.possede == True:
                __M_writer('                <li>')
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
{"filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/detail.html", "line_map": {"64": 12, "65": 13, "66": 13, "27": 0, "36": 1, "69": 13, "68": 13, "76": 70, "70": 16, "46": 2, "67": 13, "54": 2, "55": 5, "56": 5, "57": 9, "58": 10, "59": 11, "60": 11, "61": 11, "62": 11, "63": 11}, "uri": "detail.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
