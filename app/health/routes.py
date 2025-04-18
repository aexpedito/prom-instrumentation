from app.health import bp_health
import logging

logging = logging.getLogger("applicationLogger")

@bp_health.route('/health', methods=['GET'])
def health():
    logging.info('### Health check ###')
    return 'OK', 200
