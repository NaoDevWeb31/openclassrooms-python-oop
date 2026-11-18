class Toolbox:
    """Boîte à outils"""
    def __init__(self):
        """Initialise la boîte à outils avec une liste vide."""
        self.tools = []
    def add_tool(self, tool):
        """Ajoute un outil à la boîte à outils."""
        pass

    def remove_tool(self, tool):
        """Enlève un outil de la boîte à outils."""
        pass

class Hammer:
    """Marteau"""
    def __init__(self, color="red"):
        """Initialise le marteau avec une couleur spécifiée."""
        self.color = color

    def hammer_in(self, nail):
        """Enfonce un clou avec le marteau."""
        pass

    def remove(self, nail):
        """Retire un clou avec le marteau."""
        pass

    def paint(self, color):
        """Peint le marteau avec la couleur spécifiée."""
        pass

class Screwdriver:
    """Tournevis"""
    def __init__(self, size):
        """Initialise le tournevis avec une taille spécifiée."""
        self.size = size
    def tighten(self, screw):
        """Serre une vis avec le tournevis."""
        pass

    def loosen(self, screw):
        """Desserre une vis avec le tournevis."""
        pass