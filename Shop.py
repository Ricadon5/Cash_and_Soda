import customtkinter
from tkinter import BOTH, RIGHT
import Depot
from Depot import tous_les_produits, produit_1, produit_2, produit_3, produit_4, produit_5, produit_6, produit_7, produit_8


# Definizione della finestra principale (Village)
shop = customtkinter.CTk()
shop.geometry("1000x800")
shop.title("Cash & Soda: La lutte pour la liberté")
shop.iconbitmap('./Images/can.ico')

# Inserzione degli stili di scrittura
style_1 = customtkinter.CTkFont("Aptos", 28, "bold")
style_2 = customtkinter.CTkFont("Apotos", 18)
style_3 = customtkinter.CTkFont("Apotos", 16, slant="italic")
style_4 = customtkinter.CTkFont("Apotos", 24, "bold")
style_5 = customtkinter.CTkFont("Apotos", 18, "bold")


# Inserzione dei frame
frame_1 = customtkinter.CTkFrame(shop, fg_color="#143d59", corner_radius=0, height=800, width=300)
frame_2 = customtkinter.CTkFrame(shop, fg_color="#f4b41a", height=800, width=1000)
frame_3 = customtkinter.CTkFrame(frame_2, fg_color="ivory", corner_radius=20, height=400, width=600,
                                 bg_color="#f4b41a", border_color="#143d59", border_width=10)
frame_4 = customtkinter.CTkFrame(frame_2, fg_color="#143d59", corner_radius=20, height=150, width=600,
                                 bg_color="#f4b41a", border_color="ivory", border_width=5)
frame_1.pack(ipadx=10, ipady=10, expand=True, fill=BOTH, side=RIGHT)
frame_2.pack(ipadx=10, ipady=10, expand=True, fill=BOTH)
frame_2.lower()
frame_3.place(relx=0.5, rely=0.6, anchor="center")
frame_4.place(relx=0.5, rely=0.2, anchor="center")



# Widget del fraime_1
titre_11 = customtkinter.CTkLabel(frame_1, text = "Panier:", font = style_1, text_color="ivory")
titre_11.place(relx = 0.1, rely = 0.65, anchor = "w")
textbox = customtkinter.CTkTextbox(frame_1, height=230, width=290, fg_color="#143d59", text_color="ivory", font=style_2)
#textbox.configure(state="disabled")
textbox.place(relx = 0.5, rely = 0.7, anchor = "n")
# Per inserire la lita dei prodotti a disposizio e il titolo "Prodotti a disposizione"
titre_12 = customtkinter.CTkLabel(frame_1, text = "Les produits à votre\ndisposition:", font = style_1, text_color="ivory", justify="left")
ingredientes = customtkinter.CTkLabel(frame_1, text = f"\n{produit_1.nom} : {produit_1.quantite} {produit_1.unite}\n"
                                                      f"\n{produit_2.nom} : {produit_2.quantite} {produit_2.unite}\n"
                                                      f"\n{produit_3.nom} : {produit_3.quantite} {produit_3.unite}\n"
                                                      f"\n{produit_4.nom} : {produit_4.quantite} {produit_4.unite}\n"
                                                      f"\n{produit_5.nom} : {produit_5.quantite} {produit_5.unite}\n"
                                                      f"\n{produit_6.nom} : {produit_6.quantite} {produit_6.unite}\n"
                                                      f"\n{produit_7.nom} : {produit_7.quantite} {produit_7.unite}\n"
                                                      f"\n{produit_8.nom} : {produit_8.quantite} {produit_8.unite}\n",
                                      font = style_2, text_color="ivory", justify="left")
titre_12.place(relx = 0.1, rely = 0.1, anchor = "w")
ingredientes.place(relx = 0.1, rely = 0.38, anchor = "w")




# Labels per inserire del testo nel frame_4
titre_41 = customtkinter.CTkLabel(frame_4, text = "Bienvenue Chez Dupont", font = style_1, text_color="ivory")
titre_42 = customtkinter.CTkLabel(frame_4, text = "Ici, tu peux acheter tous les produits dont tu as besoin.", font = style_2, text_color="ivory")
titre_41.place(relx = 0.05, rely = 0.3, anchor = "w")
titre_42.place(relx = 0.05, rely = 0.6, anchor = "w")


# Inserisco un input nel frame_3
def stampa_scontrino():
    user_input_1 = int(entry_1.get())  # Recupera il testo
    user_input_2 = int(entry_2.get())
    user_input_3 = int(entry_3.get())
    user_input_4 = int(entry_4.get())
    user_input_5 = int(entry_5.get())
    user_input_6 = int(entry_6.get())
    user_input_7 = int(entry_7.get())
    user_input_8 = int(entry_8.get())
    Depot.list_1.nouvelle_facture(tous_les_produits, user_input_1)
    Depot.list_2.nouvelle_facture(tous_les_produits, user_input_2)
    Depot.list_3.nouvelle_facture(tous_les_produits, user_input_3)
    Depot.list_4.nouvelle_facture(tous_les_produits, user_input_4)
    Depot.list_5.nouvelle_facture(tous_les_produits, user_input_5)
    Depot.list_6.nouvelle_facture(tous_les_produits, user_input_6)
    Depot.list_7.nouvelle_facture(tous_les_produits, user_input_7)
    Depot.list_8.nouvelle_facture(tous_les_produits, user_input_8)
    for produit in tous_les_produits:
        textbox.insert(0.0, f"{produit}\n")
    if not produit:
        pass
    else:
        acheter = customtkinter.CTkButton(frame_3, text="Acheter", text_color="#143d59", fg_color="#f4b41a",
                                          font=style_2)
        effacer = customtkinter.CTkButton(frame_3, text="Effacer tout", text_color="#143d59", fg_color="#f4b41a",
                                          font=style_2, command=effacet_tout)
        acheter.place(relx=0.5, rely=0.9, anchor="center")
        effacer.place(relx=0.2, rely=0.9, anchor="center")

def effacet_tout():
    tous_les_produits.clear()
    textbox.delete("0.0", "end")

entry_1 = customtkinter.CTkEntry(frame_3, placeholder_text="CTkEntry", height=20, width=70)
entry_2 = customtkinter.CTkEntry(frame_3, placeholder_text="CTkEntry", height=20, width=70)
entry_3 = customtkinter.CTkEntry(frame_3, placeholder_text="CTkEntry", height=20, width=70)
entry_4 = customtkinter.CTkEntry(frame_3, placeholder_text="CTkEntry", height=20, width=70)
entry_5 = customtkinter.CTkEntry(frame_3, placeholder_text="CTkEntry", height=20, width=70)
entry_6 = customtkinter.CTkEntry(frame_3, placeholder_text="CTkEntry", height=20, width=70)
entry_7 = customtkinter.CTkEntry(frame_3, placeholder_text="CTkEntry", height=20, width=70)
entry_8 = customtkinter.CTkEntry(frame_3, placeholder_text="CTkEntry", height=20, width=70)
entry_1.insert(0, "0")
entry_2.insert(0, "0")
entry_3.insert(0, "0")
entry_4.insert(0, "0")
entry_5.insert(0, "0")
entry_6.insert(0, "0")
entry_7.insert(0, "0")
entry_8.insert(0, "0")
entry_1.place(relx = 0.8, rely = 0.2, anchor ="center")
entry_2.place(relx = 0.8, rely = 0.28, anchor ="center")
entry_3.place(relx = 0.8, rely = 0.36, anchor ="center")
entry_4.place(relx = 0.8, rely = 0.44, anchor ="center")
entry_5.place(relx = 0.8, rely = 0.52, anchor ="center")
entry_6.place(relx = 0.8, rely = 0.60, anchor ="center")
entry_7.place(relx = 0.8, rely = 0.68, anchor ="center")
entry_8.place(relx = 0.8, rely = 0.76, anchor ="center")


valider = customtkinter.CTkButton(frame_3, text="Valider", text_color="#143d59", fg_color="#f4b41a", font=style_2,
                                        command=stampa_scontrino)
valider.place(relx = 0.8, rely = 0.9, anchor ="center")

solde = customtkinter.CTkLabel(frame_3, text = "Solde disponible : ", font = style_2, text_color="#143d59")
materiaux = customtkinter.CTkLabel(frame_3, text =f"Bouteille\n"
                                   f"Sucre de canne\n"
                                   f"Concentré d'orange\n"
                                   f"Eau pétillants\n"
                                   f"Colorant orange\n"
                                   f"Acide citrique\n"
                                   f"Etiquette\n"
                                   f"Benzoate de sodium\n",
                                   font = style_4, text_color="#143d59", justify="left")

prix_materiaux_1 = customtkinter.CTkLabel(frame_3, text =f"{produit_1.prix} € / {produit_1.unite}\n",
                                        font = style_3, text_color="#143d59", justify="left")
prix_materiaux_2 = customtkinter.CTkLabel(frame_3, text =f"{produit_2.prix} € / {produit_2.unite}\n",
                                        font = style_3, text_color="#143d59", justify="left")
prix_materiaux_3 = customtkinter.CTkLabel(frame_3, text =f"{produit_3.prix} € / {produit_3.unite}\n",
                                        font = style_3, text_color="#143d59", justify="left")
solde.place(relx = 0.07, rely = 0.1, anchor = "w")
prix_materiaux_4 = customtkinter.CTkLabel(frame_3, text =f"{produit_4.prix} € / {produit_4.unite}\n",
                                        font = style_3, text_color="#143d59", justify="left")
solde.place(relx = 0.07, rely = 0.1, anchor = "w")
prix_materiaux_5 = customtkinter.CTkLabel(frame_3, text =f"{produit_5.prix} € / {produit_5.unite}\n",
                                        font = style_3, text_color="#143d59", justify="left")
solde.place(relx = 0.07, rely = 0.1, anchor = "w")
prix_materiaux_6 = customtkinter.CTkLabel(frame_3, text =f"{produit_6.prix} € / {produit_6.unite}\n",
                                    font = style_3, text_color="#143d59", justify="left")
solde.place(relx = 0.07, rely = 0.1, anchor = "w")
prix_materiaux_7 = customtkinter.CTkLabel(frame_3, text =f"{produit_7.prix} € / {produit_7.unite}\n",
                                        font = style_3, text_color="#143d59", justify="left")
solde.place(relx = 0.07, rely = 0.1, anchor = "w")
prix_materiaux_8 = customtkinter.CTkLabel(frame_3, text =f"{produit_8.prix} € / {produit_8.unite}\n",
                                        font = style_3, text_color="#143d59", justify="left")
solde.place(relx = 0.07, rely = 0.1, anchor = "w")
materiaux.place(relx = 0.07, rely = 0.5, anchor ="w")
prix_materiaux_1.place(relx = 0.65, rely = 0.22, anchor ="c")
prix_materiaux_2.place(relx = 0.65, rely = 0.30, anchor ="c")
prix_materiaux_3.place(relx = 0.65, rely = 0.38, anchor ="c")
prix_materiaux_4.place(relx = 0.65, rely = 0.46, anchor ="c")
prix_materiaux_5.place(relx = 0.65, rely = 0.54, anchor ="c")
prix_materiaux_6.place(relx = 0.65, rely = 0.62, anchor ="c")
prix_materiaux_7.place(relx = 0.65, rely = 0.70, anchor ="c")
prix_materiaux_8.place(relx = 0.65, rely = 0.78, anchor ="c")


shop.mainloop()

