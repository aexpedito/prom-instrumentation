from flask import Blueprint

bp_health = Blueprint('health', __name__)

from app.health import routes