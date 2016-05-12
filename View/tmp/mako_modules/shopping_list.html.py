# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463053281.546996
_enable_loop = True
_template_filename = 'G:\\public_html\\iutvalence-python-mangacollection\\View/template/shopping_list.html'
_template_uri = 'shopping_list.html'
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
        total = context.get('total', UNDEFINED)
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
        total = context.get('total', UNDEFINED)
        def container():
            return render_container(context)
        mangas = context.get('mangas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <div class="row">\r\n        <div class="thumbnail col-xs-12 col-md-4 col-md-offset-4">\r\n            <div class="caption text-center">\r\n                <h3>Total du panier</h3>\r\n                <h1>')
        __M_writer(str(total))
        __M_writer(' €</h1>\r\n                <p><a href="/shopping_list/comfirm/" class="btn btn-primary" role="button">Valider le panier</a></p>\r\n            </div>\r\n        </div>\r\n    </div>\r\n')
        for manga in mangas:
            __M_writer('    <div class="row">\r\n')
            for tome in manga.tomes:
                if tome.a_acheter == True:
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
{"uri": "shopping_list.html", "source_encoding": "utf-8", "line_map": {"64": 19, "65": 20, "66": 20, "35": 2, "68": 27, "74": 68, "45": 3, "61": 19, "67": 25, "53": 3, "54": 9, "55": 9, "56": 14, "57": 15, "58": 16, "59": 17, "60": 18, "26": 0, "62": 19, "63": 19}, "filename": "G:\\public_html\\iutvalence-python-mangacollection\\View/template/shopping_list.html"}
__M_END_METADATA
"""
