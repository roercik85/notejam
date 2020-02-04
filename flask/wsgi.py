from flask.notejam import app as application
from flask.notejam.config import DevelopmentConfig

application.config.from_object(DevelopmentConfig)

if __name__ == '__main__':
    application.run()
