from odoo import http

# Import the controllers
from .controllers.user_login import UserLoginController
from .controllers.punchin import PunchInController
from .controllers.punchout import PunchOutController
from .controllers.check_history import CheckHistoryController


# Define the routing rules
http_routing = http.route

http_routing(
    # User login
    '/api/user_login',
    type='json',
    auth='none',
    methods=['POST'],
    csrf=False,
    controller=UserLoginController,
    _route_id='user_login',
)

http_routing(
    # Punch in
    '/api/punch_in',
    type='json',
    auth='none',
    methods=['POST'],
    csrf=False,
    controller=PunchInController,
    _route_id='punch_in',
)

http_routing(
    # Punch out
    '/api/punch_out',
    type='json',
    auth='none',
    methods=['POST'],
    csrf=False,
    controller=PunchOutController,
    _route_id='punch_out',
)

http_routing(
    # Check punch history
    '/api/check_history',
    type='json',
    auth='none',
    methods=['POST'],
    csrf=False,
    controller=CheckHistoryController,
    _route_id='check_history',
)