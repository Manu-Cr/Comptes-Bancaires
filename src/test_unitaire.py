"""
Test Unitaire pour Compte Courant et Compte Epargne
"""

import pytest

from Compte import Compte, CompteCourant, CompteEpargne


@pytest.mark.cc
class TestCompteCourant():
    """Test Unitaire pour Compte Courant. """

    @pytest.fixture
    def compte_courant(self) -> CompteCourant:
        """Génère un Compte Courant"""
        return CompteCourant("Manu")

    def test_cc_a_un_solde_a_zero_par_defaut(selfself, compte_courant: CompteCourant) -> None:
        """Par défaut un nouveau compte créé à un solde égal à zéro"""
        assert compte_courant.solde == 0

    def test_cc_un_versement(self, compte_courant: CompteCourant) -> \
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

    def test_cc_retrait_negatif(self, compte_courant: CompteCourant) -> None:
        """Test d'un nombre négatif en paramètre de retrait"""
        montant = -100
        with pytest.raises(Exception):
            compte_courant.retrait(montant)

    def test_cc_retrait_depassant_autorisation_decouvert(self, compte_courant: CompteCourant) -> None:
        """Test du dépassement de découvert"""
        montant = 200
        with pytest.raises(Exception):
            compte_courant.retrait(montant)

    def test_cc_agios_retrait(self, compte_courant: CompteCourant) -> None:
        """test du calcul d'agios lors d'un retrait où le solde se retrouve dans le négatif"""
        montant = 100
        compte_courant.set_autorisation_decouvert(100)
        compte_courant.set_pourcentage_agios(10)
        compte_courant.retrait(montant)

        assert compte_courant.solde == -110

    def test_cc_agios_versement(self, compte_courant: CompteCourant) -> None:
        """test du calcul d'agios lors d'un versement où le solde reste dans le négatif """
        montant = 100
        compte_courant.set_solde(-1000)
        compte_courant.set_autorisation_decouvert(1000)
        compte_courant.set_pourcentage_agios(10)
        compte_courant.versement(montant)

        assert compte_courant.solde == -990


@pytest.mark.ce
class TestCompteEpargne():
    """Test Unitaire pour Compte Epargne"""

    @pytest.fixture
    def compte_epargne(self) -> CompteEpargne:
        """Génère un Compte Epargne"""
        return CompteEpargne("Manu")

    def test_ce_a_un_solde_a_zero_par_defaut(selfself, compte_epargne: CompteEpargne) -> None:
        """Par défaut un nouveau compte créé à un solde égal à zéro"""
        assert compte_epargne.solde == 0

    def test_ce_versement(self, compte_epargne: CompteEpargne) -> \
            None:
        """ Test de versement sur compte épargne"""
        montant = 150
        compte_epargne.versement(montant)
        assert compte_epargne.solde == montant

    def test_ce_versement_negatif(self, compte_epargne: CompteEpargne) -> None:
        """Test d'un nombre négatif en paramètre de versement"""
        montant = -200
        with pytest.raises(Exception):
            compte_epargne.versement(montant)

    def test_ce_retrait_autorisé(self, compte_epargne: CompteEpargne) -> None:
        """Test de retrait"""
        montant = 100
        compte_epargne.versement(montant)
        compte_epargne.retrait(montant)

        assert compte_epargne.solde == 0

    def test_ce_retrait_negatif(self, compte_epargne: CompteEpargne) -> None:
        """Test d'un nombre négatif en paramètre de retrait"""
        montant = -100
        with pytest.raises(Exception):
            compte_epargne.retrait(montant)

    def test_ce_retrait_non_autorisé(self, compte_epargne: CompteEpargne) -> None:
        """Test du retrait refusé"""
        montant = 200
        with pytest.raises(Exception):
            compte_epargne.retrait(montant)

    def test_ce_interets_retrait(self, compte_epargne: CompteEpargne) -> None:
        """test du calcul d'intérets lors d'un retrait"""
        montant = 1000
        compte_epargne.set_solde(5000)
        compte_epargne.set_pourcentage_interets(10)
        compte_epargne.retrait(montant)
        assert compte_epargne.solde == 4400

    def test_ce_interets_versement(self, compte_epargne: CompteEpargne) -> None:
        """test du calcul d'intérets lors d'un versement """
        montant = 1000
        compte_epargne.set_solde(5000)
        compte_epargne.set_pourcentage_interets(10)
        compte_epargne.versement(montant)
        assert compte_epargne.solde == 6600
