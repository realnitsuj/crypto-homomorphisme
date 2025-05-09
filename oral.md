# Chiffrement homomorphique appliqué au Machine Learning, et plus particulièrement à la reconnaissance d'image

## Le chiffrement homomorphique

### Définition générale
    
1. Slide 1 : définition générale des concepts

- `Oral`

    ```
    Qu'est-ce que le chiffrement homomorphe ?
    Le chiffrement homomorphique est une forme de cryptographie qui permet d’effectuer des opérations sur des données chiffrées, sans jamais avoir besoin de les déchiffrer.
        
    L'avantage est qu’un serveur (ou un tiers) peut manipuler les données sans jamais voir leur contenu, ce qui est crucial pour la confidentialité. Il y a de nombreuses applications, notamment dans le cloud, le médical, la finance ou l'intelligence artificielle, et dans notre cas la reconnaissance d'image. Concrètement, le résultat d'une opération entre deux membres cryptés doivent donner un résultat qui, une fois décrypté, donne le résultat qu'aurait eu l'opération sur les deux membres avant l'opération de cryptage. 
    
    (Apparition sur la slide)
    
    D'une manière plus formelle, considérons deux messages clairs m_1 et m_2 et ∘ une opération simple telle que l'addition ou la multiplication. Un schéma de chiffrement E est dit homomorphe si, pour ces deux messages m_1​ et m_2​, et l'opération ∘, on a :
    E(m_1)∘E(m_2)=E(m_1⋆m_2)
    Soit l'opération entre le crypté de m_1 et le crypté de m_2 donne un résultat qui correspond au crypté d'une opération entre m_1 et m_2. 
    
    (Apparition sur la slide)
    
    Pour représenter plus simplement, donnons un exemple :
    Soit 1 mon message m_1 et 2 mon message m_2. On ne va pas rentrer tout de suite en détail sur la fonction homomorphe E utilisée, mais on suppose qu'elle est choisie telle que l'opération ° et l'opération * soient l'addition pour un soucis de simplification. On note les cryptés respectifs de m_1 et m_2 selon cette fonction homomorphe e_1 et e_2 et tels que E(m_1) = e_1 et E(m_2) = e_2. Dans notre cas, e_1 = 1839283 et e_2 = 5789483. la somme de e_1 et e_2  fait 1839283+5789483=7628766 et E-1(7628766) = 3. Pour un tiers qui effectue le calcul, aucune information n'a fuitée : néanmoins, des opérations ont été réalisées sur les nombres. On peut donc déléguer le calcul sans crainte de fuites de données.
    
    ```
    
    
### Comment ça marche
    
2. Slide 2 : étapes générales du chiffrement homomorphe

- `Oral`
    
    ```
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
    ```
    
- `Diapo`

    ```
    Le fonctionnement du chiffrement homomorphe
    4 étapes clés :
        1. La fonction de génération des clés
        2. La fonction de chiffrement
        3. La fonction d'évaluation (opérations sur les données chiffrées)
        3. La fonction de déchiffrement
    
    Faire un joli schéma. Petite animation ?
    
    ```
    
3. Slide 3 : Parenthèse sur les principes à respecter

- `Oral`

    ```
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
    ```
    
- `Diapo`
    
    ```
    Principes du chiffrement homomorphe
    
    1. Chiffrement sûr ou presque-sûr, besoins des systèmes d'information (concernant la confidentialité, l'authentification, l'intégrité, la non-répudiation et la disponibilité), principe de Kerchkhoff
    
    2. Correction (Correctness)
        - Le bruit introduit dans le chiffrement -> Animation pour visualiser l'ajout de bruit ?
        -  La précision et l’encodage (cas du chiffrement de nombres réels)
    
    -> Bootstrapping
    
    On distingue donc :
    
    * Homomorphisme : structurelle (préserve les opérations)
    * Correction : fonctionnelle (le résultat est bon)
    * Sécurité : l’attaquant n’apprend rien
    ```
    

4. Slide 4 : classes de fonctions homomorphes (partielles et complètes)

- `Oral`

    ```
    Comme nous l'avons rapidement abordé précédemment, il existe plusieurs classes parmi les fonctions d'évaluation du chiffrement homomorphe. Cette fonction doit être soigneusement choisie pour permettre des opérations sur les données chiffrées tout en assurant que le résultat soit correctement déchiffrable.  
    On peut ainsi distinguer deux types de chiffrements homomorphes selon les calculs pouvant être effectués : 
    
        - Les chiffrement homomorphes partiels, qui désignent l'ensemble des chiffrements homomorphes valides pour une seule opération (addition ou multiplication)
        - Les chiffrements homomorphes complets, qui désignent l'ensemble des chiffrements homomorphes valides pour l'addition *et* la multiplication d'entiers
        
    Un chiffrement homomorphe complet est donc plus fort qu'un chiffrement homomorphe partiel, car la complétude d'une fonction d'évaluation implique ainsi sa partialité. Bien qu'on puisse penser qu'une multiplication d'entiers est une simple addition successive, effectuer cette méthode n'est pas viable lorsqu'il s'agit de grands nombres. En pratique ce sont donc les fonctions d'évaluation complètes qui sont utilisées dans la plupart des cas.
    
    /!\ Il est bon de noter que nous ne désignons que des entiers dans le chiffrement homomorphe partiel. Lorsque des fonctions d'évaluation sont utilisées pour du machine learning, il est impératif que celles-ci soient complètes dans un premier temps, et capables d'opérations sur des flottants dans un second temps. Nous parlerons plus tard de ce cas de figure d'opérations sur des flottants et considérerons des entiers pour la suite. 
    
    Pour illustrer le propos sur ces deux catégories de chiffrements homomorphes, nous allons prendre un exemple de chiffrement partiel et de chiffrement complet et montrer leur fonctionnement, en cryptant ensemble deux messages et en effectuant des opérations sur eux. 
    
    Le chiffrement partiel que nous allons étudier en exemple est le chiffrement Pailler. Le chiffrement complet sera le chiffrement BGV (Brakerski-Gentry-Vaikuntanathan). 
    ```

    
- `Diapo`
    
    ```
    (Texte) 
    Deux types de fonctions homomorphes : 
        - Partielles (+ ou *)
        - Complètes (+ et *)
        
    
    (Apparaît ensuite)
    
    /!\ Cela est valide sur des entiers. Pour des flottants, les fonctions sont nécessairement homomorphiques complètes.
    
    (Apparaît ensuite)
    
    1. Fonction homomorphe partielle : Paillier (Addition uniquement)
    2. Fonction homomorphe complète : BGV (Addition et multiplication)
    
    ```

5. SLide 5 : exemple d'une fonction homomorphe partielle : chiffrement de Paillier


- `Oral`

    ```
    Considérons tout d'abord la fonction homomorphe partielle. La chiffrement que nous avons choisi ici s'appelle le chiffrement Paillier.
    
    Le chiffrement Paillier est un exemple de schéma de chiffrement homomorphe partiel qui permet uniquement d'effectuer des additions sur des nombres entiers. C'est l'un des systèmes de chiffrement homomorphe les plus populaires ; c'est un chiffrement à clé publique et basé sur la difficulté du problème du logarithme discret dans les groupes multiplicatifs.
    
    Voici son fonctionnement :

    Comme les autres chiffrement homomorphes, Pailler repose sur un chiffrement à clé publique/clé privée. La clé publique permet de chiffrer les données, et la clé privée est utilisée pour les déchiffrer.
    Nous allons aborder étapt par étape de façon détaillée les méthodes sur lesquelles reposent ce chiffrement.
    
    1. Génération des clés
    
    Pour la génération de clé, on peut choisir deux grands nombres premiers distincts p et q.
    On calcule n=p×q (le module, qui est utilisé dans le processus de chiffrement).
    On calcule λ=PPCM(p−1,q−1), où PPCM est le plus petit multiple commun.
    On choisit un entier  dans Zn^2​, tel que g ait un ordre dans le groupe Zn∗​ (Cela signifie qu'il doit être un générateur du groupe multiplicatif Zn∗​, ou avoir des propriétés similaires). En d'autres termes, on doit avoir g premier avec n² et  PPCM(L(g^λ mod(n^2)),n)=1. Choisir g=n+1 est généralement privilégié.
    La clé publique est constituée des valeurs (n,g), et la clé privée est λ, qui est utilisée pour le déchiffrement.
    
    2. Chiffrement des messages
    
    Supposons que nous voulons chiffrer un message m (un entier compris entre 0 et n).
    On choisit un nombre aléatoire r tel que r∈Zn∗​, c'est-à-dire r doit être un entier entre 1 et n−1, et r doit être premier avec n.
    On calcule ensuite le chiffrement de m avec la formule suivante :
    E(m)=g^m×r^n mod(n^2)

    Le message m est donc chiffré en produisant deux composantes : g^m et r^n.
    La valeur chiffrée E(m) est un entier qui représente le message de manière secrète. Cette valeur peut être envoyée à un serveur sans que celui-ci ne puisse connaître le message réel m.
    
    3. Opérations sur les messages chiffrés (Addition)
    
    L'une des caractéristiques principales de Paillier est son additionnalité homomorphe comme nous l'avons vu. Si nous avons deux messages chiffrés, E(m1) et E(m2), nous pouvons effectuer une opération d'addition sur ces messages chiffrés sans jamais les déchiffrer.
    Supposons que nous ayons deux messages m1​ et m2​, avec leurs versions chiffrées respectives E(m1) et E(m2).
    La propriété homomorphe additive du chiffrement Paillier nous permet de ajouter les messages chiffrés :
    E(m1)⋅E(m2)=E(m1+m2) mod(n^2)
    L'addition des deux valeurs chiffrées donne une nouvelle valeur chiffrée qui représente la somme des deux messages en clair. Ce résultat peut ensuite être déchiffré pour obtenir la somme réelle m1+m2​.
    
    
    4. Déchiffrement du message

    Pour déchiffrer un message c chiffré, on utilise la clé privée. L'étape de déchiffrement fonctionne de la manière suivante :
    
        - On calcule L(c^λ mod(n^2), où L(x) est la fonction définie par :
            L(x)=(x−1)/n
        Soit : 
            L(c^λ mod(n^2)) = (c^λ mod(n^2)−1)/n​
            
        - On effectue un calcul similaire avec le générateur g, connu publiquement :
        L(g^λ mod(n^2))=((g^λ mod(n^2)) −1)/n
        
        Puis on calcule son inverse modulo n :
        μ=1/(L(g^λ mod(n^2))) mod(n)
        
    Le message clair m est obtenu en multipliant les deux résultats précédents modulo n :
    m= (L(c^λ mod(n^2))⋅μ) mod(n)
                
    Soit la formule finale générale : 
        m = ((c^λ mod(n^2)−1​)/n * 1/((g^λ mod(n^2) −1​) /n)) mod(n)

    Cela permet d'extraire le message m = m1 +m2 en clair à partir de la version chiffrée c.

    ```
    
- `Diapo`
    ```
    
    ```

    
6. SLide 6 : Application du chiffrement de Paillier

- `Oral`
    ```    
    Exemple concret avec Paillier
    Prenons maintenant un exemple simple pour illustrer le processus de chiffrement et d'addition avec Paillier.
    
    1. Génération des clés
    On choisit p=7 et q=11 (exemple simple).
    On calcule n=p×q=7×11=77.
    On calcule λ=PPCM(7−1,11−1)=PPCM(6,10)=30.
    On choisit g=78 = n+1 comme générateur de façon arbitraire (il correspond car = premier  avec n² = 77² et PPCM(L(g^λ mod(n^2)),n)=1). 
    
    2. Chiffrement du message
    - On chiffre m1=3 avec un r=5 (choisi aléatoirement) :
    E(3) = 78^3×5^77 mod(77^2) = 2390
    - On chiffre m2​=5 avec un r′=8 :
    E(5)=78^5×8^77 mod(77^2) = 1366
    
    3. Addition des messages chiffrés

    On additionne les deux valeurs chiffrées :
    E(3)⋅E(5) = E(3+5) = E(8)
    Or E(3)⋅E(5) = E(3) * E(5) mod(n²) (C'est  notre opération ⋅ ) = 2390⋅1366 mod(77²) = 3790 = c
    Donc E(8) = c = 3790
    
    4. Déchiffrement du message:
    
    Calculs intermédiaires : 
    - c^λ mod(n^2) = 3790^30 mod(77²) = 694
    - L(c^λ) = 77694−1 ​= 9
    - g^λ mod(n^2) = 2311
    - L(g^λ) = 772311−1 ​= 30
    - Inverse modulaire de 30 mod(77) = 18
    
    D'où :
    -> m=L(c^λ) * 1/L(g^λ) mod(n)=9*18 mod(77) = 8 = 5+3.
    ```
- `Diapo`
    ```
    ```

    
7. SLide 7 : exemple d'une fonction homomorphe complète : chiffrement BGV

- `Oral`
    ```
    ```
    
- `Diapo`
    ```
    ```
    
8. SLide 8 : Application du chiffrement BGV

- `Oral`
    ```
    ```
    
- `Diapo`
    ```
    ```
--- 

## Reconnaissance d'image à partir de données chiffrées

- Apple 
    -> On parle de leur méthode de façon générale (comme sur l'article)
    -> Comment faire de l'homomorphisme pour du machine learning comme ce ne sont pas des entiers à traiter ?

- CKKS
    -> Explication du principe

## Implémentation

- CKKS pour reconnaissance d'image


