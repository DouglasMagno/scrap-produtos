import os


class FORMATS:
    """
    constant format's used in solution
    """

    class DATE:
        EN = ['%Y{sep}%m{sep}%d', '%y{sep}%m{sep}%d']
        BR = ['%d{sep}%m{sep}%Y', '%d{sep}%m{sep}%y']


class ENV:
    """
    all environment variables
    """

    ENV = os.getenv('ENV', 'dev')
    DEBUG_FLASK = str(os.getenv('FLASK_DEBUG', 'false')).lower() in ['true', '1']
    SOLUTION = os.getenv('SOLUTION', 'scrape-produtos')
    MONGO_URL = os.getenv('MONGO_URL') or 'mongodb://localhost:27017'
    MONGO_DB = os.getenv('MONGO_DB') or os.getenv('SOLUTION') or 'peter'
    FLASK_HOST = os.getenv('FLASK_HOST') or '0.0.0.0'
    FLASK_PORT = os.getenv('FLASK_PORT') or '5000'

    @staticmethod
    def to_dict() -> dict:
        """
        transform ENV class into a dict
        """
        return {k: v for k, v in vars(ENV).items()
                if not '__' in k and k != 'to_dict'}
