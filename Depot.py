class Produit:
    def __init__(self, nom, quantite=0, prix=0, unite="unité"):
        self.nom = nom
        self.quantite = quantite
        self.prix = prix
        self.unite = unite

     # Metodo per aggiornare la quantità a disposizione dopo l'acquisto
    def actualiser_la_quantite(self, a):
        self.quantite += a


class Facture(Produit):
    def __init__(self, nom, quantite, prix, unite, total = 0, n_facture=0, tva=0.15):
        super().__init__(nom, quantite, prix, unite)
        self.total = total
        self.n_facture = n_facture
        self.tva = tva

    # Metodo calcolo prezzo senza HTVA
    def nouvelle_facture(self):
        self.total = (self. quantite * self.prix * self.tva) + self. quantite * self.prix
        self.n_facture += 1
        print(self.total, self.n_facture)

produit_1 = Produit("Bouteille", 0, 5, "unité")
produit_2 = Produit("Sucre de canne", 0, 0.07, "g")
produit_3 = Produit("Concentré du jus d'orange", 0, 0.3, "cl")
produit_4 = Produit("Eau pétillante", 0, 0.15, "L")
produit_5 = Produit("Colorant orange", 0, 0.7,"cL")
produit_6 = Produit("Acide citrique", 0, 0.7, "cL")
produit_7 = Produit("Etiquette", 0, 0.3,"unité")
produit_8 = Produit("Benzoate de sodium", 0, 0.4,"g")







