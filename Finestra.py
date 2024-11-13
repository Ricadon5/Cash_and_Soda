from tkinter import BOTH, RIGHT
import customtkinter as ctk
from PIL import Image

class Application(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.geometry("1000x800")
        self.title("Cash & Soda: La lutte pour la liberté")
        
        # Styles de police
        self.style_2 = ctk.CTkFont("Apotos", 18)
        self.style_1 = ctk.CTkFont("Aptos", 40, "bold")
        self.style_4 = ctk.CTkFont("Apotos", 24, "bold")
        self.style_6 = ctk.CTkFont("Apotos", 22)
        
        # Cadres
        self.fr_info = ctk.CTkFrame(self, fg_color="#143d59", corner_radius=0, height=800, width=300)
        self.fr_game_play = ctk.CTkFrame(self, fg_color="#f4b41a", corner_radius=0, height=800, width=1000)
        self.fr_info.pack(ipadx=10, ipady=10, expand=True, fill=BOTH, side=RIGHT)
        self.fr_game_play.pack(ipadx=10, ipady=10, expand=True, fill=BOTH)
        self.fr_game_play.lower()
        
        # Titre et description
        titre = ctk.CTkLabel(self.fr_info, text="Cash & Soda :\n La lutte pour la liberté", font=self.style_1, text_color="ivory")
        titre.place(relx=0.5, rely=0.1, anchor="center")

        histoire_1 = ctk.CTkLabel(self.fr_info, text="Plongez dans l'histoire de notre jeu :", font=self.style_6, text_color="ivory")
        histoire_1.place(relx=0.5, rely=0.25, anchor="center")

        # Dictionnaire des personnages
        self.personnages_info = {
            "Carine": {
                "description": "Carine est une experte en mécanique et technologie avancée.",
                "image_path": "C:\\Users\\carin\\OneDrive-EPHEC asbl\\Images\\Carine.jpg"
            },
            "Wilson": {
                "description": "Wilson est rapide et agile, spécialiste en furtivité.",
                "image_path": ""  # Ajoutez le chemin si nécessaire
            },
            "Théo": {
                "description": "Théo possède une force exceptionnelle et une endurance incroyable.",
                "image_path": ""
            },
            "Ayoub": {
                "description": "Ayoub est un stratège ingénieux, habile en résolution de problèmes.",
                "image_path": ""
            }
        }

        # Fonction pour afficher la description et l'image du personnage
        def afficher_description(selection):
            personnage = self.personnages_info.get(selection)
            if personnage:
                # Mise à jour de la description
                self.label_description.configure(text=personnage["description"])
                
                # Chargement et mise à jour de l'image si le chemin est défini
                if personnage["image_path"]:
                    image = ctk.CTkImage(light_image=Image.open(personnage["image_path"]), size=(300, 300))
                    self.label_image.configure(image=image)
                    self.label_image.image = image  # Garde une référence pour éviter le ramasse-miettes

        # Menu déroulant pour sélectionner un personnage
        self.dropdown_menu = ctk.CTkOptionMenu(
            self.fr_info, values=list(self.personnages_info.keys()),
            command=afficher_description,
            font=self.style_2
        )
        self.dropdown_menu.place(relx=0.5, rely=0.3, anchor="center")

        # Labels pour afficher la description et l'image dans self.fr_game_play
        self.label_description = ctk.CTkLabel(self.fr_game_play, text="", font=self.style_2, text_color="black", wraplength=500)
        self.label_description.place(relx=0.5, rely=0.7, anchor="center")

        self.label_image = ctk.CTkLabel(self.fr_game_play, text="")
        self.label_image.place(relx=0.5, rely=0.3, anchor="center")

        # Boutons
        Avancer = ctk.CTkButton(self.fr_info, text="Avancer", font=self.style_2, text_color="ivory")
        Avancer.place(relx=0.85, rely=1, anchor="center")

        Annuler = ctk.CTkButton(self.fr_info, text="Annuler", font=self.style_2, text_color="ivory")
        Annuler.place(relx=0.5, rely=1, anchor="center")

        Retour = ctk.CTkButton(self.fr_info, text="Retour", font=self.style_2, text_color="ivory")
        Retour.place(relx=0.15, rely=1, anchor="center")

        # Image principale dans self.fr_game_play
        photo = ctk.CTkImage(light_image=Image.open("C:\\Users\\carin\\OneDrive - EPHEC asbl\\Images\\poster.jpg"), size=(1016, 1200))
        poster = ctk.CTkLabel(self.fr_game_play, text=" ", font=self.style_1, text_color="#f4b41a", image=photo)
        poster.place(relx=0.5, rely=0.5, anchor="center")

        # Zone de texte pour l'histoire
        histoire = ctk.CTkTextbox(self.fr_info, font=self.style_6, text_color="ivory", width=520, height=460, wrap="word", fg_color="#143d59")
        histoire.place(relx=0.5, rely=0.6, anchor="center")
        histoire.insert("0.0", (
            "Le jeu se déroule dans un monde dystopique où les banquiers ont déclaré la guerre à l’industrie des sodas.\n\n"
            "Pour lutter contre l’obésité qui accable de plus en plus les citoyens de Bruxville, ils ont décidé de couper tout "
            "financement aux usines de soda.\n\n"
            "Tu es le dernier entrepreneur déterminé à apporter de la joie et quelques kilos aux enfants de ta chère ville.\n\n"
            "Pour y parvenir, tu devras affronter le redoutable banquier ainsi que des pickpockets sans scrupules, tout en "
            "produisant 10 bouteilles d'Orange Bull et en devenant une véritable légende."
        ))
        histoire.configure(state="disabled")  # Désactive l'édition du texte

# Lancement de l'application
app = Application()
app.mainloop()