import customtkinter
from tkinter import BOTH, RIGHT
from PIL import Image
from Depot import produit_1, produit_2, produit_3, produit_4, produit_5, produit_6, produit_7, produit_8


# Variabile per tenere traccia della finestra toplevel
info_window = None


# Funzione per aprire la finestra toplevel
def ouvrir_info_window():
    global info_window
    if info_window is None or not info_window.winfo_exists():
        # Crea una nuova finsetra se non esite
        info_window = customtkinter.CTkToplevel(village)
        info_window.geometry("700x500")
        info_window.title("Informations pratiques")
        village.iconbitmap('./Images/can.ico')

        # Aggiunge i frame di base
        frame_1 = customtkinter.CTkFrame(info_window, fg_color="#f4b41a", height=400, width=600)
        frame_2 = customtkinter.CTkFrame(frame_1, fg_color="ivory", corner_radius=20, height=400, width=600,
                                         bg_color="#f4b41a", border_color="#143d59", border_width=10)
        frame_1.pack(ipadx=10, ipady=10, expand=True, fill=BOTH)
        frame_1.lower()
        frame_2.place(relx=0.5, rely=0.5, anchor="center")

        # Aggiunge le immagini della banca, del negozio e della fabbrica
        photo_2 = customtkinter.CTkImage(light_image=Image.open("./Images/bank_2.ico"),
                                         size=(50, 50))
        photo_3 = customtkinter.CTkImage(light_image=Image.open("./Images/store.ico"),
                                         size=(50, 50))
        photo_4 = customtkinter.CTkImage(light_image=Image.open("./Images/factory_1.ico"),
                                         size=(50, 50))
        bank = customtkinter.CTkLabel(frame_2, image=photo_2, text=" ", font=style_3)
        store = customtkinter.CTkLabel(frame_2, image=photo_3, text=" ", font=style_3)
        factory = customtkinter.CTkLabel(frame_2, image=photo_4, text=" ", font=style_3)
        bank.place(relx=0.1, rely=0.2, anchor="center")
        store.place(relx=0.1, rely=0.4, anchor="center")
        factory.place(relx=0.1, rely=0.6, anchor="center")

    else:
        # Porta in primo piano la finestra info_window se esiste
        info_window.focus()

# Definizione della finestra principale (Village)
village = customtkinter.CTk()
village.geometry("1000x800")
village.title("Cash & Soda: La lutte pour la liberté")
village.iconbitmap('./Images/can.ico')

# Funzione per aprire la finestra toplevel
def ouvrir_info_window():
    global info_window
    if info_window is None or not info_window.winfo_exists():
        # Crea una nuova finsetra se non esite
        info_window = customtkinter.CTkToplevel(village)
        info_window.geometry("700x500")
        info_window.title("Informations pratiques")
        village.iconbitmap('./Images/can.ico')

        # Aggiunge i frame di base
        frame_1 = customtkinter.CTkFrame(info_window, fg_color="#f4b41a", height=400, width=600)
        frame_2 = customtkinter.CTkFrame(frame_1, fg_color="ivory", corner_radius=20, height=400, width=600,
                                         bg_color="#f4b41a", border_color="#143d59", border_width=10)
        frame_1.pack(ipadx=10, ipady=10, expand=True, fill=BOTH)
        frame_1.lower()
        frame_2.place(relx=0.5, rely=0.5, anchor="center")

        # Aggiunge le immagini della banca, del negozio e della fabbrica
        photo_2 = customtkinter.CTkImage(light_image=Image.open("./Images/bank_2.ico"),
                                         size=(50, 50))
        photo_3 = customtkinter.CTkImage(light_image=Image.open("./Images/store.ico"),
                                         size=(50, 50))
        photo_4 = customtkinter.CTkImage(light_image=Image.open("./Images/factory_1.ico"),
                                         size=(50, 50))
        bank = customtkinter.CTkLabel(frame_2, image=photo_2, text=" ", font=style_3)
        store = customtkinter.CTkLabel(frame_2, image=photo_3, text=" ", font=style_3)
        factory = customtkinter.CTkLabel(frame_2, image=photo_4, text=" ", font=style_3)
        bank.place(relx=0.1, rely=0.2, anchor="center")
        store.place(relx=0.1, rely=0.4, anchor="center")
        factory.place(relx=0.1, rely=0.6, anchor="center")

    else:
        # Porta in primo piano la finestra info_window se esiste
        info_window.focus()


# Inserzione degli stili di scrittura
style_1 = customtkinter.CTkFont("Aptos", 28, "bold")
style_2 = customtkinter.CTkFont("Apotos", 18)
style_3 = customtkinter.CTkFont("Apotos", 18, slant="italic")
style_4 = customtkinter.CTkFont("Apotos", 24, "bold")
style_5 = customtkinter.CTkFont("Apotos", 18, "bold")


# Inserzione dei frame
frame_1 = customtkinter.CTkFrame(village, fg_color="#143d59", corner_radius=0, height=800, width=300)
frame_2 = customtkinter.CTkFrame(village, fg_color="#f4b41a", height=800, width=1000)
frame_3 = customtkinter.CTkFrame(frame_2, fg_color="ivory", corner_radius=20, height=400, width=600,
                                 bg_color="#f4b41a", border_color="#143d59", border_width=10)
frame_4 = customtkinter.CTkFrame(frame_2, fg_color="#143d59", corner_radius=20, height=150, width=600,
                                 bg_color="#f4b41a", border_color="ivory", border_width=5)
frame_1.pack(ipadx=10, ipady=10, expand=True, fill=BOTH, side=RIGHT)
frame_2.pack(ipadx=10, ipady=10, expand=True, fill=BOTH)
frame_2.lower()
frame_3.place(relx=0.5, rely=0.6, anchor="center")
frame_4.place(relx=0.5, rely=0.2, anchor="center")


# Labels per inserire del testo nel frame_4
titre_41 = customtkinter.CTkLabel(frame_4, text = "Bienvenue à Bruxville", font = style_1, text_color="ivory")
titre_42 = customtkinter.CTkLabel(frame_4, text = "Da qui poi raggiungere la banca, il negozio oppure la fabbrica", font = style_2, text_color="ivory")
titre_41.place(relx = 0.05, rely = 0.3, anchor = "w")
titre_42.place(relx = 0.05, rely = 0.6, anchor = "w")


# Aggiunge immagini al frame_3
photo_31 = customtkinter.CTkImage(light_image=Image.open("./Images/Arrow.png"),
                                         size=(25, 25))
# Labels per inserire del testo nel frame_3
information = customtkinter.CTkLabel(frame_3, text = "Se ti senti perso clicca qui", font = style_2, text_color="#143d59")
batiment = customtkinter.CTkLabel(frame_3, text = "Segli l'edificio dove vuoi andare", font = style_2, text_color="#143d59")
arrow = customtkinter.CTkLabel(frame_3, image=photo_31, text=" ", font=style_3)
arrow_2 = customtkinter.CTkLabel(frame_3, image=photo_31, text=" ", font=style_3)
information.place(relx = 0.15, rely = 0.2, anchor = "w")
batiment.place(relx = 0.15, rely = 0.4, anchor = "w")
arrow.place(relx=0.08, rely=0.2, anchor="center")
arrow_2.place(relx=0.08, rely=0.4, anchor="center")
# Aggiunge i bottoni del frame_3
info = customtkinter.CTkButton(frame_3, text="Info", text_color="#143d59", fg_color="#f4b41a", font=style_2,
                               command=ouvrir_info_window)
info.place(relx=0.8, rely=0.2, anchor="center")


# Qui sono contenuti tutti i Widgets del frame_1
# Labels per inserire del testo
compte_bancaire = customtkinter.CTkLabel(frame_1, text = "Denaro a disposizione", font = style_2, text_color="ivory")
orange_bull = customtkinter.CTkLabel(frame_1, text = "Orange Bull fabbricate", font = style_2, text_color="ivory")
titre_11 = customtkinter.CTkLabel(frame_1, text = "Produits", font = style_1, text_color="ivory")
ingredientes = customtkinter.CTkLabel(frame_1, text = f"\n{produit_1.nom} : {produit_1.quantite} {produit_1.unite}\n"
                                                      f"\n{produit_2.nom} : {produit_2.quantite} {produit_2.unite}\n"
                                                      f"\n{produit_3.nom} : {produit_3.quantite} {produit_3.unite}\n"
                                                      f"\n{produit_4.nom} : {produit_4.quantite} {produit_4.unite}\n"
                                                      f"\n{produit_5.nom} : {produit_5.quantite} {produit_5.unite}\n"
                                                      f"\n{produit_6.nom} : {produit_6.quantite} {produit_6.unite}\n"
                                                      f"\n{produit_7.nom} : {produit_7.quantite} {produit_7.unite}\n"
                                                      f"\n{produit_8.nom} : {produit_8.quantite} {produit_8.unite}\n",
                                      font = style_2, text_color="ivory", justify="left")
compte_bancaire.place(relx = 0.1, rely = 0.1, anchor = "w")
orange_bull.place(relx = 0.1, rely = 0.2, anchor = "w")
titre_11.place(relx = 0.1, rely = 0.35, anchor = "w")
ingredientes.place(relx = 0.1, rely = 0.6, anchor = "w")
# Progressbar
progressbar_1 = customtkinter.CTkProgressBar(frame_1, orientation="horizontal", fg_color="ivory", progress_color="#f4b41a")
progressbar_2 = customtkinter.CTkProgressBar(frame_1, orientation="horizontal", fg_color="ivory", progress_color="#f4b41a")
progressbar_1.place(relx = 0.1, rely = 0.15, anchor = "w")
progressbar_2.place(relx = 0.1, rely = 0.25, anchor = "w")


village.mainloop()

#Funzione per andare a pagina due
#def apri_pagina2():
    #debut.destroy()
    #app.mainloop()
