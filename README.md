# __*Formation python*__

*Espace de travail pour le projet du pendu : groupe 3.*

## Fonctionnement commit et push
* **Il ne faut pas confondre ou assimiler le commit et le push!** On doit commit pour push mais chaque commit n'implique pas un push.*
### Commit 
Avant de Commit tu dois entrer __git add .__ , cette commande récupèrera les changements depuis le dernier commit et seront utilisés pour le commit qui suit.
__git commit -m "tonblabla"__ sert à sauvegarder tes changements pour ton *versionning*, ainsi en plus d'avoir une sauvegarde dans ton explorateur de fichier (ne gardant que la dernière version),
tu auras également une trace de tes changements et te permettera de faire machine arrière si quelque chose se passe mal.

### Push
Push sur ta branch quand tu as ajouté une fonctionnalité qui marche, afin qu'on puisse récupérer le travaille fait et voir si c'est compatible.
Ce n'est que sur la fin du projet ou que quelqu'un à finit de travailler sur le projet qu'il fera un merge / push su l'origin master.

## Organisation du dossier
Le fichier contient la class Pendu et le programme principal écrit en procédural.
 
 ## Organisation du repository
4 branch ont étées crées afin que chaque collaborateur puisse enregistrer ses modifications su la branch à son nom.
  
  ### branch master
Cette branche est la branche principale du projet, c'est sur cette branche que les différentes parties vont être merge.
Avant de merge sur celle-ci **vérifiez que votre code fonctionne** et **commentez** on ne le dira jamais top mais dans le travail collaboratif il faut communiquer.
Si il y a un conflit c'est que l'assimilation du code de la branch master et l'autre (ou les autres) ne s'est pas effectuée correctement.
En cas de conflit il faut vérifier que le code rajouté à bien été pris en compte et que d'autres n'ont pas étées supprimées.
   
   ### branch à votre nom
Sur cette branch vous metterez à jour vos avancées dans la programmation, essayer de push du code popre, **commenté et fonctionnel**.
Git add . et son commit sont différent de la sauvegarde sur l'ordinateur, pas besoin de commit à chaque sauvegarde en local.
