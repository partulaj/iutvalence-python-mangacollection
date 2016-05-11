# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462987177.437513
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/scenariste_list.html'
_template_uri = 'scenariste_list.html'
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
        def container():
            return render_container(context._locals(__M_locals))
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
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <div class="row">\r\n        <div class="panel-heading"></div>\r\n        <div class="list-group">\r\n')
        for scenariste in scenaristes:
            __M_writer('            <div class="list-group-item" role="button">\r\n                <h4 class="list-group-item-heading">')
            __M_writer(str(scenariste.scenariste))
            __M_writer('</h4>\r\n                <p class="list-group-item-text">\r\n                </p>\r\n            </div>\r\n')
        __M_writer('        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 2, "52": 3, "53": 8, "54": 9, "55": 10, "56": 10, "57": 15, "27": 0, "45": 3, "63": 57}, "filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/scenariste_list.html", "uri": "scenariste_list.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
