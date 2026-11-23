"""Définit la bibliothèque virtuelle de films."""

import random
from .film import FilmClean
from .data import films

class Library:
    """Bibliothèque de films."""

    def __init__(self):
        """Initialise les films."""
        self.films = []
        for film_data in films:
            film = FilmClean(film_data).generate_film()
            film.where = self
            self.films.append(film)

        self.sort_by_date_and_name()

    def sort_by_date_and_name(self):
        """Trie les films par date et par nom."""
        self.films.sort(key=lambda film: (film.creation_date, film.name))

    def sort_by_type(self):
        """Trie les films par type."""
        self.films.sort(key=lambda film: film.type)

    def get_random_film(self):
        """Retourne un film au hasard."""
        return random.choice(self.films)

    def get_lent_films(self):
        """Retourne la liste des films prêtés."""

        lent_films = []
        for film in self.films:
            if film.where is not self: # le film n'est pas dans la bibliothèque
                lent_films.append(film)
        return lent_films

    def find_film_by_name(self, name):
        """Retourne un film si le nom correspond, sinon None."""
        for film in self.films:
            if name == film.name:
                return film
        return None