class ProductionConfig:
    """
    Specifies the configuration for production environment.
    """

    def __init__(self):
        self.ENV = "production"
        self.DEBUG = False
        self.PORT = 80
        self.HOST = "0.0.0.0"
