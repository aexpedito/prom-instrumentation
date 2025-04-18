from app.metrics import bp_metrics
from flask import Response
import os
import subprocess
from pathlib import Path
import logging
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

logging = logging.getLogger("applicationLogger")

@bp_metrics.route('/metrics')
def metrics():
    logging.info('### Metrics route')
    return Response(generate_latest(),mimetype=CONTENT_TYPE_LATEST)
