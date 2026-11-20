from abc import ABC

class File(ABC):
    """Fichier."""

    def __init__(self, name, size):
        """Initialise le nom et la taille."""
        self.name = name
        self.size = size

    def display(self):
        """Affiche le fichier."""
        pass

class ImageFile(File):
    """Fichier d'image."""

    def display(self):
        """Affiche l'image."""
        print(f"Fichier image '{self.name}'.")

class ImageFileGIF(ImageFile):
    """Fichier d'image GIF."""

    def display(self):
        """Affiche l'image."""
        super().display()
        print("L'image est de type 'GIF'.")

class ImageFilePNG(ImageFile):
    """Fichier d'image PNG."""

    def display(self):
        """Affiche l'image."""
        super().display()
        print("L'image est de type 'PNG'.")

class User:
    """Utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom d'utilisateur et le mot de passe."""
        self.username = username
        self.password = password

    def login(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(content=content, user=self, publish_date="Aujourd'hui", file=file)
        else:
            post = Post(content=content, user=self, publish_date="Aujourd'hui")
        thread.add_post(post)
        return post

    def create_thread(self, title, content):
        """Créé un nouveau fil de discussion."""
        post = Post(content=content, user=self, publish_date="Aujourd'hui")
        thread = Thread(title=title, creation_date="Aujourd'hui", post=post)
        return thread

    def __str__(self):
        """représentation de l'utilisateur."""
        return self.username

class Moderator(User):
    """Utilisateur modérateur."""

    def edit(self, post, content):
        """Modifie un message."""
        post.content = content

    def delete(self, thread, post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]

class Post:
    """Message."""

    def __init__(self, content, user, publish_date):
        """Initialise le contenu, l'utilisateur et la date de publication."""
        self.content = content
        self.user = user
        self.publish_date = publish_date

    def display(self):
        """Affiche le message."""
        print(f"Message posté par {self.user} le {self.publish_date}:")
        print(self.content)


class FilePost(Post):
    """Message comportant un fichier."""

    def __init__(self, content, user, publish_date, file):
        """Initialise le fichier."""
        super().__init__(content, user, publish_date)
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display()
        print("pièce jointe:")
        self.file.display()

class Thread:
    """Fil de discussions."""

    def __init__(self, title, creation_date, post):
        """Initialise le titre, la date de création et le premier message."""
        self.title = title
        self.creation_date = creation_date
        self.posts = [post]

    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.creation_date}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.posts.append(post)
