# Demander à l'utilisateur son prénom
prenom = input("Entrez votre prénom : ")

# Demander à l'utilisateur son nom
nom = input("Entrez votre nom : ")

# Construire le message de salutation
message = f"Bonjour, {prenom} {nom} ! Bienvenue en Python."

# Afficher le message
print(message)
# Ouvrir un fichier en mode écriture
with open('exemple.txt', 'w') as fichier:
    # Écrire des lignes dans le fichier
    fichier.write("Ceci est la première ligne.\n")
    fichier.write("Et voici la deuxième ligne.\n")

# Ouvrir le fichier en mode lecture
with open('exemple.txt', 'r') as fichier:
    # Lire et afficher le contenu du fichier ligne par ligne
    for ligne in fichier:
        print(ligne.strip())  # Utilisez strip() pour supprimer les sauts de ligne

