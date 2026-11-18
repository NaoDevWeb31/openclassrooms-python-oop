"""Définit le contact par chouette."""

from exercices.P3.p3c1_solution.contact.abstract import ContactSystem
from exercices.P3.p3c1_solution.contact.helpers import verify_adress


class OwlContactSystem(ContactSystem):
    """Envoi un message en utilisant une chouette ! 🧙‍♂️"""

    def __init__(self, address):
        """Initialise l'adresse."""
        verify_adress(address)
        self.address = address
        self.owl = "Hedwige"
        super().__init__()

    def send(self, message):
        """Envoi le message."""
        print(f'Envoi du message "{message}" par chouette {self.owl}')

    def __str__(self):
        """Représentation."""
        return f"L'addresse est '{self.address}'"
