=====================================================================
  AriaBot v1.5 — Guide de l'utilisateur
  Développé par SMaSeR · 2026
=====================================================================


QU'EST-CE QU'ARIABOT ?
────────────────────────
AriaBot est un assistant d'automatisation conçu spécifiquement pour
La Prisión. Il permet d'enregistrer et de rejouer des séquences
d'actions, d'effectuer des clics automatiques, d'éviter la
déconnexion par inactivité (AFK), de surveiller les montées de
niveau et d'accéder aux guides et aux cartes du jeu sans quitter
l'écran.


RECOMMANDATIONS AVANT DE COMMENCER
─────────────────────────────────────
► Lancez le jeu en PLEIN ÉCRAN pour un fonctionnement optimal.
  AriaBot a besoin de voir l'écran correctement pour détecter les
  images et exécuter les actions à la bonne position.

► Si vous laissez le bot fonctionner sans surveillance, IGNOREZ le
  chat du jeu. Les messages d'autres joueurs peuvent déplacer la
  souris ou le clavier et désynchroniser vos séquences.

► Lancez AriaBot en tant qu'Administrateur (l'installateur le fait
  automatiquement). Si les raccourcis ne répondent pas, vérifiez
  que vous avez les droits d'administrateur.


INSTALLATION
─────────────
1. Lancez AriaBot_Setup.exe et suivez l'assistant.
2. Choisissez le dossier d'installation (par défaut dans Program Files).
3. Optionnel : créez un raccourci sur le Bureau et/ou dans le menu Démarrer.
4. Une fois terminé, vous pouvez lancer le programme directement
   depuis l'installateur.

Le programme crée automatiquement dans son dossier d'installation :
  · Secuencias.json  → vos séquences enregistrées
  · hotkeys.json     → votre configuration des raccourcis
  · settings.json    → votre paramètre de langue
  · templates\       → images capturées pour la vérification des séquences
  · changelog.txt    → historique des modifications (téléchargé lors des mises à jour)
  · _update.bat      → fichier temporaire qui apparaît et disparaît pendant
                       les mises à jour automatiques (normal, ne pas supprimer)


INTERFACE PRINCIPALE
─────────────────────
La fenêtre est divisée en deux zones :

  PANNEAU GAUCHE (sidebar)
  · État en temps réel de chaque fonction active.
  · Légende des raccourcis clavier configurés.
  · Accès rapide aux Drapeaux, au Guide et à la Carte.
  · Bouton ⚙ Options pour configurer les raccourcis et la langue.

  PANNEAU DROIT
  · Configuration générale (intervalle d'autoclick, vitesse de la
    souris, mode un cycle, enregistrement).
  · Images sauvegardées → gestion des modèles de reconnaissance.
  · Séquences d'étapes → enregistrer, modifier et exécuter des macros.
  · Journal en temps réel → historique de toutes les actions du programme.


FONCTIONNALITÉS
────────────────

1. GARDE ANTI-NIVEAU (F4 par défaut)
   Surveille le chat du jeu via OCR. Lorsqu'il détecte le message
   "HAS SUBIDO DE NIVEL" (montée de niveau) en jaune, il arrête
   toutes les fonctions actives et ferme le jeu automatiquement avec
   Alt+F4. Cela empêche le personnage de monter de niveau sans
   appliquer les points de constitution, ce qui réduirait ses points
   de vie maximum. Idéal pour le farming sans surveillance.

2. AUTOCLICK CONTINU (F5 par défaut)
   Effectue des clics en continu tant qu'il est actif. Configurez
   l'intervalle dans le champ "Intervalle Autoclick (s)" du panneau
   supérieur. Appuyez à nouveau sur la touche pour l'arrêter.

   VERROUILLER LA SOURIS PENDANT L'AUTOCLICK :
   Activez la case "Bloquer la souris pendant l'Autoclick" dans le
   panneau d'état pour fixer le curseur à la position enregistrée
   pendant que l'autoclick est en marche. Utile lorsque d'autres
   actions système pourraient déplacer le pointeur.

3. BOUCLE ANTI-AFK (F6 par défaut)
   Déplace le personnage de façon aléatoire et périodique pour éviter
   que le jeu vous déconnecte pour inactivité. Activez et oubliez.

4. ENREGISTREMENT DE SÉQUENCES (F7 par défaut)
   · Appuyez sur F7 pour démarrer l'enregistrement.
   · Effectuez les actions que vous souhaitez automatiser (clics,
     touches, attentes, mouvements de souris).
   · Appuyez à nouveau sur F7 pour arrêter l'enregistrement.
   · La séquence est sauvegardée et prête à être exécutée.
   · Vous pouvez avoir plusieurs séquences et basculer entre elles
     via le menu déroulant en haut.
   · Chaque étape peut être modifiée : changer le temps d'attente,
     assigner une image de vérification, réordonner ou supprimer
     des étapes.
   · Vous pouvez ajouter des pauses statiques entre les étapes avec
     le bouton "Ajouter une Pause Statique" situé à côté du bouton
     d'exécution.

5. CAPTURE D'IMAGE (F8 par défaut)
   Sélectionnez une région de l'écran pour la sauvegarder comme modèle.
   Ces images sont utilisées comme conditions de vérification dans les
   étapes des séquences : le bot vérifie que l'image est à l'écran
   avant d'exécuter cette étape. Si elle n'est pas détectée, il peut
   réessayer ou sauter l'étape selon la configuration.
   · Appuyez sur Échap pour annuler la capture sans rien sélectionner.
   · Vous pouvez aussi importer des images PNG externes directement
     depuis le panneau des images sauvegardées, sans capturer l'écran.

6. DRAPEAUX (F9 par défaut)
   Ouvre le Générateur de Drapeaux Maître v6 intégré. Permet de créer
   et personnaliser des drapeaux du jeu avec plus de 500 variantes,
   un éditeur de couleurs caractère par caractère, un assembleur
   pseudo+cadre et l'export direct du code pour le fichier .inf du jeu.

7. GUIDE DE LA PRISON (F10 par défaut)
   Ouvre le guide complet du jeu directement dans AriaBot, sans avoir
   besoin de changer de fenêtre. Inclut les catégories Munitions,
   Cuisine, Chimie, Bijouterie, Compétences, Vêtements, Mécanique,
   Couture, Carlito-Armure et Montée de Niveau.
   Crédits : www.gentelaprision.es

8. CARTE DE LA PRISON (F11 par défaut)
   Ouvre la carte interactive du jeu dans AriaBot avec :
   · Zoom avec la molette de la souris ou les boutons +/−
   · Glisser pour naviguer sur la carte
   · Légende avec toggles pour afficher/masquer les couches d'icônes
   · Bouton CENTRER pour revenir à la vue initiale (120% centré)
   · Clic droit sur la carte → affiche les coordonnées du point
     (utile pour la calibration)

   RECHERCHE DE SALLE :
   · Tapez le nom de n'importe quelle salle dans la barre de recherche
   · La recherche est en temps réel et insensible aux accents
     (sotano = sótano)
   · La carte fait un zoom automatique et se centre sur la salle trouvée
   · S'il y a plusieurs résultats, naviguez avec les boutons ‹ ›
   · Le compteur affiche le nombre de résultats (ex : 1 / 3)
   · Effacez le texte pour revenir à la vue normale

   Crédits : www.gentelaprision.es

9. TOUT ARRÊTER (F12 par défaut)
   Arrête immédiatement toutes les fonctions actives : autoclick, AFK,
   garde, séquences en cours d'exécution. Bouton d'urgence.


CONFIGURATION GÉNÉRALE
───────────────────────
Dans le panneau supérieur droit vous trouverez trois contrôles
indépendants :

  INTERVALLE AUTOCLICK (s)
  Saisissez directement le nombre de secondes entre chaque clic de
  l'autoclick. Appliqué en temps réel sans redémarrage.

  VITESSE DE DÉPLACEMENT DE LA SOURIS DANS LES SÉQUENCES
  Curseur qui contrôle la vitesse de déplacement de la souris pendant
  l'exécution des séquences. Centré par défaut (vitesse standard).
  Déplacez vers la gauche pour aller plus lentement, vers la droite
  pour aller plus vite.

  SÉQUENCE UN CYCLE
  Si coché, la séquence active exécutera un seul cycle complet et
  s'arrêtera automatiquement à la fin. Si décoché, la séquence se
  répète en boucle continue jusqu'à ce que vous l'arrêtiez manuellement.


CONFIGURER LES RACCOURCIS CLAVIER (⚙ Options)
───────────────────────────────────────────────
Vous pouvez changer n'importe quel raccourci par la combinaison de
votre choix :

1. Cliquez sur le bouton ⚙ Options dans le panneau gauche.
2. Cliquez sur le bouton de l'action que vous souhaitez modifier.
3. Appuyez sur la touche ou combinaison souhaitée (Ctrl+J, Alt+F, F2…).
4. En cas de conflit avec une autre action, le programme vous avertira.
5. Cliquez sur "Enregistrer et Appliquer" — les changements sont immédiats.
6. "Restaurer par défaut" remet tout sur F4–F12.

Les touches configurées sont sauvegardées dans hotkeys.json et chargées
automatiquement à chaque démarrage du programme.

IMPORTANT : les touches assignées aux actions d'AriaBot sont exclues
de l'enregistrement dans les séquences, afin de ne pas interférer avec
l'automatisation.


CHANGER DE LANGUE (⚙ Options)
───────────────────────────────
AriaBot est disponible en Espagnol, Anglais, Français et Italien.
Pour changer de langue :

1. Cliquez sur le bouton ⚙ Options dans le panneau gauche.
2. Dans la section LANGUE / LANGUAGE, sélectionnez ES, EN, FR ou IT.
3. Cliquez sur "Enregistrer et Appliquer".
4. Un avis apparaîtra indiquant qu'un redémarrage est nécessaire.
5. Cliquez sur "Redémarrer maintenant" pour appliquer le changement
   immédiatement, ou "Redémarrer plus tard" pour le faire au prochain
   lancement.

La langue choisie est sauvegardée dans settings.json et appliquée
automatiquement à chaque démarrage du programme.


ASSISTANCE TECHNIQUE
─────────────────────
AriaBot inclut un formulaire de contact intégré accessible depuis le
bouton "Assistance Technique" en bas du panneau gauche. Remplissez
votre nom, email et une description du problème et le message sera
envoyé directement au développeur.


PLATEFORME CLOUD
─────────────────
AriaBot inclut une intégration avec un serveur pour partager et
télécharger des séquences avec d'autres joueurs :

· Publier la Séquence → envoie la séquence active au serveur pour
  que d'autres joueurs puissent la télécharger.
· Explorer le Dépôt → télécharge les séquences publiées par d'autres
  utilisateurs et les importe directement dans votre collection.


SÉQUENCES — UTILISATION AVANCÉE
─────────────────────────────────
· Vous pouvez créer autant de séquences que nécessaire avec le bouton "+".
· Chaque séquence est sauvegardée automatiquement à la fermeture du programme.
· Les étapes supportent : clic gauche, clic droit, double clic, appui
  de touche, saisie de texte et attentes temporisées.
· Assigner une image à une étape oblige le bot à vérifier que l'image
  est visible à l'écran avant de l'exécuter.
· Les séquences peuvent être exécutées en boucle continue ou en un seul
  cycle en activant l'option Séquence un cycle.
· Vous pouvez ajouter des pauses statiques entre les étapes depuis le
  bouton situé à côté du bouton d'exécution.
· Vous pouvez importer des images PNG externes dans le panneau des
  modèles sans les capturer depuis l'écran.


FICHIERS ET DOSSIERS CRÉÉS
────────────────────────────
Tous les fichiers sont créés dans le même dossier que le .exe :

  Secuencias.json   → séquences enregistrées (sauvegarde recommandée)
  hotkeys.json      → configuration des raccourcis clavier
  settings.json     → configuration de la langue
  templates\        → images capturées pour la vérification des séquences
  Mapa.png          → image de la carte (mise à jour automatiquement)
  changelog.txt     → créé/mis à jour lors d'une mise à jour
  readme.txt        → guide en espagnol (mis à jour automatiquement)
  readmeFR.txt      → ce guide (mis à jour automatiquement)
  _update.bat       → fichier temporaire pendant les mises à jour
                      (se supprime automatiquement)
  AriaBot.new       → fichier temporaire pendant le téléchargement
                      d'une mise à jour (devient AriaBot.exe à la fin)


MISES À JOUR AUTOMATIQUES
───────────────────────────
AriaBot vérifie au démarrage si une nouvelle version est disponible.
Si c'est le cas, il vous demandera si vous souhaitez mettre à jour.
En acceptant :
  1. Télécharge la nouvelle version en arrière-plan (progression visible
     dans le journal).
  2. Télécharge le changelog, le readme et Mapa.png mis à jour.
  3. Se ferme automatiquement.
  4. Remplace l'exécutable par la nouvelle version.
  5. Ouvre changelog.txt dans le Bloc-notes pour que vous voyiez
     les changements.
Vous n'avez rien d'autre à faire. Vos séquences et votre configuration
sont conservées.


CRÉDITS
────────
Guides et ressources du jeu fournis par :
  www.gentelaprision.es
  — La référence en espagnol pour tout ce qui concerne La Prisión.

=====================================================================
