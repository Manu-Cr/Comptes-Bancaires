"""
Test Unitaire pour Compte Courant et Compte Epargne
"""
from random import randrange

import pytest

from Compte import Compte, CompteCourant, CompteEpargne

@pytest.mark.cc
class TestCompteCourant():
    """Test Unitaire pour Compte Courant. """

    @pytest.fixture
    def compte_courant(selfself) -> CompteCourant:
        """Génère un Compte Courant"""
        return CompteCourant("Manu")

    def test_cc_a_un_solde_a_zero_par_defaut(selfself, compte_courant:CompteCourant) -> None:
        """Par défaut un nouveau compte créé à un solde égal à zéro"""
        assert compte_courant.solde == 0

    def test_cc_un_versement(self,compte_courant :CompteCourant) ->\
            None:
        """ Test de versement """
        montant = 150
        compte_courant.versement(montant)
        assert compte_courant.solde == montant

    def test_cc_versement_negatif(self, compte_courant: CompteCourant) -> None:
        """Test d'un nombre négatif en paramètre de versement"""
        montant = -200
        with pytest.raises(Exception):
            compte_courant.versement(montant)


    def test_cc_retrait_autorisé(self, compte_courant: CompteCourant) -> None:
        """Test de retrait"""
        montant = 100
        compte_courant.versement(montant)
        compte_courant.retrait(montant)

        assert compte_courant.solde == 0

    def test_cc_retrait_negatif(selfself, compte_courant: CompteCourant) -> None:
        """Test d'un nombre négatif en paramètre de retrait"""
        montant = -100
        with pytest.raises(Exception):
            compte_courant.retrait(montant)






