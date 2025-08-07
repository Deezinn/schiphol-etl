import json

class JsonLoad:
    def __init__(self, url_config_path = 'urls.json') :
        self.__contentJson = None
        self.url_config_path = url_config_path

    def getJsonUrl(self):
        try:
            with open(self.url_config_path, "r") as file:
                self.__contentJson = json.load(file)
                return self.__contentJson
        except Exception as e:
            raise FileExistsError("Erro ao carregar arquivo", e)
