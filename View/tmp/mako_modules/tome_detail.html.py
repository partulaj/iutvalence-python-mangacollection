# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463637607.585917
_enable_loop = True
_template_filename = 'G:/public_html/iutvalence-python-mangacollection/View/template/tome_detail.html'
_template_uri = 'tome_detail.html'
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
        tome = context.get('tome', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<section>\r\n    <article class="container">\r\n\r\n        <div class="row">\r\n            <div class="col-xs-6 col-lg-3">\r\n                <a href="#" class="thumbnail"\r\n                   style="background: url(')
        __M_writer(str(tome.couverture))
        __M_writer(') no-repeat;background-size:100%, 100%;height:300px;">\r\n                </a>\r\n            </div>\r\n            <div class="col-xs-6 col-lg-9">\r\n                <div class="thumbnail">\r\n                    <div class="caption">\r\n                        <h3>')
        __M_writer(str(tome.manga.titre))
        __M_writer(' - Tome n°')
        __M_writer(str(tome.numero))
        __M_writer('</h3>\r\n                        <h4>')
        __M_writer(str(tome.prix))
        __M_writer(' € - ')
        __M_writer(str(tome.date_parution))
        __M_writer(' -\r\n')
        if tome.lu == True:
            __M_writer('                                Tome lu\r\n')
        __M_writer('                        <p>')
        __M_writer(str(tome.manga.description))
        __M_writer('</p>\r\n                        <p>\r\n                            <a href="/manga/')
        __M_writer(str(tome.manga.id))
        __M_writer('/" class="btn btn-primary" role="button">Fiche Manga</a>\r\n')
        if tome.lu != True:
            __M_writer('                            <a href="/manga/')
            __M_writer(str(tome.manga.id))
            __M_writer('/tome/read/')
            __M_writer(str(tome.numero))
            __M_writer('" class="btn btn-success" role="button">Lu</a>\r\n')
        if tome.possede == True:
            __M_writer('                                <a href="/manga/')
            __M_writer(str(tome.manga.id))
            __M_writer('/tome/sell/')
            __M_writer(str(tome.numero))
            __M_writer('" class="btn btn-warning" role="button">Vendre ce tome</a>\r\n')
        if tome.a_acheter == True:
            __M_writer('                                <a href="/manga/')
            __M_writer(str(tome.manga.id))
            __M_writer('/tome/buy/')
            __M_writer(str(tome.numero))
            __M_writer('" class="btn btn-success" role="button">Valider l\'achat</a>\r\n')
        if tome.a_acheter == False and tome.possede == False:
            __M_writer('                                <a href="/manga/')
            __M_writer(str(tome.manga.id))
            __M_writer('/tome/cart/')
            __M_writer(str(tome.numero))
            __M_writer('" class="btn btn-success" role="button">Ajouter à la shopping list</a>\r\n')
        __M_writer('                            <!-- Button trigger modal -->\r\n                            <button type="button" class="btn btn-danger" data-toggle="modal"\r\n                                    data-target="#myModal">Supprimer\r\n                            </button>\r\n\r\n                            <!-- Modal -->\r\n                        <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\r\n                            <div class="modal-dialog" role="document">\r\n                                <div class="modal-content">\r\n                                    <div class="modal-header">\r\n                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">\r\n                                            <span aria-hidden="true">&times;</span></button>\r\n                                        <h4 class="modal-title" id="myModalLabel">Confirmation</h4>\r\n                                    </div>\r\n                                    <div class="modal-body">\r\n                                        Etes vous sur de vouloir supprimer ce tome ?\r\n                                    </div>\r\n                                    <div class="modal-footer">\r\n                                        <button type="button" class="btn btn-default" data-dismiss="modal">annuler\r\n                                        </button>\r\n                                        <a href="/manga/')
        __M_writer(str(tome.manga.id))
        __M_writer('/tome/delete/')
        __M_writer(str(tome.numero))
        __M_writer('" role="button"\r\n                                           class="btn btn-danger">Supprimer</a>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                        </p>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        </div>\r\n    </article>\r\n</section>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "G:/public_html/iutvalence-python-mangacollection/View/template/tome_detail.html", "line_map": {"27": 0, "35": 2, "45": 3, "52": 3, "53": 10, "54": 10, "55": 16, "56": 16, "57": 16, "58": 16, "59": 17, "60": 17, "61": 17, "62": 17, "63": 18, "64": 19, "65": 21, "66": 21, "67": 21, "68": 23, "69": 23, "70": 24, "71": 25, "72": 25, "73": 25, "74": 25, "75": 25, "76": 27, "77": 28, "78": 28, "79": 28, "80": 28, "81": 28, "82": 30, "83": 31, "84": 31, "85": 31, "86": 31, "87": 31, "88": 33, "89": 34, "90": 34, "91": 34, "92": 34, "93": 34, "94": 36, "95": 56, "96": 56, "97": 56, "98": 56, "104": 98}, "uri": "tome_detail.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
