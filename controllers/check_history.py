from odoo import http
from odoo.http import request
import json

class CheckHistoryController(http.Controller):
    @http.route('/api/check_history', type='json', auth='none', methods=['POST'])
    def check_history(self, **kwargs):
        user_id = kwargs.get('user_id')

        punches = request.env['punch.management'].sudo().search([('user_id', '=', user_id)])

        if punches:
            punch_list = []
            for punch in punches:
                punch_data = {
                    'id': punch.id,
                    'user_id': punch.user_id.id,
                    'punch_date': punch.punch_date,
                    'punch_type': punch.punch_type,
                }
                punch_list.append(punch_data)

            return {'status': 'success', 'punches': punch_list}
        else:
            return {'status': 'failure', 'message': 'No punch history found'}