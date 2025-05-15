
# fonction du modulo à la main
def mod(x, q):
    return x % q

# -----------------------------
# Ce code est un code d'exemple applicatif du Chiffrement BGV. Voici les paramètres qu'il considère :
# -----------------------------
t = 64                 # espace de message modulo t
q = 2**36             # grand module (sans noise budget)
delta = 1024           # facteur d'encodage (scale factor)

# Clé secrète, échantillon aléatoire, bruit et aléa (fixés ici pour simplicité, cf rapport)
s = 1
a = 1234
e = 1
r = 1
# Ceci sont simples et ne fonctionnent que pour des multiplications d'entiers relativement petits (cf rapport) et de démonstration. On peut vérifier si l'opération est bonne et donc observer les divergences. Ici, ça fonctionne jusqu'à environ 8*8.


# -----------------------------
# Génération de la clé
# -----------------------------
def keygen(q, a, s, e):
    """
    Génère la clé publique (a, b) et la clé secrète s
    selon la formule : b = -a * s + e mod q
    """
    b = mod(-a * s + e, q)
    return (a, b), s

# -----------------------------
# Encodage et décodage des messages
# -----------------------------
def encode(m, delta):
    """Encode un message m en entier modulo q via un facteur delta, ici fixe"""
    return m * delta

def decode(m_prime, delta, t):
    """
    Décodage du message chiffré m_prime.
    On divise par delta, puis modulo q pour retrouver m.
    """
    return (m_prime // delta) % q

# -----------------------------
# Chiffrement
# -----------------------------
def encrypt(m, pk, delta, r, q):
    """
    Chiffre un message m avec la clé publique pk = (a, b).
    On calcule :
        c0 = b * r + encode(m)
        c1 = a * r
    modulo q.
    """
    a, b = pk
    m_enc = encode(m, delta)
    c0 = mod(b * r + m_enc, q)
    c1 = mod(a * r, q)
    return (c0, c1)

# -----------------------------
# Déchiffrement
# -----------------------------
def decrypt(ciphertext, s, q, delta, t):
    """
    Déchiffre un "ciphertext" (c0, c1) avec la clé secrète s.
    On calcule :
        m' = c0 + c1 * s mod q
    puis on décode pour retrouver m.
    """
    c0, c1 = ciphertext
    m_prime = mod(c0 + c1 * s, q)
    return decode(m_prime, delta, t)

# -----------------------------
# Addition homomorphe
# -----------------------------
def add(c1, c2, q):
    """
    Addition homomorphe de deux "ciphertexts".
    On additionne composante par composante modulo q.
    """
    c0 = mod(c1[0] + c2[0], q)
    c1_ = mod(c1[1] + c2[1], q)
    return (c0, c1_)

# -----------------------------
# Multiplication homomorphe (simplifiée)
# -----------------------------
def mul(c1, c2, s, q):
    """
    Multiplication homomorphe simplifiée de deux ciphertexts.
    Renvoie un ciphertext de degré 1 en appliquant une relinéarisation simple (cf rapport).
    """
    c0 = mod(c1[0] * c2[0], q)
    c1_ = mod(c1[0] * c2[1] + c1[1] * c2[0], q)
    c2_ = mod(c1[1] * c2[1], q)
    # Relinearisation : on injecte c2 * s dans c0 pour réduire le degré comme dans le rapport
    c0p = mod(c0 + c2_ * s, q)
    c1p = c1_
    return (c0p, c1p)

# -----------------------------
# Programme principal
# -----------------------------
if __name__ == "__main__":
    print(f"Paramètres du système :")
    print(f" - t (modulo messages) = {t}")
    print(f" - q (module) = {q}")
    print(f" - delta (facteur d'encodage) = {delta}")
    print(f" - clé secrète s = {s}")
    print(f" - bruit e = {e}")
    print(f" - aléa r = {r}")
    print("-" * 50)

    # Génération des clés
    pk, sk = keygen(q, a, s, e)
    print(f"Clé publique : a = {pk[0]}, b = {pk[1]}")
    print(f"Clé secrète : s = {sk}")
    print("-" * 50)

    # Entrée utilisateur pour deux messages
    m1 = int(input("Entrez le message m1 (entier entre 0 et t-1) : "))
    m2 = int(input("Entrez le message m2 (entier entre 0 et t-1) : "))
    print("-" * 50)

    # Chiffrement
    ct1 = encrypt(m1, pk, delta, r, q)
    ct2 = encrypt(m2, pk, delta, r, q)
    print(f"Chiffrement m1 = {m1} : c0 = {ct1[0]}, c1 = {ct1[1]}")
    print(f"Chiffrement m2 = {m2} : c0 = {ct2[0]}, c1 = {ct2[1]}")
    print("-" * 50)

    # Addition homomorphe
    ct_add = add(ct1, ct2, q)
    result_add = decrypt(ct_add, sk, q, delta, t)
    print(f"Addition homomorphe : {m1} + {m2} mod {q} = {result_add}")
    expected_add = m1 + m2
    print(f" Comparaison : {' Correct' if result_add == expected_add else f' Incorrect (obtenu = {result_add})'}")
    print("-" * 50)

    # Multiplication homomorphe
    # Attention, on multiplie les facteurs d'encodage delta donc il faut diviser par delta^2
    ct_mul = mul(ct1, ct2, sk, q)
    result_mul = decrypt(ct_mul, sk, q, delta * delta, t)
    print(f"Multiplication homomorphe : {m1} * {m2} mod {q} = {result_mul}")
    expected_mul = m1 * m2
    print(f" Comparaison : {' Correct' if result_mul == expected_mul else f' Incorrect (obtenu = {result_mul})'}")
