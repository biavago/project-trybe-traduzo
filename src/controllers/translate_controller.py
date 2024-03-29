from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
import deep_translator
from models.history_model import HistoryModel

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET"])
def route_get():
    data = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?",
    }
    return render_template("index.html", **data)


@translate_controller.route("/", methods=["POST"])
def route_post():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    translated = deep_translator.GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)
    HistoryModel({
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to
    }).save()
    data = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "translated": translated
    }
    return render_template("index.html", **data)


@translate_controller.route("/reverse", methods=["POST"])
def reverse_post():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    translated = deep_translator.GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)
    data = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": translated,
        "translate_from": translate_to,
        "translate_to": translate_from,
        "translated": text_to_translate
    }
    return render_template("index.html", **data)
