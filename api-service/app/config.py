class BaseConfig:
    DEBUG = False
    LOG_LEVEL = "INFO"
    PORT = 5000

class DevConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = "DEBUG"

class ProdConfig(BaseConfig):
    DEBUG = False
    LOG_LEVEL = "WARNING"

config_map = {
    "dev": DevConfig,
    "prod": ProdConfig,
}