# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463053282.236996
_enable_loop = True
_template_filename = 'G:\\public_html\\iutvalence-python-mangacollection\\View/template/tome_new.html'
_template_uri = 'tome_new.html'
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
        mangas = context.get('mangas', UNDEFINED)
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
        mangas = context.get('mangas', UNDEFINED)
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <form action="/tome/add/" method="post">\r\n        <select name="manga_id" class="form-control">\r\n')
        for manga in mangas:
            __M_writer('            <option value="')
            __M_writer(str(manga.id))
            __M_writer('">')
            __M_writer(str(manga.titre))
            __M_writer('</option>\r\n')
        __M_writer('        </select>\r\n        <div class="form-group">\r\n            <label for="numero">Numero :</label>\r\n            <input type="text" class="form-control" id="numero" name="numero" required>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="date_parution">Date de parution :</label>\r\n            <input type="text" class="form-control" id="date_parution" name="date_parution" required>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="prix">Prix :</label>\r\n            <input type="text" class="form-control" id="prix" name="prix" required>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="couverture">Couverture :</label>\r\n            <input type="text" class="form-control" id="couverture" name="couverture" required>\r\n        </div>\r\n        <div class="form-group">\r\n            <label for="date_achat">Date d\'achat :</label>\r\n            <input type="text" class="form-control" id="date_achat" name="date_achat">\r\n        </div>\r\n        <div class="checkbox">\r\n            <label>\r\n                <input type="checkbox" name="possede" value="1"> Je possède ce tome\r\n            </label>\r\n        </div>\r\n        <div class="checkbox">\r\n            <label>\r\n                <input type="checkbox" name="lu" value="1"> J\'ai lu ce tome\r\n            </label>\r\n        </div>\r\n        <div class="checkbox">\r\n            <label>\r\n                <input type="checkbox" name="a_acheter" value="1"> Je dois acheté ce tome\r\n            </label>\r\n        </div>\r\n        <input type="submit" class="btn btn-success">\r\n    </form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "tome_new.html", "source_encoding": "utf-8", "line_map": {"64": 58, "34": 2, "44": 3, "51": 3, "52": 7, "53": 8, "54": 8, "55": 8, "56": 8, "57": 8, "26": 0, "58": 10}, "filename": "G:\\public_html\\iutvalence-python-mangacollection\\View/template/tome_new.html"}
__M_END_METADATA
"""
