from Compte import Compte, CompteCourant, CompteEpargne

if __name__ == '__main__':
    print("Let's start coding our bank application !")

# Création de 2 comptes pour le test
compte_courant = CompteCourant("Jean", solde=1200, autorisation_decouvert=500, pourcentage_agios=2.5)
compte_epargne = CompteEpargne("Jean", solde=1200, pourcentage_interets=3.5)

# Interface Console
sortie = False
while not sortie:
    print("----------------------------------------------------------------\n")
    print(compte_courant)
    print(compte_epargne)
    choix = input("Sur quel compte souhaitez vous faire une opération?(courant ou epargne)\n")
    montant = float(input(
        "Quel est le montant de l'opération que vous souhaitez effectuez? (montant positif pour un versement/montant négatif pour un retrait)"))
    match choix:
        case 'courant':
            print('*********************************************************************************')
            print(compte_courant)
            print('*********************************************************************************')
            if montant < 0:
                try:
                    compte_courant.retrait(abs(montant))
                    print(
                        "{} à été retiré du compte courant n°{} de {}\n".format(abs(montant),
                                                                                compte_courant.numero_compte,
                                                                                compte_courant.nom_proprietaire))
                except:
                    print("RETRAIT IMPOSSIBLE! FOND INSUFFISANT!")
            else:
                compte_courant.versement(montant)
                print("{} à été versé sur le compte courant n°{} de {}\n".format(montant, compte_courant.numero_compte,
                                                                                 compte_courant.nom_proprietaire))
                print('*********************************************************************************')
                print(compte_courant)
                print('*********************************************************************************')
        case 'epargne':
            print('*********************************************************************************')
            print(compte_epargne)
            print('*********************************************************************************')
            if montant < 0:
                try:
                    compte_epargne.retrait(abs(montant))
                    print(
                        "{} à été retiré du compte épargne n°{} de {}\n".format(abs(montant),
                                                                                compte_epargne.numero_compte,
                                                                                compte_epargne.nom_proprietaire))
                except:
                    print("RETRAIT IMPOSSIBLE! FOND INSUFFISANT!")
            else:
                compte_epargne.versement(montant)
                print("{} à été versé sur le compte épargne n°{} de {}\n".format(abs(montant),
                                                                                 compte_epargne.numero_compte,
                                                                                 compte_epargne.nom_proprietaire))
                print('*********************************************************************************')
                print(compte_epargne)
                print('*********************************************************************************')

        case _:
            print("ERREUR DE SAISIE\n")  # TODO raise Exception("ERREUR DE SAISIE\n")

    choix = input("Souhaitez-vous effectuer une autre opération?(o/n)\n")
    match choix:
        case 'o':
            sortie = False
        case 'n':
            sortie = True
        case _:
            print("ERREUR DE SAISIE\n")  # TODO raise Exception("ERREUR DE SAISIE\n")
