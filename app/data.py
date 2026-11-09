"""Contenu de la page d'accueil.

Tous les textes viennent du PDF. Ils sont regroupés ici (et non dans le HTML)
pour pouvoir, plus tard, les remplacer par une base de données sans toucher
aux templates.
"""

SITE = {
    "nom": "Académie Virtuelle Ouest-Africaine",
    # "bandeau": "Maquette interactive · Projet de lancement : 8 mars 2027 · Aucune inscription ni paiement réel",
}

NAV = [
    {"label": "Nos formations", "ancre": "formations"},
    {"label": "Nos services", "ancre": "approche"},
    {"label": "Notre approche", "ancre": "approche"},
    {"label": "Nous contacter", "ancre": "parcours-une"},
    {"label": "Explorer les certificats ↗", "ancre": "certificats"},
]

HERO = {
    "eyebrow": "Banque & Finance · Espace UMOA",
    "titre_1": "Votre expertise.",
    "titre_2": "Votre avenir.",
    "titre_accent": "Votre certification.",
    "texte": ("Développez vos compétences dans les métiers de la banque et de la finance, "
              "grâce à des parcours en ligne ancrés dans les réalités ouest-africaines."),
    "cta_principal": {"label": "Découvrir les formations →", "ancre": "formations"},
    "cta_secondaire": {"label": "Essayer un quiz", "ancre": "quiz"},
    "mention": "Apprendre à votre rythme · S’exercer sur des cas pratiques · Valider ses acquis",
    "chiffres": [
        {"titre": "100 % en ligne", "texte": "Un format adapté à votre activité"},
        {"titre": "Une approche pratique", "texte": "Cas, exercices et mises en situation"},
        {"titre": "70 % pour réussir", "texte": "Seuil prévu pour l’évaluation finale"},
    ],
}

PARCOURS_UNE = {
    "eyebrow": "Parcours à la une · Proposition",
    "titre": "Analyse financière & décision de crédit",
    "texte": "Du diagnostic financier à la formulation d’une recommandation de crédit argumentée.",
    "etapes": [
        "Comprendre les états financiers",
        "Évaluer la capacité de remboursement",
        "Structurer une décision de financement",
    ],
    "cta": "Consulter le programme →",
}

CATALOGUE = {
    "eyebrow": "Construisez votre parcours",
    "titre": "Une compétence aujourd’hui. De nouvelles perspectives demain.",
    "intro": "Exemples de certificats proposés pour le futur catalogue de l’Académie.",
    "filtres": [
        {"id": "tous", "label": "Tous les parcours"},
        {"id": "credit", "label": "Crédit & analyse"},
        {"id": "risques", "label": "Gestion des risques"},
    ],
    "certificats": [
        {
            "categorie": "credit",
            "domaine": "Analyse financière",
            "icone": "↗",
            "titre": "Analyse financière et décision de crédit",
            "texte": "Analyser une contrepartie, apprécier ses flux et défendre une recommandation.",
            "public": "Analystes · Chargés d’affaires · Décideurs crédit",
            "cta": "Découvrir le programme ↗",
        },
        {
            "categorie": "risques",
            "domaine": "Gestion des risques",
            "icone": "◎",
            "titre": "Maîtrise des risques bancaires",
            "texte": "Identifier, évaluer et suivre les risques pour éclairer les décisions de la banque.",
            "public": "Risk managers · Contrôleurs · Cadres bancaires",
            "cta": "Découvrir le programme ↗",
        },
        {
            "categorie": "recouvrement",
            "domaine": "Recouvrement",
            "icone": "⇄",
            "titre": "Recouvrement et restructuration des créances",
            "texte": "Diagnostiquer un impayé, négocier un plan et suivre les engagements du débiteur.",
            "public": "Chargés de recouvrement · Crédit · Juristes",
            "cta": "Découvrir le programme ↗",
        },
    ],
}

METHODE = {
    "eyebrow": "La méthode de l’Académie",
    "titre": "Apprendre. Pratiquer. Démontrer.",
    "etapes": [
        {"titre": "Choisir son parcours",
         "texte": "Identifier la formation correspondant à son métier et à ses objectifs."},
        {"titre": "Acquérir les méthodes",
         "texte": "Étudier les cours et avancer progressivement, module après module."},
        {"titre": "Se mettre en situation",
         "texte": "Mobiliser les connaissances sur des cas et des exercices pratiques."},
        {"titre": "Valider ses acquis",
         "texte": "Passer l’évaluation finale. Le seuil de réussite prévu est de 70 %."},
    ],
}

QUIZ = {
    "eyebrow": "Un premier pas, dès maintenant",
    "carte_eyebrow": "Question découverte · Analyse crédit",
    "titre": "Testez votre regard d’analyste crédit.",
    "texte": ("Une question d’illustration pour découvrir l’esprit de nos évaluations : "
              "comprendre une situation et choisir une réponse argumentée."),
    "mention": "Ce mini-quiz ne constitue pas un examen certifiant.",
    "question": ("Une entreprise est rentable, mais ses clients la paient de plus en plus tard. "
                 "Quel risque faut-il examiner en priorité ?"),
    "options": [
        {"id": "a", "label": "Le risque de tension de trésorerie"},
        {"id": "b", "label": "La disparition automatique de son bénéfice"},
        {"id": "c", "label": "L’absence de tout risque puisqu’elle est rentable"},
    ],
    "bonne_reponse": "a",
    "bouton": "Vérifier ma réponse",
    # Messages de retour : absents du PDF, ajoutés pour que le quiz fonctionne.
    "retour_ok": "Bonne réponse. Un bénéfice n’est pas de la trésorerie : si les clients paient tard, l’argent rentre plus tard.",
    "retour_ko": "Pas tout à fait. Relisez la situation : la rentabilité n’empêche pas un décalage des encaissements.",
    "retour_vide": "Choisissez une réponse avant de vérifier.",
}

FOOTER = {
    "nom": "Académie Virtuelle Ouest-Africaine",
    "texte": "Formation professionnelle et certification aux métiers de la finance et de la banque.",
    "texte_2": "Catalogue et fonctionnalités présentés à titre de démonstration.",
    "mention": "Les certificats envisagés sont délivrés par l’Académie ; aucune reconnaissance officielle n’est annoncée.",
}
