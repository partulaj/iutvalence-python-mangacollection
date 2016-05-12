# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463053281.691996
_enable_loop = True
_template_filename = 'G:\\public_html\\iutvalence-python-mangacollection\\View/template/manga_list.html'
_template_uri = 'manga_list.html'
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
        len = context.get('len', UNDEFINED)
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
        len = context.get('len', UNDEFINED)
        mangas = context.get('mangas', UNDEFINED)
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <div class="list-group">\r\n')
        for manga in mangas:
            __M_writer('        <a href="/manga/')
            __M_writer(str(manga.id))
            __M_writer('/" class="list-group-item">\r\n            <div class="row">\r\n                <h4 class="list-group-item-heading col-lg-3">')
            __M_writer(str(manga.titre))
            __M_writer('</h4>\r\n                <p class="list-group-item-text col-lg-2">\r\n                    ')
            __M_writer(str(manga.editeur))
            __M_writer('\r\n                </p>\r\n                <p class="list-group-item-text col-lg-2">\r\n                    ')
            __M_writer(str(manga.genre))
            __M_writer('\r\n                </p>\r\n                <p class="list-group-item-text col-lg-3">\r\n')
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
            __M_writer('                </p>\r\n                <p class="list-group-item-text col-lg-2">\r\n                    ')
            t = len(manga.tomes) 
            
            __M_writer('\r\n                    ')
            __M_writer(str(t))
            __M_writer(' tomes\r\n                </p>\r\n            </div>\r\n        </a>\r\n')
        __M_writer('    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "manga_list.html", "source_encoding": "utf-8", "line_map": {"64": 17, "65": 18, "66": 18, "67": 18, "68": 19, "69": 20, "70": 20, "71": 20, "72": 20, "73": 20, "74": 22, "75": 24, "77": 24, "78": 25, "79": 25, "80": 30, "86": 80, "26": 0, "35": 2, "45": 3, "53": 3, "54": 6, "55": 7, "56": 7, "57": 7, "58": 9, "59": 9, "60": 11, "61": 11, "62": 14, "63": 14}, "filename": "G:\\public_html\\iutvalence-python-mangacollection\\View/template/manga_list.html"}
__M_END_METADATA
"""
