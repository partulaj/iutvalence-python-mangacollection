class DatabaseConnectionError:

    def __init__(self, mess):
        self.mess = mess
    def __str__(self):
        return self.mess
