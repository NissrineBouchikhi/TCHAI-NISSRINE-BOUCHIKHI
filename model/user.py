class User(object):

    def __init__(self, userNom: str = None, montantInitial: float = None):
        self.userNom = userNom
        self.montantInitial = montantInitial

    @property
    def userNom(self):
        return self.__userNom

    @userNom.setter
    def userNom(self, nom):
        self.userNom = nom

    @property
    def montantInitial(self):
        return self.__montantInitial

    @montantInitial.setter
    def montantInitial(self, montant):
        self.montantInitial = montant

    def __dict__(self):
        return {"userNom": self.userNom, "montantInitial": self.montantInitial}