# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1461680107.396816
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/new.html'
_template_uri = 'new.html'
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
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        genres = context.get('genres', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
        scenaristes = context.get('scenaristes', UNDEFINED)
        statuts = context.get('statuts', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
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
        dessinateurs = context.get('dessinateurs', UNDEFINED)
        genres = context.get('genres', UNDEFINED)
        def container():
            return render_container(context)
        scenaristes = context.get('scenaristes', UNDEFINED)
        statuts = context.get('statuts', UNDEFINED)
        editeurs = context.get('editeurs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<form>\r\n    <input type="text" name="manga">\r\n    <textarea name="description"></textarea>\r\n    <select name="scenariste">\r\n')
        for scenariste in scenaristes:
            __M_writer('        <option value="')
            __M_writer(str(scenariste.id))
            __M_writer('">')
            __M_writer(str(scenariste.scenariste))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="dessinateur">\r\n')
        for dessinateur in dessinateurs:
            __M_writer('        <option value="')
            __M_writer(str(dessinateur.id))
            __M_writer('">')
            __M_writer(str(dessinateur.dessinateur))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="editeur">\r\n')
        for editeur in editeurs:
            __M_writer('        <option value="')
            __M_writer(str(editeur.id))
            __M_writer('">')
            __M_writer(str(editeur.editeur))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="statut">\r\n')
        for statut in statuts:
            __M_writer('        <option value="')
            __M_writer(str(statut.id))
            __M_writer('">')
            __M_writer(str(statut.statut))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <select name="genre">\r\n')
        for genre in genres:
            __M_writer('        <option value="')
            __M_writer(str(genre.id))
            __M_writer('">')
            __M_writer(str(genre.genre))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "new.html", "filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/new.html", "line_map": {"64": 8, "65": 8, "66": 8, "67": 10, "68": 12, "69": 13, "70": 13, "71": 13, "72": 13, "73": 13, "74": 15, "75": 17, "76": 18, "77": 18, "78": 18, "79": 18, "80": 18, "81": 20, "82": 22, "83": 23, "84": 23, "85": 23, "86": 23, "87": 23, "88": 25, "89": 27, "90": 28, "27": 0, "92": 28, "93": 28, "94": 28, "95": 30, "91": 28, "101": 95, "39": 1, "49": 2, "60": 2, "61": 7, "62": 8, "63": 8}, "source_encoding": "ascii"}
__M_END_METADATA
"""
