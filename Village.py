import customtkinter
from tkinter import BOTH, RIGHT
from PIL import Image

village = customtkinter.CTk()
village.geometry("1000x800")
village.title("Cash & Soda: La lutte pour la liberté")
village.iconbitmap('./Images/can.ico')


#Inserzione degli stili di scrittura
style_1 = customtkinter.CTkFont("Aptos", 28, "bold")
style_2 = customtkinter.CTkFont("Apotos", 18)
style_3 = customtkinter.CTkFont("Apotos", 18, slant="italic")
style_4 = customtkinter.CTkFont("Apotos", 24, "bold")
style_5 = customtkinter.CTkFont("Apotos", 18, "bold")


#Inserzione dei frame
frame_1 = customtkinter.CTkFrame(village, fg_color="#143d59", corner_radius=0, height=800, width=300)
frame_2 = customtkinter.CTkFrame(village, fg_color="#f4b41a", height=800, width=1000)
frame_3 = customtkinter.CTkFrame(frame_2, fg_color="ivory", corner_radius=20, height=400, width=600,
                                 bg_color="#f4b41a", border_color="#143d59", border_width=10)
frame_4 = customtkinter.CTkFrame(frame_2, fg_color="#143d59", corner_radius=20, height=200, width=600,
                                 bg_color="#f4b41a", border_color="ivory", border_width=5)
frame_1.pack(ipadx=10, ipady=10, expand=True, fill=BOTH, side=RIGHT)
frame_2.pack(ipadx=10, ipady=10, expand=True, fill=BOTH)
frame_2.lower()
frame_3.place(relx=0.5, rely=0.6, anchor="center")
frame_4.place(relx=0.5, rely=0.2, anchor="center")


#Inserzione del titolo
titre = customtkinter.CTkLabel(frame_4, text = "Bienvenue au village", font = style_1, text_color="ivory")
titre.place(relx = 0.05, rely = 0.2, anchor = "w")


#Per inserire le icone: banca, negozio e fabbrica
photo_2 = customtkinter.CTkImage(light_image=Image.open("./Images/bank_2.ico"),
                                size=(50, 50))
photo_3 = customtkinter.CTkImage(light_image=Image.open("./Images/store.ico"),
                                size=(50, 50))
photo_4 = customtkinter.CTkImage(light_image=Image.open("./Images/factory_1.ico"),
                                size=(50, 50))
bank = customtkinter.CTkLabel(frame_3, image=photo_2, text=" ", font=style_3)
store = customtkinter.CTkLabel(frame_3, image=photo_3, text=" ", font=style_3)
factory = customtkinter.CTkLabel(frame_3, image=photo_4, text=" ", font=style_3)
bank.place(relx=0.1, rely=0.2, anchor="center")
store.place(relx=0.1, rely=0.4, anchor="center")
factory.place(relx=0.1, rely=0.6, anchor="center")


village.mainloop()

#Funzione per andare a pagina due
#def apri_pagina2():
    #debut.destroy()
    #app.mainloop()


#button = customtkinter.CTkButton(frame_4, text="Esci", font=style_5, fg_color="firebrick",
                                 #command = lambda: app.quit())
#button.place(relx = 0.8, rely = 0.5, anchor="center")
#button_2 = customtkinter.CTkButton(frame_4, text="Conferma", font=style_5, fg_color="dodgerblue")
#button_2.place(relx = 0.2, rely = 0.5, anchor="center")