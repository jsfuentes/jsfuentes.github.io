import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True

    #Mongoengine Variables
    MONGODB_HOST=os.environ.get('MONGODB_HOST')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
