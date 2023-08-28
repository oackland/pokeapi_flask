#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.


from flask import Blueprint

api = Blueprint('api', __name__, template_folder='api_templates')


@api.route('/')
def index():
	pass
