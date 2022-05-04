# @tremlab
# a python module that builds a populated binary tree for morse code values, with a method to easily translate a morse code string to its letter.


# https://lh3.googleusercontent.com/mpkDQZsFuR33eurypql-RlIlZIY-wmcWFqn1p5Kju5AmvgZC3EPWEMLePv4qJeJpVhNLUPM6cLgxrWHJ8edEP9HffzLLBQ2C4-V901xt6jk642n-k8hoZ3pQebd0eMj1_XJ54HYK

# Scrivere un programma che dato in input un codice morse restituisca la decodifica in lettere.

# L’input sarà una stringa composta dalla combinazione di 4 caratteri: . - ? e lo spazio.
# Ogni lettera nella stringa è delimitata dallo spazio. Ulteriori spazi non hanno significato.
# Per ricavare ogni lettera si faccia riferimento all’immagine sopra: con un “.” si va a sinistra dell’albero, con un “-” si va a destra dell’albero, mentre con un “?” si va sia a destra che a sinistra.
# Ogni lettera sarà rappresentata con un numero di caratteri variabili da 1 a 3.

# Esempio:

# Input: ..- -? .
# Output: UNME

class Morse_Code_Bin_Tree(object):
    """Class that initializes and populates a binary tree for translating morse code strings into letters.
    """

    def __init__(self):
        self.head = Node("*")

        letters = "ETIANMSURWDKGO"

        current = self.head
        nexts = []

        for char in letters:
            if current.left == None:
                current.left = Node(char)
            else:
                if current.right == None:
                    current.right = Node(char)
                else:
                    nexts.append(current.left)
                    nexts.append(current.right)
                    current = nexts.pop(0)
                    current.left = Node(char)

    def translate_mc_to_letter(self, mc_ltr_str):
        current = self.head

        for char in mc_ltr_str:
            if char == ".":
                current = current.left
            elif char == "-":
                current = current.right

        return current.val

    def translate_mc_to_letter_pas(self, mc_ltr_str):
        res = ""
        trans = []
        current = self.head
        trans.append(current)

        for char in mc_ltr_str:
            # if len(trans):
            #     current = trans.pop(0)
            if char == ".":
                for x in trans[:]:
                    current = trans.pop(0)
                    trans.append(current.left)
            elif char == "-":
                for x in trans[:]:
                    current = trans.pop(0)
                    trans.append(current.right)
            else:
                for x in trans[:]:
                    current = trans.pop(0)
                    trans.append(current.left)
                    trans.append(current.right)

        for t in trans:
            res = res + t.val
        return res


class Node(object):
    """binary node"""

    def __init__(self, char):
        self.val = char
        self.left = None
        self.right = None
