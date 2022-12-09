import datetime

from model.user import User


class Transaction():

    def __init__(self, user1: User = None, user2: User = None, montant: float = None, date: datetime = None):
        self.user1 = user1
        self.user2 = user2
        self.montant = montant
        self.date = date

    @property
    def user1(self):
        return self.user1

    @user1.setter
    def user1(self, user1):
        self.user1 = user1

    @property
    def user2(self):
        return self.user2

    @user1.setter
    def user2(self, user2):
        self.user2 = user2

    @property
    def montant(self):
        return self.montant

    @montant.setter
    def montant(self, date):
        self.date = date

    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, date):
        self.date = date

    def __dict__(self) -> dict:
        return {"userNom1": self.user1.userNom,
                "userNom2": self.user2.userNom,
                "montant": self.montant,
                "date": self.date}

    def __str__(self) -> str:
        return f'{self.user1.userNom} a envoyé {self.montant} à {self.user2.userNom} à la date de {self.date} '
