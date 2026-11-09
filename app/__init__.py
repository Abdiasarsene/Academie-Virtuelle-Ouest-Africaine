"""Fabrique de l'application Flask.

Chaque future fonctionnalité (comptes, cours, paiement, certificats…)
sera ajoutée sous forme de Blueprint dans app/routes/ puis enregistrée ici.
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    # Futurs modules :
    # from .routes.auth import auth_bp
    # app.register_blueprint(auth_bp, url_prefix="/compte")

    return app
