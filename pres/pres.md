---
title: Chiffrement homomorphique appliqué au Machine Learning
#subtitle: Scripting system
author:
- Justin Bossard
- Tom Mafille
lang: fr-FR
slideNumber: true
controls: false
theme: white
revealjs-url: https://unpkg.com/reveal.js@^4
---

# Le chiffrement homomorphique

## Définition générale

Le chiffrement homomorphique est une forme de cryptographie qui permet d’effectuer des opérations sur des données chiffrées, sans jamais avoir besoin de les déchiffrer.

***

Soit $m_{1}$ et $m_{2}$ deux messages clairs, $\star$ et $\circ$ une opération simple et $E$ un schéma de chiffrement.  
$E$ est dit homomorphe si on a :$$E(m_{1} \star m_{2}) = E(m_{1}) \circ E(m_{2})$$

## Comment ça marche ?

::: incremental

1. La fonction de génération de clés

2. La fonction de déchiffrement

3. La fonction d'évaluation (opérations sur les données chiffrées)

4. La fonction de déchiffrement
:::

## Principes à respecter

::: incremental

1. Chiffrement sûr ou presque-sûr, besoins des systèmes d'information (confidentialité, authentification, intégrité, non-répudiation et disponibilité), principe de Kerckhoff

2. Correction (Correctness)

   ::: nonincremental
   - Le bruit introduit dans le chiffrement
   - La précision et l'encodage (cas du chiffrement de nombres réels)
   :::

   $\Rightarrow$ **Bootstrapping**

:::

***

On distingue donc :

Homomorphisme
:   structurel (préserve les opérations)

Correction
:   fonctionnel (le résultat est bon)

Sécurité
:   l'attaquant n'apprend rien


## Classes de fonctions homomorphes

::: incremental

Deux types de fonctions homomorphes :

- Partielles ($+$ ou $\times$)

  RSA (multiplication) ou Paillier (addition)

- Complètes ($+$ et $\times$)

  Brakerski-Gentry-Vaikuntanathan (BGV)

:::

. . .

```
Cela est valide sur des entiers. Pour des flottants, les fonctions sont nécessairement homomorphiques complètes.
```

## Exemple d'une fonction homomorphe partielle : le chiffrement de Paillier

Schéma homomorphe partiel
:   permet uniquement l’addition sur des données chiffrées.

Basé sur la difficulté du logarithme discret dans les groupes multiplicatifs.

### Génération des clés

::: incremental

1. Choix de deux grands nombres premiers : $p$, $q$

2. Calcul : $n = p \times q$

3. Clé publique : $(n,g)$ avec $g \in Z_{n^{2}}$ et $g=n+1$ en général

4. Clé privée : $\lambda = PPCM(p-1,q-1)$

:::

### Chiffrement d’un message

::: incremental

1. Message $m \in [0,n]$

2. Choix d’un nombre aléatoire $r \in Z_{n}^{*}$

3. Formule de chiffrement :
   $$E(m)=g^{m} \times r^{n} mod(n^{2})$$

:::

### Propriété homomorphe

::: incremental

- Pour deux messages chiffrés $E(m_{1})$ et $E(m_{2})$ : $E(m_{1}) \times E(m_{2}) = E(m_{1} + m_{2})mod(n^{2})$

- Permet de faire une addition dans le domaine chiffré sans accès aux données en clair.

:::

### Déchiffrement

On définit $L(x) = \frac{x - 1}{n}$

Calcul du message déchiffré :

$m = \left(\frac{c^{\lambda} mod(n^{2}) - 1}{n} \times \frac{1}{L(g^{\lambda} mod (n^{2})) mod(n)}\right) mod(n)$



## Exemple d'une fonction homomorphe complète : BGV

Schéma homomorphe complet
:   permet l’addition et la multiplication sur des données chiffrées.

. . .

Basé sur la difficulté du problème LWE, résistant aux attaques quantiques.

. . .

Utilise des polynômes dans des anneaux du type $\mathbb{Z}[X]/(\Phi_m(X))$ où $\Phi_m$ est un polynôme cyclotomique.

### Génération des clés

1. Choix des paramètres :
   - $n$ : degré du polynôme (puissance de 2)
   - $q$ : grand entier premier (modulo)
   - f(x) : polynôme cyclotomique, généralement
     
     $f : x \mapsto x^n + 1$

***

2. Clé privée $s(x)$ : polynôme aléatoire, coefficients dans $\{-1, 0, 1\}$, $deg \leq n$

***

3. Génération de la clé publique :
   - $a(x) \in R_q \text{ aléatoire}$
   - $e(x) \text{ petit bruit}$
   - $b(x) = -a(x) \times (x) + e(x) mod(q)$

   Clé publique : $(a(x), b(x))$


### Chiffrement d’un message

::: incremental

1. Encodage du message $m(x)$ : $m'(x) = m(x) \cdot \delta$

   avec $\delta = \lfloor \frac{q}{t} \rfloor$

2. Choix d’un bruit aléatoire $r(x)$

3. Calcul du chiffré :
   
   ::: nonincremental

   - $c_0(x) = b(x) \cdot r(x) + m'(x) \mod q$
   - $c_1(x) = a(x) \cdot r(x) \mod q$

   :::

   Le chiffré est la paire $(c_0(x), c_1(x))$

:::

### Propriétés homomorphes

::: incremental

- **Addition** :
  
  $$(c_{0},c_{1}) + (c_{0}',c_{1}') = (c_{0} + c_{0}', c_{1} + c_{1}')$$

- **Multiplication** :
  Multiplie deux chiffrés → donne un triplet $(c_0, c_1, c_2)$  
  Il faut une étape de **relinéarisation** pour revenir à un format à deux composantes.

:::

### Déchiffrement

::: incremental

1. Calcul intermédiaire :

   $$m'(x)=c_{0}(x)+c_{1}(x) \times s(x) ~ mod(q)$$


2. Décodage final :

   $$m(x) = \lfloor \frac{m'(x)}{\delta} \rfloor$$

:::

# Reconnaissance d'image à partir de données chiffrées

## Définitions

Vecteur d'embedding
:   Encode les caractéristiques visuelles essentielles d’une image (formes, couleurs, textures) dans un espace vectoriel de dimension réduite (souvent entre 128 et 512 dimensions).

***

Quantification
:   Convertion des valeurs réelles en entiers pour permettre leur chiffrement. Cela permet d’utiliser un chiffrement comme BFV qui ne supporte que les entiers.

***

Batching
:   Encodage par paquets

# Implémentation
