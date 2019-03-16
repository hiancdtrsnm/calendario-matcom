from flask import Blueprint

api = Blueprint('api', __name__)

from . import course_controller, group_controller, local_controller, resource_controller, \
    tag_controller, user_controller
