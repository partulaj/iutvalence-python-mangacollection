# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463034462.935126
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = ['container', 'chart']


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
        def chart():
            return render_chart(context._locals(__M_locals))
        genres = context.get('genres', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'container'):
            context['self'].container(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'chart'):
            context['self'].chart(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <div class="ct-chart col-lg-6 col-xs-6" id="genreChart">\r\n        <h3>Nombre de tomes par genre</h3>\r\n    </div>\r\n    <div class="ct-chart col-lg-6 col-xs-6" id="editeurChart">\r\n        <h3>Nombre de tome par editeur</h3>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_chart(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        editeurs = context.get('editeurs', UNDEFINED)
        def chart():
            return render_chart(context)
        genres = context.get('genres', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<script text="javascript/text">\r\nvar data = {\r\n  labels: [\r\n')
        for genre in genres:
            __M_writer("  '")
            __M_writer(str(genre[0]))
            __M_writer("',\r\n")
        __M_writer('  ],\r\n  series: [\r\n')
        for genre in genres:
            __M_writer('  ')
            __M_writer(str(genre[1]))
            __M_writer(',\r\n')
        __M_writer("  ]\r\n};\r\n\r\nvar options = {\r\n  width: 400,\r\n  height: 400,\r\n  labelInterpolationFnc: function(value) {\r\n    return value[0]\r\n  }\r\n};\r\n\r\nvar responsiveOptions = [\r\n  ['screen and (min-width: 640px)', {\r\n    chartPadding: 30,\r\n    labelOffset: 100,\r\n    labelDirection: 'explode',\r\n    labelInterpolationFnc: function(value) {\r\n      return value;\r\n    }\r\n  }],\r\n  ['screen and (min-width: 1024px)', {\r\n    labelOffset: 80,\r\n    chartPadding: 20\r\n  }]\r\n];\r\n\r\nnew Chartist.Pie('#genreChart', data, options, responsiveOptions);\r\n\r\nvar data = {\r\n  labels: [\r\n")
        for editeur in editeurs:
            __M_writer("  '")
            __M_writer(str(editeur[0]))
            __M_writer("',\r\n")
        __M_writer('  ],\r\n  series: [\r\n')
        for editeur in editeurs:
            __M_writer('  ')
            __M_writer(str(editeur[1]))
            __M_writer(',\r\n')
        __M_writer("  ]\r\n};\r\n\r\nnew Chartist.Pie('#editeurChart', data, options, responsiveOptions);\r\n</script>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 13, "73": 13, "74": 17, "75": 18, "76": 18, "77": 18, "78": 20, "79": 22, "80": 23, "81": 23, "82": 23, "83": 25, "84": 55, "85": 56, "86": 56, "87": 56, "88": 58, "89": 60, "90": 61, "27": 0, "92": 61, "93": 63, "91": 61, "38": 2, "43": 12, "99": 93, "53": 3, "59": 3}, "source_encoding": "utf-8", "filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/index.html", "uri": "index.html"}
__M_END_METADATA
"""
