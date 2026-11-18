class Rectangle: # déclaration de classe avec constructeur d'instance __init__ (méthode magique)
    def __init__(self, length, width, color="red"): # création d'objets à partir d'une classe spécifique avec des variables dynamiques (attributs d’instance)
        self.length = length
        self.width = width
        self.color = color

    def calculate_area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3) # instancier un objet Rectangle de longueur 5 et de largeur 3

rect1 = Rectangle(4, 2, "blue") # spécifier une couleur
rect2 = Rectangle(3, 1, color="pink") # spécifier une couleur plus explicitement en utilisant le nom du paramètre

print(rectangle.length) # accéder aux attributs de l'instance de l'objet Rectangle
rectangle.color = "yellow" # affecter une nouvelle couleur en modifiant directement l'attribut de l'instance de l'objet Rectangle

area = rectangle.calculate_area() # assigner une variable au retour de la méthode de l'instance de l'objet Rectangle
print(area) # afficher le nombre 15 retourné par la méthode de calcul de l’aire (longueur x largeur)

class Bird:
    """Un oiseau. 🐦"""

    # ici on utilise deux attributs de classe.
    names = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions = {}

    def __init__(self, name):
        """Les attributs définis ici sont des attributs d'instance."""
        self.wings = 2
        self.position = 1, 2
        self.name = name
        
        # On accède à l'attribut de classe "positions" avec self (c'est possible).
        self.positions[self.position] = self.name

    def fly(self):
        """Cette méthode est une méthode d'instance."""
        print("Je vole !")

    @classmethod # permet de définir une méthode de classe
    def find_bird(cls, position): # déclaration de fonction (toujours « cls » en premier paramètre = la classe elle-même)
        """Retrouve un oiseau selon la position donnée."""
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]} !"

        return "On a rien trouvé..."

    @staticmethod # permet de définir une méthode statique, qui n'a pas besoin d'instance ni de classe comme premier paramètre
    def get_definition():
        """Donne la définition d'un oiseau."""
        return (
        "Animal (vertébré à sang chaud) au corps recouvert de plumes, "
        "dont les membres antérieurs sont des ailes et qui a un bec."
        )


# On peut accéder aux variables de classe sans instanciation.
Bird.names
Bird.positions
print(Bird.find_bird((2, 5)))

# On instancie un oiseau
bird = Bird("mouette") # obligation d'instancier un oiseau pour utiliser ses attributs
bird.wings
bird.fly()


# On le retrouve avec la méthode find_bird.
print(Bird.find_bird((1, 2)))

# On peut aussi accéder à la définition d'un oiseau sans instancier d'objet
print(Bird.get_definition())
