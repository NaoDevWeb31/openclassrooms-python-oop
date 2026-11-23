class User:
    """Un utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom d'utilisateur et le mot de passe."""
        if not username or username == "":
            raise EmptyUsernameException(username)
        if not password or password == "":
            raise EmptyPasswordException(password)
        if len(username) < 3:
            raise TooShortUsernameException(username)
        if len(password) < 6:
            raise TooShortPasswordException(password)

        self.username = username
        self.password = password

class EmptyUsernameException(Exception):
    """Exception levée lorsque le nom d'utilisateur est vide."""
    def __init__(self, username, message="", *args, **kwargs):
        """Initialise le message."""
        message = message or f"Le nom d'utilisateur {username} est obligatoire !"
        super().__init__(message, *args, **kwargs)

class TooShortUsernameException(Exception):
    """Exception levée lorsque le nom d'utilisateur est trop court."""
    def __init__(self, username, message="", *args, **kwargs):
        """Initialise le message."""
        message = message or f"Le nom d'utilisateur {username} est trop court !"
        super().__init__(message, *args, **kwargs)

class EmptyPasswordException(Exception):
    """Exception levée lorsque le mot de passe est vide."""
    def __init__(self, password, message="", *args, **kwargs):
        """Initialise le message."""
        message = message or f"Le mot de passe {password} est obligatoire !"
        super().__init__(message, *args, **kwargs)

class TooShortPasswordException(Exception):
    """Exception levée lorsque le mot de passe est trop court."""
    def __init__(self, password, message="", *args, **kwargs):
        """Initialise le message."""
        message = message or f"Le mot de passe {password} est trop court !"
        super().__init__(message, *args, **kwargs)


if __name__ == "__main__":
    user = User("John", "supersecret")
    try:
        user = User("", "supersecret")
    except EmptyUsernameException:
        print("L'exception sur le nom d'utilisateur vide a été levée.")
    except TooShortUsernameException:
        print("L'exception sur le nom d'utilisateur trop court a été levée.")

    try:
        user = User("John", "t")
    except EmptyPasswordException:
        print("L'exception sur le mot de passe vide a été levée.")
    except TooShortPasswordException:
        print("L'exception sur le mot de passe trop court a été levée.")