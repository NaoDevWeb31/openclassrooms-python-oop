"""Définit les films."""

class Film:
    """Film."""

    def __init__(self, name, creation_date):
        """Initialise un film avec un nom et une date de création."""
        self.name = name
        self.creation_date = creation_date
        self.where = None

    def __str__(self):
        """Représentation du film."""
        return f"{self.name} ({self.creation_date})"

class FilmVHF(Film):
    """Film VHF."""

    type = "VHF"

    def __init__(self, name, creation_date):
        """Initialise un film VHF. L'attribut magnetic_tape indique que le film est sur bande magnétique."""
        super().__init__(name, creation_date)
        self.magnetic_tape = True

class FilmDVD(Film):
    """Film DVD."""

    type = "DVD"

    def __init__(self, name, creation_date):
        """Initialise un film DVD. L'attribut mega_octets représente la capacité de stockage standard d'un DVD."""
        super().__init__(name, creation_date)
        self.mega_octets = 4700

class FilmClean:
    """Génère un film à partir de données de base (nom avec date, type de support)."""

    """Constantes pour les indices des données de base dans le tableau films."""
    NAME_AND_DATE_INDEX = 0
    TYPE_INDEX = 1

    def __init__(self, film_data):
        """Initialise les données du film."""
        self.film_data = film_data

    def generate_film(self):
        """Génère un film à partir des données de base (nom avec date et type de support)."""
        name = self.generate_name()
        creation_date = self.generate_date()
        type = self.generate_type()

        for Film in (FilmVHF, FilmDVD):
            if type == Film.type:
                return Film(name, creation_date)

    def generate_name(self):
        """Génère le nom du film à partir des données de base (nom avec date)."""
        name_and_date = self.film_data[self.NAME_AND_DATE_INDEX]
        return name_and_date[:name_and_date.rfind(" (")]

    def generate_date(self):
        """Génère la date du film à partir des données de base (nom avec date)."""
        name_and_date = self.film_data[self.NAME_AND_DATE_INDEX]
        return int(name_and_date[name_and_date.rfind(" (") + 2:name_and_date.rfind(")")])

    def generate_type(self):
        """Génère le type de support du film à partir des données de base (type de support)."""
        return self.film_data[self.TYPE_INDEX].upper()