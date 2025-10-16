# ----------------------------------
# Programm Name: Lotto.py
# Date: 01.10.2025
# ----------------------------------

## Coding-Vorgabe:
# 1. Eine Main-Methode, um als Einstiegspunkt festzulegen, wegen einer imporierung
# 2. alles auf Englisch machen snake_case, mini-Text mit Beschreibung
# 3. Alle Variablen "änderbar" machen, also nicht fest codieren
#    wegen der änderbarkeit, keine fixen Werte
# 4. Globale Variablen vermeiden
# 5. Methoden müssen so Automar wie möglich sein (Abkappselung)
# 6. Kommentare um Methoden zu beschreiben
# 7. Return Werte benutzen
# ----------------------------------
import random as rnd  

# Eingabe
eingabe = input("Gib 1-6 verschiedene Zahlen (1-45) ein, getrennt durch Leerzeichen: ")

# Methode einbauen, wie oft eine Zufallszahl gezogen werden soll


# String in Zahlen umwandeln
tipp = []
for x in eingabe.split():  
    zahl = int(x)
    tipp.append(zahl)


# Prüfen, ob mindestens eine Zahl eingegeben wurde
if len(tipp) == 0:
    print("Du musst mindestens eine Zahl eingeben!")
    exit()

# Prüfen, ob maximal 6 Zahlen
if len(tipp) > 6:
    print("Maximal 6 Zahlen erlaubt!")
    exit()

# Optional: Bestätigung bei weniger als 6 Zahlen
if len(tipp) < 6:
    input("Du hast weniger als 6 Zahlen eingegeben. Enter drücken zum Fortfahren...")

# Prüfen auf Duplikate
if len(set(tipp)) != len(tipp):
    print("Alle Zahlen müssen verschieden sein!")
    exit()

# Prüfen auf gültigen Bereich
for z in tipp:
    if z < 1 or z > 45:
        print("Ungültige Zahl:", z)
        exit()

# Ziehung
ziehung = sorted(rnd.sample(range(1, 46), 6))

# Ausgabe
print("Dein Tipp:       ", sorted(tipp))
print("Gezogene Zahlen:", ziehung)

# Treffer zählen
treffer = []
for z in tipp:
    if z in ziehung:
        treffer.append(z)

# Treffer ausgeben
if len(treffer) == 0:
    print("Treffer: 0, keine")
else:
    print("Treffer:", len(treffer), treffer)

# Extra-Meldungen
if len(treffer) == 6:
    print("!------ Jackpot! ------!")
elif len(treffer) > 0:
    print("!------ Gut gemacht! ------!")
else:
    print("!------ Verloren ------!")



# 1. Eine Main-Methode, um als Einstiegspunkt festzulegen, wegen einer imporierung
# 2. alles auf Englisch machen snake_case, mini-Text mit Beschreibung
# 3. Alle Variablen "änderbar" machen, also nicht fest codieren
#    wegen der änderbarkeit, keine fixen Werte
# 4. Globale Variablen vermeiden
# 5. Methoden müssen so Automar wie möglich sein (Abkappselung)
# 6. Kommentare um Methoden zu beschreiben
# 7. Return Werte benutzen


# gewähkte Zahl an die letzte Stelle schieben, Letzte Zahl an die gewählte Stelle schieben