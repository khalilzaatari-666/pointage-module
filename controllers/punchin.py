from odoo import http
from odoo.http import request
import json


class PunchInController(http.Controller):
    @http.route('/api/punch_in', type='json', auth='none', methods=['POST'])
    def punch_in(self, **kwargs):
        user_id = kwargs.get('user_id')

        punch_data = {
            'user_id': user_id,
            'punch_type': 'punch_in',
        }

        punch = request.env['punch.management'].sudo().create(punch_data)

        if punch:
            return {'status': 'success', 'punch_id': punch.id}
        else:
            return {'status': 'failure', 'message': 'Failed to punch in'}