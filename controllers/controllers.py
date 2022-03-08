# -*- coding: utf-8 -*-
# from odoo import http


# class GestionCours(http.Controller):
#     @http.route('/gestion_cours/gestion_cours', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_cours/gestion_cours/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_cours.listing', {
#             'root': '/gestion_cours/gestion_cours',
#             'objects': http.request.env['gestion_cours.gestion_cours'].search([]),
#         })

#     @http.route('/gestion_cours/gestion_cours/objects/<model("gestion_cours.gestion_cours"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_cours.object', {
#             'object': obj
#         })
