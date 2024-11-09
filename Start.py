from tkinter import BOTH, RIGHT
import customtkinter
from PIL import Image

start = customtkinter.CTk()
start.geometry("1000x800")
start.title("Cash & Soda: La lutte pour la liberté")
start.iconbitmap("./Images/can.ico")


#Stili di scrittura
style_1 = customtkinter.CTkFont("Aptos", 28, "bold")
style_2 = customtkinter.CTkFont("Apotos", 18)
style_3 = customtkinter.CTkFont("Apotos", 18, slant="italic")
style_4 = customtkinter.CTkFont("Apotos", 24, "bold")
style_5 = customtkinter.CTkFont("Apotos", 18, "bold")


#Inserzione dei frame
frame_1 = customtkinter.CTkFrame(start, fg_color="#143d59", corner_radius=0, height=800, width=300)
frame_2 = customtkinter.CTkFrame(start, fg_color="#f4b41a", height=800, width=1000)
frame_1.pack(ipadx=10, ipady=10, expand=True, fill=BOTH, side=RIGHT)
frame_2.pack(ipadx=10, ipady=10, expand=True, fill=BOTH)
frame_2.lower()


#Inserzione delle label: titolo e titolo_2
titre = customtkinter.CTkLabel(frame_1, text = "Cash & Soda:\n La lutte pour la liberté", font = style_1, text_color="ivory")
titre_2 = customtkinter.CTkLabel(frame_1, text = "Inserisci il tuo nome", font = style_5, text_color="ivory")
titre.place(relx = 0.5, rely = 0.1, anchor = "center")
titre_2.place(relx = 0.5, rely = 0.3, anchor = "center")


#Qui aggiungiamo due bottoni: uscita e continuare
sortir = customtkinter.CTkButton(frame_1, text="Sortir", font=style_5, fg_color="firebrick",
                                 command = lambda: start.quit())
continuer = customtkinter.CTkButton(frame_1, text="Start", font=style_5, fg_color="dodgerblue")
sortir.place(relx = 0.5, rely = 0.8, anchor="center")
continuer.place(relx = 0.5, rely = 0.9, anchor="center")


#In qusta sezione aggiungiamo l'immagine principale del gioco nel frame_2
photo = customtkinter.CTkImage(light_image=Image.open("./Images/poster.jpg"), size=(800, 800))
poster = customtkinter.CTkLabel(frame_2, text=" ", font=style_1, text_color="#f4b41a", image=photo,)
poster.place(relx=0.5, rely=0.5, anchor="center")


#In questa sezione l'utilizzatore potrà inserire il proprio nome
prenom_utilisateur = customtkinter.CTkTextbox(frame_1, width=200, height=50)
prenom_utilisateur.insert("0.0", "Mario")
prenom_utilisateur.place(relx=0.5, rely=0.4, anchor="center")


#Per avviare la finestra
start.mainloop()