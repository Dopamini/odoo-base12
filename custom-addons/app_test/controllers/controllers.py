# -*- coding: utf-8 -*-
from odoo import http

# class Custom-addons/appTest(http.Controller):
#     @http.route('/custom-addons/app_test/custom-addons/app_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/app_test/custom-addons/app_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons/app_test.listing', {
#             'root': '/custom-addons/app_test/custom-addons/app_test',
#             'objects': http.request.env['custom-addons/app_test.custom-addons/app_test'].search([]),
#         })

#     @http.route('/custom-addons/app_test/custom-addons/app_test/objects/<model("custom-addons/app_test.custom-addons/app_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons/app_test.object', {
#             'object': obj
#         })