class Rectangle: # déclaration de classe (variables & méthodes qui composent cette classe  = attributs de classe)
    width = 3 # déclaration d’affectation de variable
    height = 2 # déclaration d’affectation de variable

    def calculate_area(self): # déclaration de fonction (toujours « self » en premier paramètre = l’objet lui-même)
        return self.width * self.height


class Rectangle: # déclaration de classe avec constructeur d'instance __init__ (méthode magique)
    def __init__(self, length, width, color="red"): # création d'objets à partir d'une classe spécifique avec des variables dynamiques (attributs d’instance)
        self.length = length
        self.width = width
        self.color = color