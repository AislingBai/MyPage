class Config:
    SECRET_KEY = "YOU-WILL-NEVER-GUESS"

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'default': DevelopmentConfig
}