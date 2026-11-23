def get_half_even_number(number):
    if number % 2 == 0:
        return number / 2
    else:
        message = (
        f"This Function only supports halving even numbers. Received: {number}"
        )
        raise Exception(message) # lancer des exceptions personnalisées dans nos propres programmes

def increase_percent(initial_value, after_value):
    """Gérer les exceptions lors du calcul de l’augmentation (ou la réduction) du pourcentage avec try-except."""
    try:
        return (after_value / initial_value) * 100
    except ZeroDivisionError:
        return 0
    except Exception as error:
        print("Uh oh, unexpected error occurred!")
        raise error

class InvalidAddressException(Exception):
    """Gère les exceptions liées aux mauvaises adresses."""

    def __init__(self, address, base_message="Adresse invalide !", *args, **kwargs):
        """Initialise le message.


        L’utilisation de *args et **kwags permet de prendre un nombre
        de paramètres dynamiques.
        """
        msg = f"{base_message} Adresse: {address}"
        super().__init__(msg, *args, **kwargs)

from exercices.P3.p3c1.contact.contactsystem import ContactSystem
from exercices.P3.p3c1.contact.helpers import verify_address

class OwlContactSystem(ContactSystem):
    def __init__(self, address):
        if (not verify_address(address)):
            raise InvalidAddressException(f"Adresse invalide: {address}")
        self.address = address

class MyAppException(Exception):
    """Classe de base pour notre hiérarchie d’exceptions personnalisées car les exceptions personnalisées dans une grosse application n’héritent habituellement pas directement d’exception"""
    pass


class MyAppInvalidAddressException(MyAppException):
    pass