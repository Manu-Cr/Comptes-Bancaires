# POEC Développement Cybersécurité  / EPSI

# Exercice sur les Comptes bancaires

## Contenu

-Compte.py contient la classe abstraite CompteCourant ainsi que ses classes filles CompteCourant et CompteEpargne,
 leurs attributs et leurs methods

-main.py contient l'interface console avec la demande du compte sur lequel faire une opération, et le montant de la transaction.

-test_unitaire est un jeu de test pour Compte.py

## Sujet

Ecrire un programme qui implémente en POO un fonctionnement bancaire basique :  

- une classe abstraite `Compte` 
    - **attributs :** numero_compte, nom_proprietaire, solde  
    - **méthodes :** retrait, versement, afficher_solde  

- une classe fille `CompteCourant`, qui ajoute une gestion du découvert (montant maximum négatif 
possible) et des agios (pénalité de X % si le solde est inférieur à zéro) :  
    - **attributs :** autorisation_decouvert, pourcentage_agios  
    - **méthodes :** appliquer_agios  

- une classe fille `CompteEpargne`, qui ajoute :  
    - **attributs :** pourcentage_interets  
    - **méthodes :** appliquer_interets  
    

Le programme doit demander à l’utilisateur le compte concerné (« courant » ou « epargne ») et le montant 
de la transaction (positif pour un versement, négatif pour un retrait)  

Chaque appel de méthode doit afficher le solde avant opération, le détail de l’opération et le solde après 
opération. On suppose pour la simplicité de l’exercice que chaque modification du solde applique les agios 
ou intérêts du compte modifié.
