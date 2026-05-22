# Importiert das Modul 'random' für zufällige Auswahl
import random
# Importiert das Modul 'string' für vordefinierte Zeichenketten
import string

def generate_password(
    length=12,
    use_uppercase=True,
    use_digits=True,
    use_special=True
):
    """
    Erzeugt ein zufälliges Passwort mit den angegebenen Kriterien.

    Parameter:
    - length: Länge des Passworts (Standard: 12)
    - use_uppercase: Großbuchstaben einbeziehen? (Standard: Ja)
    - use_digits: Zahlen einbeziehen? (Standard: Ja)
    - use_special: Sonderzeichen einbeziehen? (Standard: Ja)
    """
    # Basis-Zeichensatz: Kleinbuchstaben
    characters = string.ascii_lowercase

    # Füge Großbuchstaben hinzu, falls gewünscht
    if use_uppercase:
        characters += string.ascii_uppercase

    # Füge Zahlen hinzu, falls gewünscht
    if use_digits:
        characters += string.digits

    # Füge Sonderzeichen hinzu, falls gewünscht
    if use_special:
        characters += string.punctuation

    # Erzeuge das Passwort
    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )
    return password

if __name__ == "__main__":
    # Beispielaufruf
    print("Dein neues Passwort:", generate_password(length=16))