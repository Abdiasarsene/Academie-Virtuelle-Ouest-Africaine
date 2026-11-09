# Académie Virtuelle Ouest-Africaine – page d'accueil

Flask (back-end) + HTML / CSS / JavaScript / Bootstrap 5 (front-end).

## Lancer le site
```bash
python -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate
pip install -r requirements.txt
python run.py                   # puis ouvrir http://127.0.0.1:5000
```

## Structure
```
academie/
├── run.py                      Lance le serveur
├── requirements.txt            Dépendances (Flask)
└── app/
    ├── __init__.py             create_app() : crée l'app et branche les Blueprints
    ├── data.py                 TOUS les textes de la page (extraits du PDF)
    ├── routes/
    │   └── main.py             Routes : "/" (accueil) et "/api/quiz/verifier" (quiz)
    ├── templates/
    │   ├── base.html           Squelette commun (head, Bootstrap, navbar, footer)
    │   ├── home.html           Page d'accueil = assemblage des sections
    │   ├── partials/           Éléments communs à toutes les pages (bandeau, navbar, footer)
    │   └── sections/           Une section de l'accueil par fichier (hero, catalogue, méthode, quiz)
    └── static/
        ├── css/style.css       Couleurs, typographie, responsive (sommaire en tête du fichier)
        ├── js/main.js          Filtres du catalogue, quiz, menu mobile
        └── img/logo-academie.jpeg
```

## Ajouter une fonctionnalité plus tard
1. Créer `app/routes/ma_fonction.py` avec un `Blueprint`.
2. L'enregistrer dans `app/__init__.py` (`app.register_blueprint(...)`).
3. Créer ses templates (ils héritent de `base.html`).
