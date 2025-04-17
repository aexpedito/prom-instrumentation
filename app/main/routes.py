from app.main import bp
from flask import render_template
import os
import subprocess
from pathlib import Path
import logging

logging = logging.getLogger("applicationLogger")

@bp.route('/')
@bp.route('/index')
@bp.route('/index.html')
def index():
    logging.info('### Render template: index.html')
    return render_template('main/index.html')
