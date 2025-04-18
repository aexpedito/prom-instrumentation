from flask import Flask
from logging.config import fileConfig
import logging

def create_app(conf_class=object):
    #Start flask application
    app = Flask(__name__)
    app.config.from_object(conf_class)

    #Register all blueprints with routes
    from app.main import bp as bp_main
    app.register_blueprint(bp_main)

    from app.metrics import bp_metrics
    app.register_blueprint(bp_metrics)

    #configure logging
    dict_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(levelname)s - %(asctime)s - %(message)s'
            },
        },
        'handlers': {
            'default': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'INFO',
                'formatter': 'standard',
                'filename': 'logs/flask.log',
                'maxBytes': 1024,
                'backupCount': 5,
                'encoding': 'utf8'
            },
            "console": {
                "class": "logging.StreamHandler",
                "level": "ERROR",
                "formatter": "standard",
                "stream": "ext://sys.stdout"
            },
            'app': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'INFO',
                'formatter': 'standard',
                'filename': 'logs/app.log',
                'maxBytes': 1024,
                'backupCount': 5,
                'encoding': 'utf8'
            }
        },
        'loggers': {
            'applicationLogger': {
                'handlers': ['app'],
                'level': 'INFO',
                'propagate': False
            },
            '': {
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }
    logging.config.dictConfig(dict_config)
    app.logger.info("#####Started app####")
    return app