# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463637606.911917
_enable_loop = True
_template_filename = 'G:/public_html/iutvalence-python-mangacollection/View/template/manga_detail.html'
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
        range = context.get('range', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        commentaire = context.get('commentaire', UNDEFINED)
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
        range = context.get('range', UNDEFINED)
        def container():
            return render_container(context)
        len = context.get('len', UNDEFINED)
        commentaire = context.get('commentaire', UNDEFINED)
        manga = context.get('manga', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<section>\r\n    <div class="container">\r\n        <div class="row">\r\n            <div class="col-xs-12">\r\n                <div class="thumbnail">\r\n                    <div class="caption">\r\n                        <h3>')
        __M_writer(str(manga.titre))
        __M_writer('</h3>\r\n                        <h4>Par\r\n')
        if manga.dessinateur==manga.scenariste:
            __M_writer('                            ')
            __M_writer(str(manga.dessinateur))
            __M_writer('\r\n')
        else:
            __M_writer('                            ')
            __M_writer(str(manga.dessinateur))
            __M_writer(' / ')
            __M_writer(str(manga.scenariste))
            __M_writer('\r\n')
        __M_writer('                            - ')
        __M_writer(str(manga.genre))
        __M_writer(' - ')
        __M_writer(str(manga.statut))
        __M_writer('\r\n                        </h4>\r\n                        <p>')
        __M_writer(str(manga.description))
        __M_writer('</p>\r\n\r\n                        <button type="button" class="btn btn-danger" data-toggle="modal"\r\n                                data-target="#myModal">Supprimer\r\n                        </button>\r\n                        <div class="btn-group">\r\n                            <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown"\r\n                                    aria-haspopup="true" aria-expanded="false">\r\n                                Statut <span class="caret"></span>\r\n                            </button>\r\n                            <ul class="dropdown-menu">\r\n                                <li><a href="/manga/')
        __M_writer(str(manga.id))
        __M_writer('/ongoing/">En cours</a></li>\r\n                                <li><a href="/manga/')
        __M_writer(str(manga.id))
        __M_writer('/complete/">Terminé</a></li>\r\n                                <li><a href="/manga/')
        __M_writer(str(manga.id))
        __M_writer('/pause/">En Pause</a></li>\r\n                            </ul>\r\n                        </div>\r\n                        <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\r\n                            <div class="modal-dialog" role="document">\r\n                                <div class="modal-content">\r\n                                    <div class="modal-header">\r\n                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">\r\n                                            <span aria-hidden="true">&times;</span></button>\r\n                                        <h4 class="modal-title" id="myModalLabel">Confirmation</h4>\r\n                                    </div>\r\n                                    <div class="modal-body">\r\n                                        Etes vous sur de vouloir supprimer ce manga ?\r\n                                    </div>\r\n                                    <div class="modal-footer">\r\n                                        <button type="button" class="btn btn-default" data-dismiss="modal">Annuler\r\n                                        </button>\r\n                                        <a href="/manga/delete/')
        __M_writer(str(manga.id))
        __M_writer('/" role="button"\r\n                                           class="btn btn-danger">Supprimer</a>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                        <button type="button" class="btn btn-success" data-toggle="modal"\r\n                                data-target="#myModal2">Commentaire\r\n                        </button>\r\n                        <div class="modal fade" id="myModal2" tabindex="-1" role="dialog"\r\n                             aria-labelledby="myModalLabel">\r\n                            <div class="modal-dialog" role="document">\r\n                                <div class="modal-content">\r\n                                    <form method="post" action="/comment/add/')
        __M_writer(str(manga.id))
        __M_writer('/">\r\n                                        <div class="modal-header">\r\n                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">\r\n                                                <span aria-hidden="true">&times;</span></button>\r\n                                            <h4 class="modal-title" id="myModalLabel2">Commentaire</h4>\r\n                                        </div>\r\n                                        <div class="modal-body">\r\n                                            <div class="form-group">\r\n                                                <label for="titre">Titre</label>\r\n                                                <input type="text" class="form-control" id="titre" name="titre">\r\n                                            </div>\r\n                                            <textarea class="form-control" rows="3" name="commentaire"></textarea>\r\n                                        </div>\r\n                                        <div class="modal-footer">\r\n                                            <button type="button" class="btn btn-default" data-dismiss="modal">Annuler\r\n                                            </button>\r\n                                            <button type="submit" role="button"\r\n                                                    class="btn btn-success">Commenter\r\n                                            </button>\r\n                                        </div>\r\n                                    </form>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div class="row">\r\n            <div class="well">\r\n                <!-- Carousel\r\n                ================================================== -->\r\n                <div id="myCarousel" class="carousel slide">\r\n                    <div class="carousel-inner">\r\n                        ')
        __M_writer('\r\n                        ')

        if len(manga.tomes)>4:
            nb_item = math.ceil(len(manga.tomes)/4)
        elif len(manga.tomes)>0:
            nb_item = 1
        else:
            nb_item = 0
        min=1
        max=5
        
        
        __M_writer('\r\n')
        for i in range(nb_item):
            if i==0:
                __M_writer('                        <div class="item active">\r\n                            <div class="row">\r\n')
                for tome in manga.tomes:
                    if tome.numero in range(min, max):
                        __M_writer('                                <div class="col-xs-6 col-lg-3">\r\n                                    <a href="/manga/')
                        __M_writer(str(manga.id))
                        __M_writer('/tome/')
                        __M_writer(str(tome.numero))
                        __M_writer('/" class="thumbnail"\r\n                                       style="background: url(')
                        __M_writer(str(tome.couverture))
                        __M_writer(') no-repeat;background-size:100%, 100%;height:300px;">\r\n                                    </a>\r\n                                </div>\r\n')
                __M_writer('                                ')

                min+=4
                max+=4
                
                
                __M_writer('\r\n                            </div>\r\n                        </div>\r\n')
            else:
                __M_writer('                        <div class="item">\r\n                            <div class="row">\r\n')
                for tome in manga.tomes:
                    if tome.numero in range(min, max):
                        __M_writer('                                <div class="col-xs-6 col-lg-3">\r\n                                    <a href="/manga/')
                        __M_writer(str(manga.id))
                        __M_writer('/tome/')
                        __M_writer(str(tome.numero))
                        __M_writer('/" class="thumbnail"\r\n                                       style="background: url(')
                        __M_writer(str(tome.couverture))
                        __M_writer(') no-repeat;background-size:100%, 100%;height:300px;">\r\n                                    </a>\r\n                                </div>\r\n')
                __M_writer('                            </div>\r\n                        </div>\r\n')
        __M_writer('                    </div>\r\n                    <a class="left carousel-control" href="#myCarousel" data-slide="prev"><i\r\n                            class="fa fa-chevron-left fa-2x"></i></a>\r\n                    <a class="right carousel-control" href="#myCarousel" data-slide="next"><i\r\n                            class="fa fa-chevron-right fa-2x"></i></a>\r\n                    <ol class="carousel-indicators">\r\n')
        for i in range(nb_item):
            if i==0:
                __M_writer('                        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>\r\n')
            else :
                __M_writer('                        <li data-target="#myCarousel" data-slide-to="')
                __M_writer(str(i))
                __M_writer('"></li>\r\n')
        __M_writer('                    </ol>\r\n                </div><!-- End Carousel -->\r\n            </div><!-- End Well -->\r\n        </div>\r\n')
        if commentaire != None:
            __M_writer('        <div class="row">\r\n            <div class="thumbnail">\r\n                <div class="caption">\r\n                    <h3>')
            __M_writer(str(commentaire.titre))
            __M_writer('</h3>\r\n                    <p>')
            __M_writer(str(commentaire.commentaire))
            __M_writer('</p>\r\n                </div>\r\n            </div>\r\n        </div>\r\n')
        __M_writer('    </div>\r\n</section>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "G:/public_html/iutvalence-python-mangacollection/View/template/manga_detail.html", "line_map": {"128": 132, "129": 132, "130": 132, "131": 133, "132": 133, "133": 138, "134": 142, "135": 148, "136": 149, "137": 150, "138": 151, "139": 152, "140": 152, "141": 152, "142": 155, "143": 159, "16": 96, "145": 163, "146": 163, "147": 164, "148": 164, "149": 169, "155": 149, "29": 0, "40": 2, "50": 3, "60": 3, "61": 10, "62": 10, "63": 12, "64": 13, "65": 13, "66": 13, "67": 14, "68": 15, "69": 15, "70": 15, "71": 15, "72": 15, "73": 17, "74": 17, "75": 17, "76": 17, "77": 17, "78": 19, "79": 19, "80": 30, "81": 30, "82": 31, "83": 31, "84": 32, "85": 32, "86": 49, "87": 49, "88": 62, "89": 62, "90": 96, "91": 97, "144": 160, "102": 106, "103": 107, "104": 108, "105": 109, "106": 111, "107": 112, "108": 113, "109": 114, "110": 114, "111": 114, "112": 114, "113": 115, "114": 115, "115": 120, "116": 120, "121": 123, "122": 126, "123": 127, "124": 129, "125": 130, "126": 131, "127": 132}, "uri": "manga_detail.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
