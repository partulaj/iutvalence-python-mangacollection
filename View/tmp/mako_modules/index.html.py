# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463637606.412917
_enable_loop = True
_template_filename = 'G:/public_html/iutvalence-python-mangacollection/View/template/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = ['chart', 'container']


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
        def chart():
            return render_chart(context._locals(__M_locals))
        def container():
            return render_container(context._locals(__M_locals))
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


def render_chart(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def chart():
            return render_chart(context)
        genres = context.get('genres', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"filename": "G:/public_html/iutvalence-python-mangacollection/View/template/index.html", "line_map": {"64": 18, "65": 18, "66": 20, "67": 22, "68": 23, "69": 23, "70": 23, "71": 25, "72": 55, "73": 56, "74": 56, "75": 56, "76": 58, "77": 60, "78": 61, "79": 61, "80": 61, "81": 63, "87": 3, "27": 0, "93": 3, "99": 93, "38": 2, "43": 12, "53": 13, "61": 13, "62": 17, "63": 18}, "uri": "index.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
