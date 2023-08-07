from odoo import http
from odoo.http import request
import json


class PunchOutController(http.Controller):
    @http.route('/api/punch_out', type='json', auth='none', methods=['POST'])
    def punch_out(self, **kwargs):
        user_id = kwargs.get('user_id')

        punch_data = {
            'user_id': user_id,
            'punch_type': 'punch_out',
        }

        punch = request.env['punch.management'].sudo().create(punch_data)

        if punch:
            return {'status': 'success', 'punch_id': punch.id}
        else:
            return {'status': 'failure', 'message': 'Failed to punch out'}