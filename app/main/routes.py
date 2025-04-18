from app.main import bp
from flask import render_template
import os
import subprocess
from pathlib import Path
import logging
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

logging = logging.getLogger("applicationLogger")

#Cria metrica do prometheus
REQUEST_COUNT = Counter('http_requests_index_total', 'Count all HTTP requests', ['method', 'endpoint'])

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
@bp.route('/index.html', methods=['GET'])
def index():
    logging.info('### Render template: index.html')
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return render_template('main/index.html')
