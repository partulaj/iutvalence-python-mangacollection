# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463637606.704917
_enable_loop = True
_template_filename = 'G:/public_html/iutvalence-python-mangacollection/View/template/no_category.html'
_template_uri = 'no_category.html'
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
        __M_writer('\r\n<div class="container">\r\n')
        for manga in mangas:
            __M_writer('    <div class="row">\r\n')
            for tome in manga.tomes:
                if tome.a_acheter != True and tome.possede != True:
                    __M_writer('        <div class="col-xs-6 col-md-3">\r\n            <a href="/manga/')
                    __M_writer(str(manga.id))
                    __M_writer('/tome/')
                    __M_writer(str(tome.numero))
                    __M_writer('/" class="thumbnail"\r\n               style="background: url(')
                    __M_writer(str(tome.couverture))
                    __M_writer(') no-repeat;background-size:100%, 100%;height:300px;">\r\n            </a>\r\n        </div>\r\n')
            __M_writer('    </div>\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "G:/public_html/iutvalence-python-mangacollection/View/template/no_category.html", "line_map": {"64": 16, "65": 18, "35": 2, "71": 65, "45": 3, "27": 0, "52": 3, "53": 5, "54": 6, "55": 7, "56": 8, "57": 9, "58": 10, "59": 10, "60": 10, "61": 10, "62": 11, "63": 11}, "uri": "no_category.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
