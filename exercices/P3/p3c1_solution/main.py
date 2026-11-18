"""Point d'entrée."""

from exercices.P3.p3c1_solution.contact.user import User
from exercices.P3.p3c1_solution.contact.owlcontact import OwlContactSystem
from exercices.P3.p3c1_solution.contact.textcontact import TextContactSystem
from exercices.P3.p3c1_solution.contact.helpers import send_mass_messages


def main():
    """Main function."""
    alice = User("Alice", TextContactSystem("0102030405"))
    bob = User("Bob", OwlContactSystem("4 Privet Drive"))

    user_list = [alice, bob]
    send_mass_messages("Hello {name}, Comment vas-tu?", user_list)
    send_mass_messages(
        "Salut {name}. Tes informations de contact sont-elles corrects?"
        " Nous avons celles-ci: {contact_info}.",
        user_list,
    )


if __name__ == "__main__":
    main()
