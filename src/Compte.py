import uuid
from abc import ABC


class Compte(ABC):
    """
        Abstract class Compte
    """

    def __init__(self, nom_proprietaire, solde=0):
        """
        Constructeur de la classe Compte
        attributs : numero_compte, nom_proprietaire, solde
        """
        self._numero_compte = uuid.uuid4()
        self._nom_proprietaire = nom_proprietaire
        self._solde = solde

    def retrait(self, montant=0):
        '''
        Méthode retrait
        Prend un montant en paramètre et le soustrait au solde du compte.
        '''
        self._solde = self._solde - montant

    def versement(self, montant=0):
        """
        Méthode versement
        Prend un montant en paramètre et l'ajoute au solde du compte
        """
        self._solde = self._solde + montant

    def __str__(self):
        """
        Méthode pour afficher l'état du compte
        """
        return "Compte n°: {}\nPropriétaire: {}\nSolde: {}\n".format(self._numero_compte,
                                                                     self._nom_proprietaire, round(self._solde, 2))

    @property
    def solde(self):
        """getter solde"""
        return self._solde

    @solde.setter
    def solde(self, value):
        """setter solde"""
        self._solde=value

    @property
    def numero_compte(self):
        """getter numero_compte"""
        return self._numero_compte

    @property
    def nom_proprietaire(self):
        """getter nom_proprietaire"""
        return self._nom_proprietaire

class CompteCourant(Compte):
    """
    Class CompteCourant qui hérite de la class Compte
    Le compte courant gère la possibilité d'avoir un solde négatif avec une autorisation de découvert
    Ainsi que la gestion d'Agios, un pourcentage qui est retiré à chaque opération
    si le solde du compte se trouve dans le négatif.
    """

    def __init__(self, nom_proprietaire, solde=0, autorisation_decouvert=0, pourcentage_agios=0):
        """
        Constructeur de la class CompteCourant
        attributs : numero_compte, nom_proprietaire, solde, autorisation_decouvert, pourcentage_agios
        """
        super().__init__(nom_proprietaire, solde)
        self._autorisation_decouvert = autorisation_decouvert
        self._pourcentage_agios = pourcentage_agios

    def __str__(self):
        """
        Surcharge de la méthode __str__
        Affiche l'état du compte
        """
        return "Compte Courant n°: {}\nPropriétaire: {}\nSolde: {}\nDécouvert autorisé: {}\nPourcentage Agios: {}\n".format(
            self._numero_compte,
            self._nom_proprietaire,
            round(self._solde, 2),
            self._autorisation_decouvert,
            self._pourcentage_agios)

    def appliquer_agios(self):
        """
        Méthode appliquer_agios
        Retire le pourcentage d'agios sur le compte courant dès qu'une opération est effectuée alors que le solde du compte courant est en négatif.
        """
        if self._solde < 0:
            self._solde += self._solde * self._pourcentage_agios / 100

    def retrait(self, montant=0):
        """
        Surcharge Méthode retrait
        Prend un montant en paramètre et le soustrait au solde du compte si le nouveau solde ne dépasse pas le découvert autorisé.
        Applique les agios si le solde après retrait est dans le négatif
        """
        if montant < 0:
            raise ValueError("le montant doit être positif")
        if self._solde - montant < -self._autorisation_decouvert:
            raise Exception("RETRAIT IMPOSSIBLE, FONDS INSUFFISANT")
        else:
            self._solde -= montant
            self.appliquer_agios()

    def versement(self, montant=0):
        """
        Surcharge Méthode versement
        Prend un montant en paramètre et l' ajoute au solde du compte
        Applique les agios si le solde après versement est dans le négatif
        """
        if montant < 0:
            raise ValueError("le montant doit être positif")
        self._solde = self._solde + montant
        if self._solde < 0:
            self.appliquer_agios()

    @property
    def autorisation_decouvert(self):
        """getter autorisation_decouvert"""
        return self._autorisation_decouvert


    @autorisation_decouvert.setter
    def autorisation_decouvert(self, value):
        """setter autorisation_decouvert"""
        if value < 0:
            raise ValueError("autorisation de découvert doit être positif")
        self._autorisation_decouvert = value

    @property
    def pourcentage_agios(self):
        """getter pourcentage_agios"""
        return self._pourcentage_agios



class CompteEpargne(Compte):
    """
    Class CompteEpargne qui hérite de la class Compte
    Un compte épargne ne peut pas se retrouver avec un solde négatif.
    Le compte épargne génère des intérêts appliqués à chaque opération sur le compte épargne.
    """

    def __init__(self, nom_proprietaire, solde=0, pourcentage_interets=0):
        """
        Constructeur de la class CompteEpargne
        attributs : numero_compte, nom_proprietaire, solde, pourcentage_interets
        """
        super().__init__(nom_proprietaire, solde)
        self._pourcentage_interets = pourcentage_interets

    def __str__(self):
        """
        Surcharge de la méthode __str__
        Affiche l'état du compte
        """
        return "Compte Epargne n°: {}\nPropriétaire: {}\nSolde: {}\nTaux d'intérêts: {}\n".format(self._numero_compte,
                                                                                                  self._nom_proprietaire,
                                                                                                  round(self._solde, 2),
                                                                                                  self._pourcentage_interets)

    def appliquer_interets(self):
        """
        Méthode appliquer_interets
        Applique le pourcentage d'intérêts sur le compte épargne dès qu'une opération est effectuée.
        """
        if self._solde > 0:
            self._solde += self._solde * self._pourcentage_interets / 100

    def retrait(self, montant=0):
        """
        Surcharge Méthode retrait
        Prend un montant en paramètre et le soustrait au solde du compte si le nouveau solde reste positif.
        Applique les intérets après chaque retrait effectué.
        """
        if self._solde - montant < 0:
            raise Exception("RETRAIT IMPOSSIBLE, FONDS INSUFFISANT")
        else:
            self._solde -= montant
            self.appliquer_interets()

    def versement(self, montant=0):
        """
        Surcharge Méthode versement
        Prend un montant en paramètre et l' ajoute au solde du compte
        Applique les intérets à chaque versement
        """
        self._solde = self._solde + montant
        self.appliquer_interets()


