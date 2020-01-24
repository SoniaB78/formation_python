# __*Formation python*__

*Espace de travail pour le projet du pendu :*

## Fonctionnement GIT

### branch master
Cette branche est la branche principale du projet, c'est sur cette branche que les différentes parties vont être merge.
Avant de merge sur celle-ci **vérifiez que votre code fonctionne** et **commentez** on ne le dira jamais top mais dans le travail collaboratif il faut communiquer.
Si il y a un conflit c'est que l'assimilation du code de la branch master et l'autre (ou les autres) ne s'est pas effectuée correctement.
En cas de conflit il faut vérifier que le code rajouté à bien été pris en compte et que d'autres n'ont pas étées supprimées.

### branch dev / test ...
Une branch commune est souvent ajoutée pour les mutualisations de code afin de protége la branch master.
   
### branch à votre nom
Sur cette branch vous metterez à jour vos avancées dans la programmation, essayer de push du code popre, **commenté et fonctionnel**.
_Git add ._ et son commit sont différent de la sauvegarde sur l'ordinateur, pas besoin de commit à chaque sauvegarde en local.
**Il ne faut pas confondre ou assimiler le commit et le push!** On doit commit pour push mais chaque commit n'implique pas un push.

### Commit 
Avant de Commit tu dois entrer _git add ._ , cette commande récupèrera les changements depuis le dernier commit et seront utilisés pour le commit qui suit.
_git commit -m "tonblabla"_ sert à sauvegarder tes changements pour ton **versionning**, ainsi en plus d'avoir une sauvegarde dans ton explorateur de fichier (ne gardant que la dernière version),
tu auras également une trace de tes changements et te permettera de faire machine arrière si quelque chose se passe mal.

### Push
Push sur ta branch quand tu as ajouté une fonctionnalité qui marche, afin qu'on puisse récupérer le travaille fait et voir si c'est compatible.
Ce n'est que sur la fin du projet ou que quelqu'un à finit de travailler sur le projet qu'il fera un merge / push sur l'origin master.
Avant de **push sur une autre branch que la vôtre**, vérifiez que vous ètes à jour sur la destination du push à l'aide de _git log_ et si besoin pullez.

### Pull
Avant de taper _git pull origin nomDeBanch_, il faut **obligatoirement** que l'autre branch ai push pour pouvoir récupérer les changements. 
Il est **recommandé** de push sur notre branch avant de pull le contenu d'une autre pour réduire les risques de **conflits**, 
mais il est **encore plus fortement conseillé** de faire au moins un commit pour avoir une sauvegarde an cas de conflit. 

## Organisation du dossier
Le fichier " pendu " contient une version console et une version utilisant Pygame. 
La version console fonctionne avec un solo.py et 4 dossiers, un par thème, il en va de même pour l'autre version.

## Documentation
[Blog: Synbioz](https://www.synbioz.com/blog/tech/git-adopter-un-modele-de-versionnement-efficace)
[Forum: Openclassrooms ](https://openclassrooms.com/forum/sujet/git-pull-sans-commit-49970#message-7109921)


>En espérant que ce ReadMe vous ai été utile.
![Logo sonia devint](https://soniadevint.fr/portfolio/view/inc/img/logo.png)



