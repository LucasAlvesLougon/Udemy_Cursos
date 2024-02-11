# method vs  @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe 
# @staticmethod - método estático(❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

# conta1 = Connection()
conta1 = Connection.create_with_auth('lucas', '123')
# conta1.set_user('luiz')
# conta1.set_password('123')
print(conta1.user)
print(conta1.password)