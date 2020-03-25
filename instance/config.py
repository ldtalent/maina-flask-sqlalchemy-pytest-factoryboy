import os


class Config:
    DEBUG=False
    CSRF_ENABLED=True
    SECRET=os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfig(Config):
    DEBUG=False

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_TEST_URL')
    DEBUG=True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}

