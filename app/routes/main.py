"""Routes publiques : page d'accueil et petite API du mini-quiz."""
from flask import Blueprint, jsonify, render_template, request

from .. import data

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template(
        "home.html",
        site=data.SITE,
        nav=data.NAV,
        hero=data.HERO,
        parcours=data.PARCOURS_UNE,
        catalogue=data.CATALOGUE,
        methode=data.METHODE,
        quiz=data.QUIZ,
        footer=data.FOOTER,
    )


@main_bp.post("/api/quiz/verifier")
def verifier_quiz():
    """Vérifie la réponse côté serveur (la bonne réponse n'est jamais envoyée au navigateur)."""
    choix = (request.get_json(silent=True) or {}).get("reponse")
    quiz = data.QUIZ
    if choix not in {o["id"] for o in quiz["options"]}:
        return jsonify(statut="vide", message=quiz["retour_vide"]), 400
    ok = choix == quiz["bonne_reponse"]
    return jsonify(statut="ok" if ok else "ko",
                   message=quiz["retour_ok"] if ok else quiz["retour_ko"])
