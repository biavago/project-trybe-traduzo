import json
from src.models.history_model import HistoryModel


def test_request_history():
    history_load = json.loads(HistoryModel.list_as_json())

    assert isinstance(history_load, list)
