def calculation(a, b):
    return a * (1 - (b / 100))

def subtract_discount(price, discount): # nommer de façon logique
    return price * (1 - (discount / 100))

from exercices.P3.p3c1.contact import contact, owlcontact
from exercices.P3.p3c1.contact.textcontact import TextContactSystem

text = TextContactSystem("01234 567890")