from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        # deve retornar um novo dict contendo os atributos name e acronym.
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"],
        }

    @classmethod
    def list_dicts(cls):
        dict_list = []
        for language in cls.find():
            dict_list.append(language.to_dict())

        return dict_list
