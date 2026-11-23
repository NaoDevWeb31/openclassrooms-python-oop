"""Définit les amis."""

from .data import friends

class Friend:
    """Ami."""

    def __init__(self, name, film=None):
        """Initialise l'ami avec un nom et un film prêté (optionnel)."""
        self.name = name
        self.film = film
        if film is not None:
            film.where = self

    def __str__(self):
        """Représentation d'un ami."""
        return f"{self.name}"

class FriendClean:
    """Génère un ami à partir de données de base (nom, film)."""

    """Constantes pour les indices des données de base dans le tableau friends."""
    NAME_INDEX = 0
    FILM_INDEX = 1

    def __init__(self):
        """Initialise les données des amis."""
        self.friends = friends

    def generate_friend(self, data, library):
        """Génère un ami à partir des données de base (nom, film)."""
        name = data[self.NAME_INDEX]

        if len(data) > self.FILM_INDEX:
            film_name = data[self.FILM_INDEX]
            film = library.find_film_by_name(film_name)
        else:
            film = None

        return Friend(name, film)

    def list_friends_from_data(self, library):
        """Retourne une liste d'amis générés à partir des données de base."""

        friends_list = []
        for friend_data in self.friends:
            friend = self.generate_friend(friend_data, library)
            friends_list.append(friend)
        return friends_list