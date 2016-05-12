# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463053977.610396
_enable_loop = True
_template_filename = 'G:/public_html/iutvalence-python-mangacollection/View/template/base.html'
_template_uri = 'base.html'
_source_encoding = 'utf-8'
_exports = ['chart', 'container']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def container():
            return render_container(context._locals(__M_locals))
        def chart():
            return render_chart(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="fr">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <title>Manga Collection</title>\r\n    <link rel="stylesheet" href="/View/css/bootstrap.min.css">\r\n    <link rel="stylesheet" href="/View/css/font-awesome.min.css">\r\n    <link rel="stylesheet" href="/View/css/chartist.min.css">\r\n    <link rel="stylesheet" href="/View/css/style.css">\r\n</head>\r\n<body>\r\n<nav class="navbar navbar-default">\r\n    <div class="container-fluid">\r\n        <!-- Brand and toggle get grouped for better mobile display -->\r\n        <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"\r\n                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n                <span class="sr-only">Toggle navigation</span>\r\n                <span class="icon-bar"></span>\r\n                <span class="icon-bar"></span>\r\n                <span class="icon-bar"></span>\r\n            </button>\r\n            <a class="navbar-brand" href="/">Manga Collection</a>\r\n        </div>\r\n\r\n        <!-- Collect the nav links, forms, and other content for toggling -->\r\n        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n            <form class="navbar-form navbar-left" role="search" method="post" action="/search/">\r\n                <div class="form-group">\r\n                    <input name="query" type="text" class="form-control" placeholder="Recherche">\r\n                </div>\r\n                <button type="submit" class="btn btn-default">Rechercher</button>\r\n            </form>\r\n            <ul class="nav navbar-nav navbar-right">\r\n                <li><a href="/collection/">Collection</a></li>\r\n                <li><a href="/shopping_list/">Shopping List</a></li>\r\n                <li><a href="/no_category/">Manga sans catégorie</a></li>\r\n                <li class="dropdown">\r\n                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="dropdownMenu2" role="button"\r\n                       aria-haspopup="true"\r\n                       aria-expanded="false">Listes<span class="caret"></span></a>\r\n                    <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">\r\n                        <li><a href="/manga/">Liste des mangas</a></li>\r\n                        <li><a href="/editeur/">Liste des éditeurs</a></li>\r\n                        <li><a href="/dessinateur/">Liste des dessinateurs</a></li>\r\n                        <li><a href="/scenariste/">Liste des scénaristes</a></li>\r\n                        <li><a href="/genre/">Liste des genres</a></li>\r\n                    </ul>\r\n                </li>\r\n                <li class="dropdown">\r\n                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"\r\n                       aria-expanded="false">Nouveau<span class="caret"></span></a>\r\n                    <ul class="dropdown-menu">\r\n                        <li><a href="/manga/new/">Nouveau manga</a></li>\r\n                        <li><a href="/tome/new/">Nouveau tome</a></li>\r\n                        <li><a href="/editeur/new/">Nouvelle éditeur</a></li>\r\n                        <li><a href="/dessinateur/new/">Nouveau dessinateur</a></li>\r\n                        <li><a href="/scenariste/new/">Nouveau scénariste</a></li>\r\n                        <li><a href="/genre/new/">Nouveau genre</a></li>\r\n                    </ul>\r\n                </li>\r\n\r\n            </ul>\r\n        </div><!-- /.navbar-collapse -->\r\n    </div><!-- /.container-fluid -->\r\n</nav>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'container'):
            context['self'].container(**pageargs)
        

        __M_writer('\r\n<script src="/View/js/jquery-1.12.3.min.js"></script>\r\n<script src="/View/js/bootstrap.min.js"></script>\r\n<script src="/View/js/chartist.min.js"></script>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'chart'):
            context['self'].chart(**pageargs)
        

        __M_writer('\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_chart(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def chart():
            return render_chart(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "G:/public_html/iutvalence-python-mangacollection/View/template/base.html", "uri": "base.html", "line_map": {"16": 0, "65": 59, "35": 74, "53": 68, "41": 73, "25": 2, "59": 68, "30": 69, "47": 73}}
__M_END_METADATA
"""
