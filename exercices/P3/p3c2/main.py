"""Programme principal pour gérer une bibliothèque de films."""

from pprint import pprint
from films.library import Library
from films.friend import FriendClean

def main():
    library = Library()

    films = library.films
    pprint(films)
    print("--------\nListe des films dans la bibliothèque :\n")
    for film in films:
        print(film)

    friends = FriendClean().list_friends_from_data(library)
    print("--------")
    pprint(friends)
    print("--------\nListe des amis :\n")
    for friend in friends:
        print(friend)

    library.sort_by_type()
    print("--------\nMes films triés par type:\n")
    for film in films:
        print(film)

    film = library.get_random_film()
    print(f"--------\nFilm récupéré au hasard: {film}")
    print()

    films_lent = library.get_lent_films()
    print("--------\nJ'ai prêté ces films:\n")
    for film in films_lent:
        print(f"Le film '{film}' est chez", film.where)

if __name__ == "__main__":
    main()