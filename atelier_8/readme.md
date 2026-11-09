Atelier 8 – Artem Kharseev

Ce document explique comment installer les ateliers 4-5 (et non l’atelier 7, car le Wild West l’a pris) et comment créer une icône pour cet outil.

L’outil crée un nombre choisi d’objets (cubes, cylindres et sphères) et les place dans la scène de Maya avec une échelle aléatoire.

Étape 1 : Télécharger le script

Option A :

Allez sur https://github.com/artemm999/NAND403_A26_Ateliers.git
Cliquez sur Code > Download ZIP
Option B :

Créez un nouveau dossier à partir de Visual Studio Code
Ouvrez le terminal de Visual Studio Code
Copiez-collez la ligne suivante : git clone https://github.com/artemm999/NAND403_A26_Ateliers.git
Étape 2 : Installer les prérequis

Dirigez Fvous dans le fichier 5_6 du dossier NAND403_A26_Ateliers.
Dans Visual Studio Code, faites Ctrl + Shift + P > Python: Select Interpreter
Dirigez vous vers le fichier Python
Dans les extensions de Visual Studio Code, installez Python – Maya.
Faites un clic droit sur Maya dans votre espace de travail, puis encore un clic droit sur Maya.
Cliquez sur Propriétés
Dans Cible, copiez le lien.
Dans Visual Studio Code, faites Ctrl + Shift + P > Python: Select Interpreter.
Collez le lien dedans.
Étape 3 : Lier Visual Studio Code et Maya

Ouvrez Maya
Dans Visual Studio Code, faites Ctrl + Entrée
Un code Python apparaît en bas à droite de Visual Studio Code. Copiez-le
Dans Maya, ouvrez Windows > General Editors > Script Editor
Dans la section Python, collez le code avec Ctrl + V
Faites Ctrl + Entrée
Retournez dans Visual Studio Code et faites encore Ctrl + Entrée
Le résultat du script apparaît dans Maya
Étape 4 : Créer l’icône dans Maya

En haut à gauche de Maya, cliquez sur l’engrenage
Cliquez sur New Shelf
Donnez un nom à votre shelf, par exemple teste_atelier5-6
Dans le Script Editor, cliquez sur File > Save Script to Shelf
Donnez un nom à votre outil
Une nouvelle icône apparaît dans votre shelf, en haut de Maya
Changer l’image de l’icône :

Faites un clic droit sur le nouvel outil > Edit
Dans l’onglet Shelves, trouvez la ligne Icon Name en haut à droite
Cliquez sur l’icône du dossier à droite
Choisissez une nouvelle image sur votre ordinateur
 

Bonne journée

(Zakary Breton a tester mes instructions)

