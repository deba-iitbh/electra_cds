class DevConfig:
    """
    Specific Configuration for development environment.
    """

    def __init__(self):
        self.ENV = "development"
        self.DEBUG = True
        self.PORT = 5000
        self.HOST = "127.0.0.1"
