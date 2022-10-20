class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'Your username is {self.username} and your password is {self.password}'


andrew = User('atmakings', 'badpassword')
print(str(andrew))