import os


class Config:
    def __init__(self):
        self.mqtt = MQTTConfig()


class MQTTConfig:
    """
    I have properties which return
    configuration for the MQTT
    communication :D
    """

    @property
    def host(self):
        return 'localhost'

    @property
    def port(self):
        return int(_getenv('MQTT_PORT'))


def _getenv(name):
    return os.environ[name]


config = Config()
