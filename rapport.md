---
title: Le chiffrement homomorphique appliqué au Machine Learning, et plus particulièrement à la reconnaissance d'image
subtitle: Rapport
author: 
    - Justin BOSSARD
    - Tom MAFILLE
geometry: margin=2cm
lang: fr-FR
header-includes:
 - \usepackage{fvextra}
 - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
---


# Le chiffrement homomorphique

## Définition générale

Le chiffrement homomorphique est une forme de cryptographie qui permet d’effectuer des opérations sur des données chiffrées, sans jamais avoir besoin de les déchiffrer.
    
L'avantage est qu’un serveur (ou un tiers) peut manipuler les données sans jamais voir leur contenu, ce qui est crucial pour la confidentialité. Il y a de nombreuses applications, notamment dans le cloud, le médical, la finance ou l'intelligence artificielle, et dans notre cas la reconnaissance d'image. Concrètement, le résultat d'une opération entre deux membres cryptés doivent donner un résultat qui, une fois décrypté, donne le résultat qu'aurait eu l'opération sur les deux membres avant l'opération de cryptage. 


D'une manière plus formelle, considérons deux messages clairs m_1 et m_2 et $\star$ une opération simple telle que l'addition ou la multiplication. Un schéma de chiffrement E est dit homomorphe si, pour ces deux messages m_1​ et m_2​, et l'opération $\star$, on a :
E(m_1) $\star$ E(m_2)=E(m_1⋆m_2)
Soit l'opération entre le crypté de m_1 et le crypté de m_2 donne un résultat qui correspond au crypté d'une opération entre m_1 et m_2. 


Pour représenter plus simplement, donnons un exemple :
Soit 1 mon message m_1 et 2 mon message m_2. On ne va pas rentrer tout de suite en détail sur la fonction homomorphe E utilisée, mais on suppose qu'elle est choisie telle que l'opération ° et l'opération * soient l'addition pour un soucis de simplification. On note les cryptés respectifs de m_1 et m_2 selon cette fonction homomorphe e_1 et e_2 et tels que E(m_1) = e_1 et E(m_2) = e_2. Dans notre cas, e_1 = 1839283 et e_2 = 5789483. la somme de e_1 et e_2  fait 1839283+5789483=7628766 et E-1(7628766) = 3. Pour un tiers qui effectue le calcul, aucune information n'a fuitée : néanmoins, des opérations ont été réalisées sur les nombres. On peut donc déléguer le calcul sans crainte de fuites de données.


Maintenant, nous allons nous pencher plus précisément sur le fonctionnement du chiffrement homomorphe et les étapes clés qu'il implique d'un point de vue général.
En effet, pour que le chiffrement homomorphe fonctionne, plusieurs fonctions clés doivent être utilisées. Ces fonctions permettent respectivement de générer des clés, de chiffrer des données, de réaliser des calculs sur ces données, et de les déchiffrer une fois les opérations terminées.
Tout type de chiffrement homomorphe implique ces 4 étapes clés. Il est tout de même bon de noter que c'est seulement la base indéfectible de ce qui constitue le chiffrement homomorphe et que d'autres étapes peuvent être engagées suivant les différents types de chiffrement homomorphes que nous aborderons par la suite. 

Voici ces étapes :

1. En premier lieu, la fonction de génération des clés

C'est la première étape d'un système de chiffrement homomorphe. Elle génère deux types de clés :
    - Clé publique : utilisée pour chiffrer les données.
    - Clé privée : utilisée pour déchiffrer les données.

Les clés sont générées à partir de paramètres cryptographiques tels que des grands nombres premiers, et elles permettent de garantir que seules les personnes possédant la clé privée peuvent déchiffrer les données. Nous ne nous attarderons pas sur cela étant donné que nous avons étudié ça en cours.
On peut tout de même noter que les clés publiques et privées doivent être générées avec une structure mathématique qui permettra d’effectuer certaines opérations sur les données chiffrées, on ne peut pas les choisir au hasard. 
On ne rentrera pas dans ces détails dans cet exposé, mais par exemple, si on veut autoriser des additions dans le monde chiffré, comme dans le chiffrement de Paillier que nous verrons tout à l'heure, on choisit une structure qui rend cela possible — ici, un groupe de Z mod n².
Pour CKKS que nous verrons également, c’est encore plus complexe, car on doit pouvoir faire des multiplications, des divisions approximées, et gérer la précision. Les clés sont donc construites autour de polynômes, avec des paramètres très spécifiques (représentation des vecteurs de nombres réels ou complexes comme des polynômes dans un anneau modulo un cyclotomique pour les plus curieux et matheux). 

2. Ensuite, la fonction de chiffrement

La fonction de chiffrement prend un message en clair et le transforme en un message chiffré à l'aide de la clé publique. Le chiffrement doit être conçu de manière à préserver la sécurité du message, tout en permettant l'application d'opérations sur le message chiffré.
Les messages sont généralement représentés sous forme d'entiers, mais elles peuvent également être sous forme de vecteurs ou de flottants suivant la complexité de la fonction homomorphe mise en jeu. Le chiffrement transforme ces données en un format difficilement lisible sans la clé privée.

Le chiffrement homomorphe encode les données de manière à ce que certaines opérations effectuées sur les chiffrés aient un équivalent direct sur les données en clair. C'est la structure même du chiffrement (et non juste la clé publique) qui rend cela possible.

3. Puis la fonction d'évaluation (opérations sur les données chiffrées)

La fonction d'évaluation permet de réaliser des calculs ou des opérations sur les données chiffrées. Ces opérations peuvent être de différents types, selon le type de chiffrement homomorphe :
    - Addition homomorphe : Ajouter deux valeurs chiffrées, ce qui donnera une nouvelle valeur chiffrée représentant la somme des messages en clair.

    - Multiplication homomorphe : Multiplier deux valeurs chiffrées pour obtenir un résultat chiffré correspondant à la multiplication des messages en clair.

Ces opérations sont réalisées sur les données chiffrées, et l'idée est de préserver la sécurité des données tout en effectuant les calculs nécessaires. Il existe différents niveaux de fonctionnalité selon les schémas (chiffrement partiellement homomorphe, totalement homomorphe, etc.) que nous allons étuier dans la prochaine slide.

C’est ici que l’homomorphie est véritablement exploitée. Les schémas homomorphes sont construits de manière à permettre des opérations dans l’espace chiffré qui ont un sens dans l’espace en clair. C’est cette étape qui distingue un chiffrement classique d’un chiffrement homomorphe.

4. Et enfin la fonction de déchiffrement

La fonction de déchiffrement permet de récupérer les messages en clair à partir des données chiffrées après qu'une opération a été effectuée. Cette fonction utilise la clé privée pour déchiffrer le résultat, et elle doit être conçue de manière à garantir que le déchiffrement donne le bon résultat des calculs réalisés sur les données chiffrées.

Par exemple, après avoir ajouté deux messages chiffrés, la fonction de déchiffrement permet de récupérer le résultat de cette addition sur les messages en clair.


Avant de passer à la suite, nous allons ouvrir une parenthèse : c'est important de noter un certain nombre de points concernant le chiffrement homomorphe. 
Il est nécessaire de savoir qu'il existe plusieurs principes à respecter pour que le chiffrement homomorphe soit correct. Il ne s'agit pas uniquement de trouver ces fonctions qui correspondent et le tour est joué. En plus de respecter les conditions cryptographiques basiques (chiffrement sûr ou presque-sûr, besoins des systèmes d'information (concernant la confidentialité, l'authentification, l'intégrité, la non-répudiation et la disponibilité) et respectant le principe de Kerchkhoff),  le chiffrement doit remplir une condition supplémentaire, qui est la suivante.

1. Correction (Correctness)

Le principe fondamental du cryptage homomorphique est la correction. Cela signifie que les opérations réalisées sur des données chiffrées doivent produire des résultats corrects lorsqu'elles sont décryptées. En d'autres termes, si on applique une opération sur des données chiffrées, le déchiffrement du résultat doit correspondre à l'opération effectuée sur les données originales.
Cela garantit que le chiffrement homomorphe fonctionne de manière fiable et qu'il n'introduit aucune erreur durant les calculs.

Maintenant, on peut se dire que cela est naturel lorsqu'il y a homomorphie. Alors pourquoi la correction n'est pas garantie par simple homomorphie ?

Une fonction de chiffrement peut être homomorphe sur une certaine opération, mais ne pas garantir la correction dans toutes les conditions, notamment à cause de deux facteurs principaux :
    - Le bruit introduit dans le chiffrement
    Dans la plupart des schémas de chiffrement homomorphes modernes (comme BGV ou CKKS que nous allons voir…), chaque opération (addition ou multiplication) augmente le bruit dans le chiffré.
    Ce bruit est d'erreur introduite pour assurer la sécurité du chiffrement: tant que le bruit reste en dessous d’un certain seuil, le déchiffrement est correct ; mais si le bruit devient trop grand (après de nombreuses opérations), le déchiffrement peut échouer, même si la fonction reste homomorphe au sens formel.
    -  La précision et l’encodage (cas du chiffrement de nombres réels)

    Dans des schémas comme CKKS, qui permettent de traiter des nombres flottants (approximatifs), la correction devient approximative :
    Le résultat déchiffré est proche (mais pas toujours exactement égal) à celui qu’on aurait obtenu en clair. Cela fait partie du design de CKKS, qui tolère une erreur relative contrôlée. On parle alors de chiffrement homomorphe approché (approximate HE), ce qui signifie que la correction est bornée mais pas exacte.
    Une fonction peut être homomorphe sans être "correcte" dans tous les cas.

Pour assurer la correction, on peut utiliser le bootstrapping. Qu'est-ce que c'est le bootstrapping ?
Le bootstrapping est une technique clé pour rendre le chiffrement homomorphe praticable sur des données de taille plus importante ou pendant plusieurs étapes de calcul. Comme on vient de l'aborder, les schémas de chiffrement homomorphes souffrent souvent d'un croissance exponentielle du bruit au fur et à mesure que des opérations sont effectuées. Ce bruit peut rendre les données inutilisables pour des opérations supplémentaires.

Le bootstrapping consiste à réinitialiser le bruit à un niveau acceptable, de sorte que l'on puisse continuer à effectuer des calculs sur les données chiffrées sans que le bruit ne compromette le résultat final. C'est un processus coûteux en ressources, mais il est nécessaire pour rendre les calculs sur des données chiffrées pratiquement réalisables à grande échelle.



Pour résumer, il faut donc ajouter une condition explicite de correction, qui garantit que le déchiffrement d’un calcul homomorphe donne bien le bon résultat (ou un résultat approché admissible), tant que certaines conditions sont respectées.
C’est pour cela que dans les définitions formelles, on distingue :
* Homomorphisme : structurelle (préserve les opérations)
* Correction : fonctionnelle (le résultat est bon)
* Sécurité : l’attaquant n’apprend rien

Nous pouvons maintenant fermer cette parenthèse et nous attaquer à la suite concernant les chiffrements homomorphes partiel et complet.


Comme nous l'avons rapidement abordé précédemment, il existe plusieurs classes parmi les fonctions d'évaluation du chiffrement homomorphe. Cette fonction doit être soigneusement choisie pour permettre des opérations sur les données chiffrées tout en assurant que le résultat soit correctement déchiffrable.  
On peut ainsi distinguer deux types de chiffrements homomorphes selon les calculs pouvant être effectués : 
    - Les chiffrement homomorphes partiels, qui désignent l'ensemble des chiffrements homomorphes valides pour une seule opération (addition ou multiplication)
    - Les chiffrements homomorphes complets ou chiffrements entièrement homomorphes (FHE), qui désignent l'ensemble des chiffrements homomorphes valides pour l'addition *et* la multiplication d'entiers
    
Un chiffrement homomorphe complet est donc plus fort qu'un chiffrement homomorphe partiel, car la complétude d'une fonction d'évaluation implique ainsi sa partialité. Bien qu'on puisse penser qu'une multiplication d'entiers est une simple addition successive, effectuer cette méthode n'est pas viable lorsqu'il s'agit de grands nombres. En pratique ce sont donc les fonctions d'évaluation complètes qui sont utilisées dans la plupart des cas.

/!\ Il est bon de noter que nous ne désignons que des entiers dans le chiffrement homomorphe partiel. Lorsque des fonctions d'évaluation sont utilisées pour du machine learning, il est impératif que celles-ci soient complètes dans un premier temps, et capables d'opérations sur des flottants dans un second temps. Nous parlerons plus tard de ce cas de figure d'opérations sur des flottants et considérerons des entiers pour la suite. 

Pour illustrer le propos sur ces deux catégories de chiffrements homomorphes, nous allons prendre un exemple de chiffrement partiel et de chiffrement complet et montrer leur fonctionnement, en cryptant ensemble deux messages et en effectuant des opérations sur eux. 

Le chiffrement partiel que nous allons étudier en exemple est le chiffrement Pailler. Le chiffrement complet sera le chiffrement BGV (Brakerski-Gentry-Vaikuntanathan). 
