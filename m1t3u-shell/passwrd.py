import sys
import secrets
import string
import keyring

def generate_passwrd(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_password_to_keyring(service_name, username, password):
    keyring.set_password(service_name, username, password)

def retrieve_password_from_keyring(service_name, username):
    return keyring.get_password(service_name, username)

# Exemple d'utilisation
service_name = "NomDeVotreApplication"
username = "NomDUtilisateur"

# Génération du mot de passe
strong_password = generate_passwrd()
print(f"Mot de passe généré: {generate_passwrd}")

# Sauvegarde du mot de passe dans le trousseau
save_password_to_keyring(service_name, username, generate_passwrd)
print("Mot de passe sauvegardé dans le trousseau.")

# Récupération du mot de passe depuis le trousseau
retrieved_password = retrieve_password_from_keyring(service_name, username)
print(f"Mot de passe récupéré depuis le trousseau: {retrieved_password}")

