class Produit:
    def __init__(self, nom, quantite=0, prix=0, unite="p."):
        self.nom = nom
        self.quantite = quantite
        self.prix = prix
        self.unite = unite

     # Metodo per aggiornare la quantità a disposizione dopo l'acquisto
    def actualiser_la_quantite(self, a):
        self.quantite += a
        print(self.quantite)


class Facture(Produit):
    def __init__(self, nom, quantite, prix, unite, total = 0, n_facture=0, tva=0.15):
        super().__init__(nom, quantite, prix, unite)
        self.total = total
        self.n_facture = n_facture
        self.tva = tva


    # Metodo calcolo prezzo senza TVA
    def nouvelle_facture(self, liste_produits, quantite):
        if quantite > 0:
            self.total = (quantite * self.prix * self.tva) + quantite * self.prix
            produit_achete = [f"{quantite}   {self.nom}   {round(self.total,2)} €"]
            liste_produits.append(produit_achete)
        else:
            pass




produit_1 = Produit("Bouteille", 0, 0.2, "p.")
produit_2 = Produit("Sucre de canne", 0, 0.07, "g")
produit_3 = Produit("Concentré d'orange", 0, 0.3, "cl")
produit_4 = Produit("Eau pétillante", 0, 0.15, "L")
produit_5 = Produit("Colorant orange", 0, 0.7,"cL")
produit_6 = Produit("Acide citrique", 0, 0.7, "cL")
produit_7 = Produit("Etiquette", 0, 0.3,"p.")
produit_8 = Produit("Benzoate de sodium", 0, 0.4,"g")

tous_les_produits = []

list_1 = Facture(produit_1.nom, produit_1.quantite, produit_1.prix, produit_1.unite)
list_2 = Facture(produit_2.nom, produit_2.quantite, produit_2.prix, produit_2.unite)
list_3 = Facture(produit_3.nom, produit_3.quantite, produit_3.prix, produit_3.unite)
list_4 = Facture(produit_4.nom, produit_4.quantite, produit_4.prix, produit_4.unite)
list_5 = Facture(produit_5.nom, produit_5.quantite, produit_5.prix, produit_5.unite)
list_6 = Facture(produit_6.nom, produit_6.quantite, produit_6.prix, produit_6.unite)
list_7 = Facture(produit_7.nom, produit_7.quantite, produit_7.prix, produit_7.unite)
list_8 = Facture(produit_8.nom, produit_8.quantite, produit_8.prix, produit_8.unite)



