"""Définit le système de contact par chouette."""
from .contactsystem import ContactSystem
from .helpers import verify_address

class OwlContactSystem(ContactSystem):
    """Envoi un message en utilisant une chouette ! 🧙‍♂️"""

    def __init__(self, address):
        """Initialise l'addresse."""
        verify_address(address)
        self.address = address
        self.owl = "Hedwige"
        super().__init__()

    def send(self, message):
        """Envoi le message."""
        print(f'Envoi du message "{message}" par chouette {self.owl}')

    def __str__(self):
        """Représentation."""
        return f"L'addresse est '{self.address}'"
