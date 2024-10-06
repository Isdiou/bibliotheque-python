# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:25:05 2024

@author: Charles BURGY
"""
# On présente tout le code de la bibliothèque vu que la classe a subit des changements notament au niveau des attributs implicites

# On insère d'abord l'intégralité des classes préalablement implémantés lors du TD2

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ***** classe Personne *****
class Personne:
    def __init__(self,nom,prenom,adresse):
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        
    def __str__(self):
        return f"Classe Personne - Nom : {self.__nom}, Prenom : {self.__prenom}, Adresse : {self.__adresse}"
        
    def set_nom(self,nom):
        self.__nom = nom
        
    def get_nom(self):
        return self.__nom
        
    def set_prenom(self,prenom):
        self.__prenom = prenom
        
    def get_prenom(self):
        return self.__prenom
        
    def set_adresse(self,adresse):
        self.__adresse = adresse
        
    def get_adresse(self):
        return self.__adresse

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ***** classe Livre *****          
class Livre:
    def __init__(self,titre,auteur,numero,nb_total):
        self.__titre = titre        
        self.__auteur = auteur
        self.__numero = numero
        self.__nb_total = nb_total
        self.__nb_dispo = nb_total

    def set_auteur(self,auteur):
        self.__auteur = auteur
        
    def get_auteur(self):
        return self.__auteur
        
    def set_titre(self,titre):
        self.__titre = titre
        
    def get_titre(self):
        return self.__titre
        
    def set_numero(self,numero):
        self.__numero = numero
        
    def get_numero(self):
        return self.__numero
    
    def set_nb_total(self,nb_total):
        self.__nb_total = nb_total
        
    def get_nb_total(self):
        return self.__nb_total

    def set_nb_dispo(self,nb_dispo):
        self.__nb_dispo = nb_dispo
        
    def get_nb_dispo(self):
        return self.__nb_dispo
        
    def __str__(self):
        return 'Livre - Auteur : {}, Titre : {}, Numero : {}, Nb total : {}, Nb dispo : {}'.format(self.__auteur,self.__titre,self.__numero,self.__nb_total,self.__nb_dispo)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ***** classe Lecteur *****        
class Lecteur(Personne):
    def __init__(self,nom,prenom,adresse,numero):
        Personne.__init__(self,nom,prenom,adresse)        
        self.__numero = numero
        self.__nb_emprunts = 0
        
    def set_numero(self,numero):
        self.__numero = numero
        
    def get_numero(self):
        return self.__numero
        
    def set_nb_emprunts(self,nb_emprunts):
        self.__nb_emprunts = nb_emprunts
        
    def get_nb_emprunts(self):
        return self.__nb_emprunts
        
    def __str__(self): #Permet d'afficher les proprietes de l'objet avec la fonction print
        return 'Lecteur - Nom : {}, Prenom : {}, Adresse : {}, Numero : {}, Nb emprunts : {}'.format(self.get_nom(),self.get_prenom(),self.get_adresse(),self.__numero,self.__nb_emprunts)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
      
# ***** classe Bibliotheque *****
class Bibliotheque:
    def __init__(self,nom):
        self.__nom = nom
        self.__lecteurs = []
        self.__livres = []
        self.__emprunts = []
        self.__bibliothecaires=[]
        self.__conservateur=[]
        
    def get_nom(self):
        return self.__nom
        
    def ajout_lecteur(self,nom,prenom,adresse,numero):
        self.__lecteurs.append(Lecteur(nom,prenom,adresse,numero))
        
    def retrait_lecteur(self,numero):
        # On cherche le lecteur
        lecteur = self.chercher_lecteur_numero(numero)
        if lecteur == None:
            return False
        # On verifie qu'il n'a pas d'emprunt en cours
        for e in self.__emprunts:
            if e.get_numero_lecteur()==numero:
                return False
        # On peut ici retirer le lecteur de la liste
        self.__lecteurs.remove(lecteur)
        return True                
                
    def ajout_livre(self,auteur,titre,numero,nb_total):
        self.__livres.append(Livre(auteur,titre,numero,nb_total))
    
    def retrait_livre(self,numero):
        # On cherche le livre
        livre = self.chercher_livre_numero(numero)
        if livre == None:
            return False
        # On verifie que le livre n'est pas en cours d'emprunt
        for e in self.__emprunts:
            if e.get_numero_livre()==numero:
                return False
        # On peut ici retirer le livre de la liste
        self.__livres.remove(livre)
        return True        
        
    def chercher_lecteur_numero(self,numero):
        for l in self.__lecteurs:
            if l.get_numero() == numero:
                return l
        return None

    def chercher_lecteur_nom(self,nom,prenom):
        for l in self.__lecteurs:
            if l.get_nom() == nom and l.get_prenom() == prenom:
                return l
        return None    
        
    def chercher_livre_numero(self,numero):
        for l in self.__livres:
            if l.get_numero() == numero:
                return l
        return None

    def chercher_livre_titre(self,titre):
        for l in self.__livres:
            if l.get_titre() == titre:
                return l
        return None    
        
    def chercher_emprunt(self, numero_lecteur, numero_livre,numero_bibliothecaire):
        for e in self.__emprunts:
            if e.get_numero_lecteur() == numero_lecteur and e.get_numero_livre() == numero_livre and e.get_numero_bibliothecaire() == numero_bibliothecaire:
                return e
        return None

    def emprunt_livre(self, numero_lecteur, numero_livre,numero_bibliothecaire):
        # On verifie que le numero de livre est valide
        livre = self.chercher_livre_numero(numero_livre)
        if livre == None:
            print('Emprunt impossible : livre inexistant')
            return None
            
        # On verifie qu'il reste des exemplaires disponibles pour ce livre
        if livre.get_nb_dispo() == 0:
            print('Emprunt impossible : plus d\'exemplaires disponibles')
            return None
            
        # On verifie que le numero de lecteur est valide
        lecteur = self.chercher_lecteur_numero(numero_lecteur)
        if lecteur == None:
            print('Emprunt impossible : lecteur inexistant')
            return None
        # On verifie que ce lecteur n'a pas deja emprunte ce livre
        e = self.chercher_emprunt(numero_lecteur, numero_livre,numero_bibliothecaire)
        if e != None:
            print('Emprunt impossible : deja en cours')
            return None

        # On verifie que le numero de bibliothecaire est valide
        bibliothecaire = self.chercher_bibliothecaire(numero_bibliothecaire)
        if bibliothecaire == None:
            print('Emprunt impossible : lecteur inexistant')
            return None


        # Les conditions sont reunies pour pouvoir faire cet emprunt            
        self.__emprunts.append(Emprunt(numero_lecteur, numero_livre,numero_bibliothecaire))
        livre.set_nb_dispo(livre.get_nb_dispo()-1)
        lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()+1)
        return self.__emprunts[-1]

    def retour_livre(self, numero_lecteur, numero_livre, numero_bibliothecaire):
        # On recherche l'emprunt identifie par le numero de livre et de lecteur
        e = self.chercher_emprunt(numero_lecteur, numero_livre, numero_bibliothecaire)
        if e != None: # l'emprunt existe, on le retire de la liste et on met a jour nb_emprunt pour le lecteur et nb_dispo pour le livre
            self.__emprunts.remove(e)
            lecteur = self.chercher_lecteur_numero(numero_lecteur)
            if lecteur != None : lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()-1)
            livre = self.chercher_livre_numero(numero_livre)
            if livre != None: livre.set_nb_dispo(livre.get_nb_dispo()+1)
            print('Retour effectue')
            return True
        else:
            print('Aucun emprunt ne correspond a ces informations')
            return False
        
    def affiche_lecteurs(self):
        for l in self.__lecteurs:
            print(l)

    def affiche_livres(self):
        for l in self.__livres:
            print(l)           
            
    def affiche_emprunts(self):
        for e in self.__emprunts:
            print(e)     
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# méthodes supplémentaires implémantés dans la classe bibliothèque

    # Ajoute un bibliothécaire à la liste des bibliothécaires de la bibliothèque
    def ajout_bibliothecaire(self, nom, prenom, adresse, numero):
        # Création d'une instance de la classe Bibliothecaire
        a = Bibliothecaire(nom, prenom, adresse, numero)
        # Ajout de ce bibliothécaire à la liste privée __bibliothecaires
        self.__bibliothecaires.append(a)

    # Recherche un bibliothécaire par son numéro de bibliothécaire
    def chercher_bibliothecaire(self, numero):
        # Parcourt tous les bibliothécaires dans la liste __bibliothecaires
        for x in self.__bibliothecaires:
            # Si le numéro de bibliothécaire correspond à celui passé en paramètre, on retourne le bibliothécaire
            if x.get_nb_bibliothecaire() == numero:
                return x
        # Si aucun bibliothécaire n'a été trouvé avec ce numéro, retourne None
        return None

    # Retire un bibliothécaire de la liste en fonction de son numéro
    def retrait_bibliotecaire(self, numero):
        # Recherche du bibliothécaire à retirer via son numéro
        x = self.chercher_bibliothecaire(numero)
        # Parcourt la liste des bibliothécaires pour trouver l'index du bibliothécaire à retirer
        for j in range(len(self.__bibliothecaires)):
            # Si l'élément à l'index j correspond au bibliothécaire à retirer
            if self.__bibliothecaires[j] == x:
                # On crée une nouvelle liste en excluant le bibliothécaire correspondant
                self.__bibliothecaires = self.__bibliothecaires[:j] + self.__bibliothecaires[j+1:]

    # Affiche tous les bibliothécaires de la bibliothèque
    def affiche_bibliothecaire(self):
        # Parcourt tous les bibliothécaires de la liste et les affiche
        for v in self.__bibliothecaires:
            print(v)

    # Définit un conservateur pour la bibliothèque (remplace l'ancien conservateur)
    def definir_conservateur(self, nom, prenom, adresse):
        # Crée une nouvelle instance de Conservateur et remplace le précédent conservateur
        # Le conservateur est lié au nom de la bibliothèque (self.__nom)
        self.__conservateur = [Conservateur(nom, prenom, adresse, self.__nom)]

    # Affiche le conservateur actuel de la bibliothèque
    def affiche_conservateur(self):
        # Parcourt la liste des conservateurs et les affiche (en principe il n'y a qu'un seul conservateur)
        for h in self.__conservateur:
            print(h)

            
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ceci est la partie concernant la classe bibliothècaire :

# ***** classe Bibliothecaire *****
class Bibliothecaire(Personne):
    
    def __init__(self, nom, prenom, adresse, numero_bibliothecaire):
        Personne.__init__(self,nom, prenom, adresse)
        self.__nb = numero_bibliothecaire
        
    def get_nb_bibliothecaire(self):
        """Retourne le numéro de bibliothécaire."""
        return self.__nb
    
    def set_nb_bibliothecaire(self, nb):
        """Met à jour le numéro de bibliothécaire."""
        self.__nb = nb

    def __str__(self):
        """Retourne une représentation en chaîne du bibliothécaire."""
        return ('Information du bibliothécaire : Nom : {}, Prénom : {}, Adresse : {}, '
                'Numéro de Bibliothécaire : {}'.format(self.get_nom(), self.get_prenom(),self.get_adresse(), self.__nb))
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ceci est la partie concernant la classe Emprunt (modifiée dans son constructeur et dans ses méthodes du fait de son association avec la classe Bibliothecaire):

from datetime import date

# ***** classe Emprunt *****        
class Emprunt:
    
    # Le constructeur de la classe Emprunt. Il prend en entrée le numéro du lecteur, du livre, et du bibliothécaire.
    def __init__(self, numero_lecteur, numero_livre, numero_bibliothecaire):
        # Stocke le numéro du lecteur ayant effectué l'emprunt dans un attribut privé.
        self.__numero_lecteur = numero_lecteur
        # Stocke le numéro du livre emprunté dans un attribut privé.
        self.__numero_livre = numero_livre
        # Stocke le numéro du bibliothécaire responsable de l'emprunt dans un attribut privé.
        self.__numero_bibliothecaire = numero_bibliothecaire
        # Stocke la date de l'emprunt, qui est la date actuelle, dans un format ISO (AAAA-MM-JJ).
        self.__date = date.isoformat(date.today())

    # Méthode pour obtenir le numéro du lecteur ayant effectué l'emprunt.
    def get_numero_lecteur(self):
        return self.__numero_lecteur
        
    # Méthode pour obtenir le numéro du livre emprunté.
    def get_numero_livre(self):
        return self.__numero_livre
        
    # Méthode pour obtenir la date de l'emprunt.
    def get_date(self):
        return self.__date
    
    # Méthode pour obtenir le numéro du bibliothécaire responsable de l'emprunt.
    def get_numero_bibliothecaire(self):
        return self.__numero_bibliothecaire

    # Méthode spéciale __str__ pour afficher les détails de l'emprunt sous forme de chaîne de caractères.
    def __str__(self):
        # Renvoie une chaîne formatée contenant les informations de l'emprunt : numéro du lecteur, numéro du livre, date de l'emprunt, et bibliothécaire référent.
        return 'Emprunt - Numero lecteur : {}, Numero livre: {}, Date : {}, Bibliothécaire Référent : {}'.format(
            self.__numero_lecteur, self.__numero_livre, self.__date, self.__numero_bibliothecaire)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ceci est la partie concernant la classe Conservateur 


# ***** classe Conservateur ***** 
class Conservateur(Personne):
    # La classe Conservateur hérite de la classe Personne
    # Le constructeur de la classe Conservateur. Il prend les paramètres nom, prenom, adresse et nom_bibliotheque.
    def __init__(self, nom, prenom, adresse, nom_bibliotheque):
        # Appelle le constructeur de la classe parent (Personne) pour initialiser nom, prenom et adresse.
        Personne.__init__(self, nom, prenom, adresse)
        # Attribue le nom de la bibliothèque à l'attribut privé __nom_bibliotheque.
        self.__nom_bibliotheque = nom_bibliotheque
        
    # Méthode pour récupérer le nom de la bibliothèque où travaille le conservateur.
    def get_nom_bibliotheque(self):
        return self.__nom_bibliotheque

    # Méthode pour définir ou modifier le nom de la bibliothèque où travaille le conservateur.
    def set_nom_bibliotheque(self, nb):
        self.__nom_bibliotheque = nb

    # Redéfinition de la méthode __str__ pour afficher les informations du conservateur sous forme de chaîne de caractères.
    def __str__(self):
        # Renvoie une chaîne formatée contenant les informations sur le conservateur : nom, prénom, adresse et la bibliothèque.
        return 'Informations du conservateur : Nom : {}; Prénom : {}; Adresse : {}; Bibliothèque de fonction : {}'.format(
            self.get_nom(), self.get_prenom(), self.get_adresse(), self.__nom_bibliotheque)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#Ci dessous les tests des differentes classes : 
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------

# Test de la classe Bibliothecaire
def test_bibliothecaire():
    # Création de trois objets Bibliothecaire avec différents paramètres
    bibliothecaire1 = Bibliothecaire("Dupont", "Jean", "123 Rue Principale", 1001)
    bibliothecaire2 = Bibliothecaire("Martin", "Alice", "456 Rue des Fleurs", 1002)
    bibliothecaire3 = Bibliothecaire("Durand", "Pierre", "789 Rue du Parc", 1003)

    # Test des méthodes get_nb_bibliothecaire()
    assert bibliothecaire1.get_nb_bibliothecaire() == 1001, "Erreur dans get_nb_bibliothecaire pour bibliothecaire1"
    assert bibliothecaire2.get_nb_bibliothecaire() == 1002, "Erreur dans get_nb_bibliothecaire pour bibliothecaire2"
    assert bibliothecaire3.get_nb_bibliothecaire() == 1003, "Erreur dans get_nb_bibliothecaire pour bibliothecaire3"

    # Test de la méthode set_nb_bibliothecaire() (modification du numéro de bibliothécaire)
    bibliothecaire1.set_nb_bibliothecaire(2001)
    assert bibliothecaire1.get_nb_bibliothecaire() == 2001, "Erreur dans set_nb_bibliothecaire pour bibliothecaire1"

    # Test des méthodes héritées de la classe Personne
    assert bibliothecaire1.get_nom() == "Dupont", "Erreur dans get_nom pour bibliothecaire1"
    assert bibliothecaire2.get_prenom() == "Alice", "Erreur dans get_prenom pour bibliothecaire2"
    assert bibliothecaire3.get_adresse() == "789 Rue du Parc", "Erreur dans get_adresse pour bibliothecaire3"

    # Test de la méthode __str__()
    print(str(bibliothecaire1))
    print(str(bibliothecaire2))
    print(str(bibliothecaire3))

    print("Tous les tests sont passés avec succès.")

# Lancement du test
if __name__ == "__main__":
    test_bibliothecaire()
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
# Test de la classe Emprunt (ici on teste la classe Emprunt modifiée pour vérifier son bon fonctionnement)
def test_emprunt():
    # Création de trois objets Emprunt avec différents paramètres
    emprunt1 = Emprunt(123, 456, 789)
    emprunt2 = Emprunt(111, 222, 333)
    emprunt3 = Emprunt(444, 555, 666)

    # Test des méthodes get_numero_lecteur()
    assert emprunt1.get_numero_lecteur() == 123, "Erreur dans get_numero_lecteur pour emprunt1"
    assert emprunt2.get_numero_lecteur() == 111, "Erreur dans get_numero_lecteur pour emprunt2"
    assert emprunt3.get_numero_lecteur() == 444, "Erreur dans get_numero_lecteur pour emprunt3"

    # Test des méthodes get_numero_livre()
    assert emprunt1.get_numero_livre() == 456, "Erreur dans get_numero_livre pour emprunt1"
    assert emprunt2.get_numero_livre() == 222, "Erreur dans get_numero_livre pour emprunt2"
    assert emprunt3.get_numero_livre() == 555, "Erreur dans get_numero_livre pour emprunt3"

    # Test des méthodes get_numero_bibliothecaire()
    assert emprunt1.get_numero_bibliothecaire() == 789, "Erreur dans get_numero_bibliothecaire pour emprunt1"
    assert emprunt2.get_numero_bibliothecaire() == 333, "Erreur dans get_numero_bibliothecaire pour emprunt2"
    assert emprunt3.get_numero_bibliothecaire() == 666, "Erreur dans get_numero_bibliothecaire pour emprunt3"

    # Test de la méthode get_date() (vérification de la date actuelle)
    today = date.isoformat(date.today())
    assert emprunt1.get_date() == today, "Erreur dans get_date pour emprunt1"
    assert emprunt2.get_date() == today, "Erreur dans get_date pour emprunt2"
    assert emprunt3.get_date() == today, "Erreur dans get_date pour emprunt3"

    # Test de la méthode __str__()
    print(str(emprunt1))
    print(str(emprunt2))
    print(str(emprunt3))

    print("Tous les tests sont passés avec succès.")

# Lancement du test
if __name__ == "__main__":
    test_emprunt()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          
# Test de la classe Conservateur
def test_conservateur():
    # Création de trois objets Conservateur avec différents paramètres
    conservateur1 = Conservateur("Lemoine", "Sophie", "12 Rue de la Paix", "Bibliothèque Nationale")
    conservateur2 = Conservateur("Leclerc", "Thomas", "34 Avenue des Arts", "Bibliothèque Municipale")
    conservateur3 = Conservateur("Dubois", "Marie", "56 Boulevard Saint-Germain", "Bibliothèque Universitaire")

    # Test des méthodes get_nom_bibliotheque()
    assert conservateur1.get_nom_bibliotheque() == "Bibliothèque Nationale", "Erreur dans get_nom_bibliotheque pour conservateur1"
    assert conservateur2.get_nom_bibliotheque() == "Bibliothèque Municipale", "Erreur dans get_nom_bibliotheque pour conservateur2"
    assert conservateur3.get_nom_bibliotheque() == "Bibliothèque Universitaire", "Erreur dans get_nom_bibliotheque pour conservateur3"

    # Test de la méthode set_nom_bibliotheque() (modification du nom de la bibliothèque)
    conservateur1.set_nom_bibliotheque("Nouvelle Bibliothèque Nationale")
    assert conservateur1.get_nom_bibliotheque() == "Nouvelle Bibliothèque Nationale", "Erreur dans set_nom_bibliotheque pour conservateur1"

    # Test des méthodes héritées de la classe Personne
    assert conservateur1.get_nom() == "Lemoine", "Erreur dans get_nom pour conservateur1"
    assert conservateur2.get_prenom() == "Thomas", "Erreur dans get_prenom pour conservateur2"
    assert conservateur3.get_adresse() == "56 Boulevard Saint-Germain", "Erreur dans get_adresse pour conservateur3"

    # Test de la méthode __str__()
    print(str(conservateur1))
    print(str(conservateur2))
    print(str(conservateur3))

    print("Tous les tests sont passés avec succès.")

# Lancement du test
if __name__ == "__main__":
    test_conservateur()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Test de la classe Bibliotheque
def test_bibliotheque():
    # Création d'une bibliothèque
    biblio = Bibliotheque("Bibliothèque Centrale")

    # Test ajout et retrait de lecteurs
    biblio.ajout_lecteur("Dupont", "Jean", "1 Rue de Paris", 123)
    biblio.ajout_lecteur("Martin", "Alice", "2 Avenue des Champs", 124)
    assert biblio.chercher_lecteur_numero(123) is not None, "Erreur dans ajout_lecteur"
    assert biblio.chercher_lecteur_numero(124) is not None, "Erreur dans ajout_lecteur"
    
    assert biblio.retrait_lecteur(123), "Erreur dans retrait_lecteur"
    assert biblio.chercher_lecteur_numero(123) is None, "Erreur dans retrait_lecteur"
    
    # Test ajout et retrait de livres
    biblio.ajout_livre("Victor Hugo", "Les Misérables", 1001, 5)
    biblio.ajout_livre("Jules Verne", "Voyage au centre de la Terre", 1002, 3)
    assert biblio.chercher_livre_numero(1001) is not None, "Erreur dans ajout_livre"
    assert biblio.chercher_livre_numero(1002) is not None, "Erreur dans ajout_livre"
    
    assert biblio.retrait_livre(1001), "Erreur dans retrait_livre"
    assert biblio.chercher_livre_numero(1001) is None, "Erreur dans retrait_livre"

    # Test emprunt de livre
    biblio.ajout_lecteur("Durand", "Pierre", "3 Rue du Lac", 125)
    biblio.ajout_livre("George Orwell", "1984", 1003, 2)
    biblio.ajout_bibliothecaire("Lemoine", "Sophie", "4 Rue des Fleurs", 101)
    emprunt = biblio.emprunt_livre(125, 1003, 101)
    assert emprunt is not None, "Erreur dans emprunt_livre"
    
    # Test retour de livre
    assert biblio.retour_livre(125, 1003, 101), "Erreur dans retour_livre"
    
    # Test ajout et affichage de bibliothécaires
    biblio.ajout_bibliothecaire("Leclerc", "Thomas", "5 Avenue des Arts", 102)
    biblio.affiche_bibliothecaire()

    # Test ajout et affichage de conservateurs
    biblio.definir_conservateur("Dupuis", "Claire", "6 Boulevard de l'Opéra")
    biblio.affiche_conservateur()

    # Affichage des emprunts, lecteurs et livres restants
    biblio.affiche_lecteurs()
    biblio.affiche_livres()
    biblio.affiche_emprunts()

    print("Tous les tests sont passés avec succès.")

# Lancement du test
if __name__ == "__main__":
    test_bibliotheque()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#****** FIN DU CODE ******

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------