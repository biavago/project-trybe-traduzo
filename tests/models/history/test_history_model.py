import json
from src.models.history_model import HistoryModel


def test_request_history():
    history_load = json.loads(HistoryModel.list_as_json())

    assert isinstance(history_load, list)

    test_dict = {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    }

    for i, li in enumerate([test_dict]):
        assert '_id' in history_load[i]
        assert li["text_to_translate"] == history_load[i]["text_to_translate"]
        assert li["translate_from"] == history_load[i]["translate_from"]
        assert li["translate_to"] == history_load[i]["translate_to"]
