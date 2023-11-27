from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        # Ele deve retornar um novo dicionário contendo os atributos name e acronym.
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"],
        }
    