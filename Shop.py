import customtkinter
from tkinter import BOTH, RIGHT
#from Depot import produit_1, produit_2, produit_3, produit_4, produit_5, produit_6, produit_7, produit_8



# Definizione della finestra principale (Village)
shop = customtkinter.CTk()
shop.geometry("1000x800")
shop.title("Cash & Soda: La lutte pour la liberté")
shop.iconbitmap('./Images/can.ico')

# Inserzione degli stili di scrittura
style_1 = customtkinter.CTkFont("Aptos", 28, "bold")
style_2 = customtkinter.CTkFont("Apotos", 18)
style_3 = customtkinter.CTkFont("Apotos", 18, slant="italic")
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


titre_11 = customtkinter.CTkLabel(frame_1, text = "Produits", font = style_1, text_color="ivory")

titre_11.place(relx = 0.1, rely = 0.35, anchor = "w")
#ingredientes.place(relx = 0.1, rely = 0.6, anchor = "w")


# Labels per inserire del testo nel frame_4
titre_41 = customtkinter.CTkLabel(frame_4, text = "Bienvenue à Chez Dupont", font = style_1, text_color="ivory")
titre_42 = customtkinter.CTkLabel(frame_4, text = "Da qui poi acquistare tutti i prodotti di cui hai bisogno", font = style_2, text_color="ivory")
titre_41.place(relx = 0.05, rely = 0.3, anchor = "w")
titre_42.place(relx = 0.05, rely = 0.6, anchor = "w")

# Inserisco un input nel frame_3
def stampa():
    global user_input
    user_input = entry.get()
    print(user_input)
entry = customtkinter.CTkEntry(frame_3, placeholder_text="CTkEntry")
entry.place(relx = 0.5, rely = 0.5, anchor = "center")
compra = customtkinter.CTkButton(frame_3, text="Compra", text_color="#143d59", fg_color="#f4b41a", font=style_2,
                               command=stampa)
compra.place(relx = 0.5, rely = 0.8, anchor = "center")

shop.mainloop()

