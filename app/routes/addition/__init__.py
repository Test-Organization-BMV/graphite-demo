from flask import Blueprint

bp = Blueprint("addition", __name__)

from . import views
