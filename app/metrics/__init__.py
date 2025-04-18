from flask import Blueprint

bp_metrics = Blueprint('metrics', __name__)

from app.metrics import routes