from odoo import http
from odoo.http import request
import json


class UserLoginController(http.Controller):

    @http.route('/api/user_login', type='json', auth='none', methods=['POST'])
    def user_login_handler(self, **kwargs):
        data = json.loads(request.httprequest.data)
        username = data.get('username')
        password = data.get('password')

        # Your logic to authenticate the user and return the response
        # For example, you can check the username and password against the database
        # and return a success or failure response.

        if username == 'your_username' and password == 'your_password':
            return {'success': True, 'message': 'Login successful!'}
        else:
            return {'success': False, 'message': 'Invalid credentials.'}