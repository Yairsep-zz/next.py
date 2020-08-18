class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided argument %s is not a positive integer." % self._arg
    def get_arg(self):
        return self._arg

class UsernameTooShort(Exception):

class UsernameTooLong(Exception):

class PasswordMissingCharacter(Exception):

class PasswordTooShort(Exception):

class PasswordTooLong(Exception):


def checkUsername(username):
    if len(username) > 16:
        raise UsernameTooLong()
    if len(username) < 3:
        raise UsernameTooShort()
    if username


def checkPassword(password):



def check_input(username, password):
    if checkUsername(username):
        if checkPassword(password:
            print('OK')

def main():
    pass

if __name__ == "__main__":
    main()