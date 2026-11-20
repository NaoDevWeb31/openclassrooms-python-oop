class Film:
    def __init__(self, name):
        self.name = name

    def watch(self, player):
        print("Bon visionnage !")

class FilmCassette(Film):
    def __init__(self, name):
        """Initialise le nom et la bande magnétique."""
        super().__init__(name)
        self.magnetic_tape = True

    def rewind(self):
        """Rembobine la bande magnétique."""
        print("C'est long à rembobiner !")
        self.magnetic_tape = True

    def watch(self, player):
        """Regarde le film"""
        if player.type != "cassette":
            print(
                "Le lecteur n'est pas un lecteur de cassettes !",
                "Vous en trouverez peut-être un dans le grenier..?"
            )
        else:
            print("Ça commence ! Allumez votre TV cathodique. :)")
        super().watch(player)

class Player:
    """Un lecteur."""

    def __init__(self, type):
        """Possède un type."""
        self.type = type

film = Film("2001: L'Odyssée de l'espace")
film_cassette = FilmCassette("Blade Runner")

film.name
film.watch(Player("cassette"))

print(film_cassette.name)
print(film_cassette.magnetic_tape)
player = Player("DVD")
film_cassette.watch(player)
film_cassette.rewind()