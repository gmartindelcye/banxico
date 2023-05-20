from dotenv import dotenv_values

values = dotenv_values(".env")


class Config():
    """
    Configure settings class
    """
    def __init__(self):
        self._token = values.get('TOKEN')
        self._url = values.get('URL')
        self._format = values.get('FORMAT')
        self._language = values.get('LANGUAGE')

    @property
    def token(self):
        return self._token

    @property
    def url(self):
        return self._url

    @property
    def format(self):
        return self._format

    @property
    def language(self):
        return self._language