# -*- coding: utf-8 -*-
# from odoo import http


# class Cafe(http.Controller):
#     @http.route('/cafe/cafe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cafe/cafe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cafe.listing', {
#             'root': '/cafe/cafe',
#             'objects': http.request.env['cafe.cafe'].search([]),
#         })

#     @http.route('/cafe/cafe/objects/<model("cafe.cafe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cafe.object', {
#             'object': obj
#         })
