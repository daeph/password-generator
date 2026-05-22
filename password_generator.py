# --- IMPORTE ---
# Importiert das Modul 'random', um zufällige Auswahl zu ermöglichen (z. B. für Passwort-Zeichen)
import random
# Importiert das Modul 'string', das vordefinierte Zeichenketten enthält (z. B. Buchstaben, Zahlen, Sonderzeichen)
import string

# --- FUNKTION: Passwort generieren ---
def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """
    Erzeugt ein zufälliges Passwort mit den angegebenen Kriterien.

    Parameter:
    - length: Länge des Passworts (Standard: 12 Zeichen)
    - use_uppercase: Soll Großbuchstaben (A-Z) enthalten? (Standard: Ja)
    - use_digits: Soll Zahlen (0-9) enthalten? (Standard: Ja)
    - use_special: Soll Sonderzeichen (!@#$%^&* etc.) enthalten? (Standard: Ja)
    """
    # Starte mit Kleinbuchstaben (a-z) als Basis für das Passwort
    characters = string.ascii_lowercase

    # Füge Großbuchstaben (A-Z) hinzu, falls gewünscht
    if use_uppercase:
        characters += string.ascii_uppercase  # string.ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Füge Zahlen (0-9) hinzu, falls gewünscht
    if use_digits:
        characters += string.digits  # string.digits = "0123456789"

    # Füge Sonderzeichen hinzu, falls gewünscht
    if use_special:
        characters += string.punctuation  # string.punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Erzeuge das Passwort:
    # 1. 'random.choice(characters)' wählt ein zufälliges Zeichen aus 'characters' aus
    # 2. 'for _ in range(length)' wiederholt das 'length'-mal (z. B. 16x)
    # 3. ''.join(...) fügt alle ausgewählten Zeichen zu einem String zusammen
    return ''.join(random.choice(characters) for _ in range(length))

# --- HAUPTPROGRAMM ---
# Diese Zeile prüft, ob das Skript DIREKT ausgeführt wird (nicht importiert)
if __name__ == "__main__":
    # Ruft die Funktion auf und gibt das Ergebnis aus:
    # - length=16: Erzeuge ein 16 Zeichen langes Passwort
    # - Alle anderen Parameter bleiben auf Standard (True)
    print("Dein neues Passwort:", generate_password(length=16))