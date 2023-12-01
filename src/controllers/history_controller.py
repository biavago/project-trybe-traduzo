from models.history_model import HistoryModel
from flask import Blueprint, jsonify

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def route_get_history():
    history = HistoryModel.list_as_json()
    return jsonify(history), 200
