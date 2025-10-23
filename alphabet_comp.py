alphabet = "abcdefghijklmnopqrstuvwxyz"
# Upper und Lowercase Buchstaben als eigene Methode
def firstTask():
    alphabet_dict = {letter: i for i, letter in enumerate(alphabet)}

    # enumerate() gibt bei jedem Durchlauf zwei Werte zurück:
    # i = laufende Nummer (beginnt bei 0)
    # letter = aktueller Buchstabe aus der Zeichenkette
    print(alphabet_dict)

def secondTask():
    #print("hello")
    for i, letter in enumerate(alphabet):
        print(i, letter)


def main(): # alle Methoden hier auflisten, um einen Zentralen einstiegspunkt zu setzen
    firstTask()
    secondTask()

if __name__ == "__main__":
    main() # Hier wird der Zentrale Einstiegspunkt genutzt