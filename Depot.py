class Ingredient:
    def __init__(self, nom, quantite=0, prix=0, unite="unité"):
        self.nom = nom
        self.quantite = quantite
        self.prix = prix
        self.unite = unite

     # Metodo per aggiornare la quantità a disposizione dopo l'acquisto
    def actualiser_la_quantite(self, a):
        self.quantite += a


produit_1 = Ingredient("Bouteille", 0, 5, "unité")
produit_2 = Ingredient("Sucre de canne", 0, 0.07, "g")
produit_3 = Ingredient("Concentré du jus d'orange", 0, 0.3, "cl")
produit_4 = Ingredient("Eau pétillante", 0, 0.15, "L")
produit_5 = Ingredient("Colorant orange", 0, 0.7,"cL")
produit_6 = Ingredient("Acide citrique", 0, 0.7, "cL")
produit_7 = Ingredient("Etiquette", 0, 0.3,"unité")
produit_8 = Ingredient("Benzoate de sodium", 0, 0.4,"g")

produit_3.actualiser_la_quantite(100)
print(produit_1.nom)



