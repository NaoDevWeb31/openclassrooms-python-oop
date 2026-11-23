class Wings:
    def fly(self):
        print("Je vole")

class Parrot:
    def __init__(self):
        self.wings = Wings()

class Penguin:
    pass # problème : les pingouins ne peuvent pas voler

parrot = Parrot()
parrot.wings.fly()
