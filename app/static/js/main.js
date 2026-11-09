/* =========================================================
   Académie Virtuelle Ouest-Africaine – JavaScript de la page d'accueil
   1. Filtres du catalogue
   2. Mini-quiz (la vérification se fait côté Flask)
   3. Fermeture du menu mobile après un clic
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {

  /* 1. FILTRES DU CATALOGUE */
  const boutons = document.querySelectorAll(".filtre");
  const cartes = document.querySelectorAll(".carte-col");

  boutons.forEach((bouton) => {
    bouton.addEventListener("click", () => {
      const choix = bouton.dataset.filtre;
      boutons.forEach((b) => {
        const actif = b === bouton;
        b.classList.toggle("actif", actif);
        b.setAttribute("aria-pressed", actif);
      });
      cartes.forEach((carte) => {
        const visible = choix === "tous" || carte.dataset.categorie === choix;
        carte.classList.toggle("cache", !visible);
      });
    });
  });

  /* 2. MINI-QUIZ */
  const form = document.getElementById("quiz-form");
  const retour = document.getElementById("quiz-retour");

  if (form) {
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const choix = form.querySelector('input[name="reponse"]:checked');
      retour.className = "quiz-retour";

      try {
        const reponse = await fetch("/api/quiz/verifier", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ reponse: choix ? choix.value : null }),
        });
        const data = await reponse.json();
        retour.textContent = data.message;
        if (data.statut === "ok" || data.statut === "ko") retour.classList.add(data.statut);
      } catch (erreur) {
        retour.textContent = "Connexion impossible. Réessayez dans un instant.";
      }
    });
  }

  /* 3. MENU MOBILE : se referme quand on choisit une rubrique */
  const menu = document.getElementById("menu");
  document.querySelectorAll("#menu .nav-link").forEach((lien) => {
    lien.addEventListener("click", () => {
      if (menu.classList.contains("show")) bootstrap.Collapse.getInstance(menu).hide();
    });
  });
});
