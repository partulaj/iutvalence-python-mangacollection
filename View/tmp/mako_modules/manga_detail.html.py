# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463000934.499081
_enable_loop = True
_template_filename = 'C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/manga_detail.html'
_template_uri = 'manga_detail.html'
_source_encoding = 'utf-8'
_exports = ['container']


import math 

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
        range = context.get('range', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
        manga = context.get('manga', UNDEFINED)
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
        range = context.get('range', UNDEFINED)
        def container():
            return render_container(context)
        manga = context.get('manga', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<section>\r\n    <div class="container">\r\n        <div class="row">\r\n        <div class="col-xs-12">\r\n            <div class="thumbnail">\r\n                <div class="caption">\r\n                    <h3>')
        __M_writer(str(manga.titre))
        __M_writer(' par\r\n')
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
        __M_writer('                    </h3>\r\n                    <h4>')
        __M_writer(str(manga.genre))
        __M_writer(' €</h4>\r\n                    <p>')
        __M_writer(str(manga.description))
        __M_writer('</p>\r\n\r\n\r\n                    <button type="button" class="btn btn-danger" data-toggle="modal"\r\n                            data-target="#myModal">Supprimer\r\n                    </button>\r\n\r\n                    <!-- Modal -->\r\n                    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\r\n                        <div class="modal-dialog" role="document">\r\n                            <div class="modal-content">\r\n                                <div class="modal-header">\r\n                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">\r\n                                        <span aria-hidden="true">&times;</span></button>\r\n                                    <h4 class="modal-title" id="myModalLabel">Confirmation</h4>\r\n                                </div>\r\n                                <div class="modal-body">\r\n                                    Etes vous sur de vouloir supprimer ce manga ?\r\n                                </div>\r\n                                <div class="modal-footer">\r\n                                    <button type="button" class="btn btn-default" data-dismiss="modal">annuler\r\n                                    </button>\r\n                                    <a href="/manga/delete/')
        __M_writer(str(manga.id))
        __M_writer('/" role="button"\r\n                                       class="btn btn-danger">Supprimer</a>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n                </div>\r\n            </div>\r\n            </div>\r\n        <div class="row">\r\n        <div class="well">\r\n            <!-- Carousel\r\n            ================================================== -->\r\n            <div id="myCarousel" class="carousel slide">\r\n                <div class="carousel-inner">\r\n                    ')
        __M_writer('\r\n                    ')

        if len(manga.tomes)>4:
            nb_item = math.ceil(len(manga.tomes)/4)
        elif len(manga.tomes)>0:
            nb_item = 1
        else:
            nb_item = 0
        print(len(manga.tomes))
        print(nb_item)
        min=1
        max=5
        
        
        __M_writer('\r\n')
        for i in range(nb_item):
            if i==0:
                __M_writer('                    <div class="item active">\r\n                        <div class="row">\r\n')
                for tome in manga.tomes:
                    if tome.numero in range(min, max):
                        __M_writer('                            <div class="col-xs-6 col-lg-3">\r\n                                <a href="/manga/')
                        __M_writer(str(manga.id))
                        __M_writer('/tome/')
                        __M_writer(str(tome.numero))
                        __M_writer('/" class="thumbnail"\r\n                                   style="background: url(')
                        __M_writer(str(tome.couverture))
                        __M_writer(') no-repeat;background-size:100%, 100%;height:300px;">\r\n                                </a>\r\n                            </div>\r\n')
                __M_writer('                            ')

                min+=4
                max+=4
                
                
                __M_writer('\r\n                        </div>\r\n                    </div>\r\n')
            else:
                __M_writer('                    <div class="item">\r\n                        <div class="row">\r\n')
                for tome in manga.tomes:
                    if tome.numero in range(min, max):
                        __M_writer('                            <div class="col-xs-6 col-lg-3">\r\n                                <a href="/manga/')
                        __M_writer(str(manga.id))
                        __M_writer('/tome/')
                        __M_writer(str(tome.numero))
                        __M_writer('/" class="thumbnail"\r\n                                   style="background: url(')
                        __M_writer(str(tome.couverture))
                        __M_writer(') no-repeat;background-size:100%, 100%;height:300px;">\r\n                                </a>\r\n                            </div>\r\n')
                __M_writer('                        </div>\r\n                    </div>\r\n')
        __M_writer('                </div>\r\n                <a class="left carousel-control" href="#myCarousel" data-slide="prev"><i\r\n                        class="fa fa-chevron-left fa-2x"></i></a>\r\n                <a class="right carousel-control" href="#myCarousel" data-slide="next"><i\r\n                        class="fa fa-chevron-right fa-2x"></i></a>\r\n\r\n                <ol class="carousel-indicators">\r\n')
        for i in range(nb_item):
            if i==0:
                __M_writer('                    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>\r\n')
            else :
                __M_writer('                    <li data-target="#myCarousel" data-slide-to="')
                __M_writer(str(i))
                __M_writer('"></li>\r\n')
        __M_writer('                </ol>\r\n            </div><!-- End Carousel -->\r\n        </div><!-- End Well -->\r\n    </div>\r\n    </div>\r\n</section>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "manga_detail.html", "line_map": {"128": 114, "129": 115, "130": 115, "131": 115, "132": 118, "138": 132, "16": 56, "29": 0, "39": 2, "49": 3, "58": 3, "59": 10, "60": 10, "61": 11, "62": 12, "63": 12, "64": 12, "65": 13, "66": 14, "67": 14, "68": 14, "69": 14, "70": 14, "71": 16, "72": 17, "73": 17, "74": 18, "75": 18, "76": 40, "77": 40, "78": 56, "79": 57, "92": 68, "93": 69, "94": 70, "95": 71, "96": 73, "97": 74, "98": 75, "99": 76, "100": 76, "101": 76, "102": 76, "103": 77, "104": 77, "105": 82, "106": 82, "111": 85, "112": 88, "113": 89, "114": 91, "115": 92, "116": 93, "117": 94, "118": 94, "119": 94, "120": 94, "121": 95, "122": 95, "123": 100, "124": 104, "125": 111, "126": 112, "127": 113}, "source_encoding": "utf-8", "filename": "C:/Users/jerem/Documents/Workspace/iutvalence-python-mangacollection/View/template/manga_detail.html"}
__M_END_METADATA
"""
