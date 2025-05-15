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
---

# Le chiffrement homomorphique

## Définition générale

Le chiffrement homomorphique est une forme de cryptographie qui permet d’effectuer des opérations sur des données chiffrées, sans jamais avoir besoin de les déchiffrer.

***

Soit $m_{1}$ et $m_{2}$ deux messages clairs, $\star$ une opération simple et $E$ un schéma de chiffrement.  
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
:   structurelle (préserve les opérations)

Correction
:   fonctionnelle (le résultat est bon)

Sécurité
:   l'attaquant n'apprend rien


## Classes de fonctions homomorphes

::: incremental

Deux types de fonctions homomorphes :

- Partielles (+ ou $\times$)

  RSA (multiplication) ou Paillier (addition)

- Complètes (+ et $\times$)

  Brakerski-Gentry-Vaikuntanathan (BGV)

:::

. . .

```
Cela est valide sur des entiers. Pour des flottants, les fonctions sont nécessairement homomorphiques complètes.
```


## Exemple d'une fonction homomorphe partielle : le chiffrement de Paillier



## Application du chiffrement de Paillier



# Reconnaissance d'image à partir de données chiffrées

# Implémentation
