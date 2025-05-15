import random
import math
from sympy import mod_inverse, lcm

# -----------------------
# Ce code est un code d'exemple applicatif du Chiffrement de Pailliler. Voici les paramètres qu'il considère :
# - p = 7
# - q = 11
# Ceci sont simples et ne fonctionnent que pour des additions d'entiers petits et de démonstration. On peut vérifier si l'opération est bonne et donc observer les divergences.
# -----------------------


# -----------------------
# Génération des clés
# -----------------------
def generate_keys(p, q):
    n = p * q
    nsq = n * n
    lam = int(lcm(p - 1, q - 1))  # Convertir en vrai int python
    g = n + 1  # Comme dans notre exemple, choix simple
    if math.gcd(g, nsq) != 1:
        raise ValueError("g n'est pas premier avec n^2")
    return (n, g), (lam, n)

# Fonction L définie par le schéma de Paillier
def L(u, n):
    return (u - 1) // n

# -----------------------
# Chiffrement
# -----------------------
def encrypt(m, public_key):
    n, g = public_key
    nsq = n * n
    r = random.randint(1, n - 1)
    while math.gcd(r, n) != 1:
        r = random.randint(1, n - 1)
    c = (pow(g, m, nsq) * pow(r, n, nsq)) % nsq
    print(f" Chiffrement de {m} avec r = {r}:")
    print(f"   c = (g^{m} mod n²) * (r^n mod n²) mod n²")
    print(f"   => c = {c}")
    return c

# -----------------------
# Déchiffrement
# -----------------------
def decrypt(c, private_key, public_key):
    lam, n = private_key
    g = public_key[1]
    nsq = n * n
    u = pow(c, lam, nsq)
    l_u = L(u, n)
    g_lam = pow(g, lam, nsq)
    l_g = L(g_lam, n)
    mu = mod_inverse(l_g, n)
    m = (l_u * mu) % n
    print(f" Déchiffrement:")
    print(f"   u = c^λ mod n² = {u}")
    print(f"   L(u) = {l_u}, L(g^λ mod n²) = {l_g}, μ = {mu}")
    print(f"   m = L(u) * μ mod n = {m}")
    return m


# -----------------------
# Addition homomorphe
# -----------------------
def homomorphic_add(c1, c2, n):
    nsq = n * n
    c_add = (c1 * c2) % nsq
    print(f" Addition homomorphe:")
    print(f"   c_add = c1 * c2 mod n² = {c_add}")
    return c_add


# -----------------------
# Main
# -----------------------
if __name__ == "__main__":
    # Petits premiers d'exemple'
    p = 7
    q = 11
    print("Génération des clés :")
    public_key, private_key = generate_keys(p, q)
    n, g = public_key
    print(f"   p = {p}, q = {q}")
    print(f"   n = {n}, g = {g}, λ = {private_key[0]}")
    print("-" * 50)

    # Entrée utilisateur
    m1 = int(input("Entrez le message m1 (entier) : "))
    m2 = int(input("Entrez le message m2 (entier) : "))
    print("-" * 50)

    # Chiffrement
    c1 = encrypt(m1, public_key)
    print("-" * 50)
    c2 = encrypt(m2, public_key)
    print("-" * 50)

    # Addition homomorphe
    c_add = homomorphic_add(c1, c2, n)
    print("-" * 50)

    # Déchiffrement
    result = decrypt(c_add, private_key, public_key)
    print("-" * 50)

    # Comparaison avec la valeur réelle
    expected = (m1 + m2)
    print(f"Résultat attendu : {m1} + {m2} mod n = {expected}")
    print(f" Comparaison : {' Correct' if result == expected else f' Incorrect (obtenu = {result})'}")
