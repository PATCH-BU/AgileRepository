# import re
# from tkinter import *
# import customtkinter as  ctk
# from tkinter import messagebox
# import csv
#
# def change():
#     # a = random.choice(menu1)
#     Bet1_button.configure(text = 'hello',state='disabeld')
# # Création de la fenêtre principale
# window = ctk.CTk()
# window.title("GoBet")
# window.minsize(800, 600)
# window.maxsize(1366, 768)
#
# window.config(bg='#272524')
#
# # Création du cadre
# frame = ctk.CTkFrame(window,
#                      width=400,
#                      height=500,
#                     corner_radius=10,
#                     fg_color='#4f4d49',
#                     bg_color= '#272524',
#                     )
# frame.place(relx=0.5, rely=0.5, anchor=CENTER)
# # Le bouton
# Bet1_button = ctk.CTkButton(frame, text="---", width=300,fg_color='#007BFF', hover_color='#001328', corner_radius=8, command=change)
# # Positionnement
# Bet1_button.place(relx=0.5, rely=0.8, anchor=CENTER)
# # Lancer la boucle principale
# window.mainloop()
import csv
import random


#(********  savoire les font installer sur la machine  *********)
# from tkinter import *
# from tkinter import font
#
# root = Tk()
# available_fonts = list(font.families())  # Récupérer les noms des polices installées
# root.destroy()
#
# print(available_fonts)
# class ValidationError(EXCEPTION):
#     pass
# def validation():
#     messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")
# try:
#     for i in bet:
#         if i[0] == alism and i[2] == al9an_siri:
#             messagebox.showinfo("Succès", "Connexion réussie !")
#             window.destroy()
#             import game1
#     else:
#         raise ValidationError()
# except ValidationError:
#     validation()
#***************************************************************
# import customtkinter as ctk
# from PIL import Image
#
# # Configuration de CustomTkinter
# ctk.set_appearance_mode("Dark")  # Modes: "Light", "Dark", "System"
# ctk.set_default_color_theme("blue")
#
# # Fenêtre principale
# root = ctk.CTk()
# root.geometry("300x200")
# root.title("Bouton avec Image")
#
# # Charger une image avec PIL
# image = ctk.CTkImage(
#     light_image=Image.open("IMG/pic-marouane-2.png"),  # Image pour le mode clair
#     dark_image=Image.open("IMG/pic-marouane-2.png"),  # Image pour le mode foncé
#     size=(150, 150)  # Taille de l'image
# )
#
# # Bouton avec une image
# bouton = ctk.CTkButton(
#     root,
#     text="",  # Pas de texte
#     image=image,  # Image à afficher
#     width=150,
#     height=150
# )
# bouton.pack(pady=20)
#
# # Lancement de l'application
# root.mainloop()

#***************************************************************

# import customtkinter as ctk
# from PIL import Image
#
# # Configuration de CustomTkinter
# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("blue")
#
# # Fenêtre principale
# root = ctk.CTk()
# root.geometry("300x200")
# root.title("Bouton avec Image au Clic")
#
# # Charger l'image pour le bouton
# image = ctk.CTkImage(
#     light_image=Image.open("IMG/pic-marouane-2.png"),  # Remplacez par le chemin de votre image
#     size=(50, 50)  # Ajustez la taille
# )
#
# # Fonction pour afficher l'image sur le bouton
# def afficher_image():
#     bouton.configure(image=image, text="")  # Ajouter l'image et supprimer le texte
#
# # Bouton
# bouton = ctk.CTkButton(
#     root,
#     text="Cliquez ici",  # Texte initial
#     command=afficher_image,  # Commande appelée au clic
#     width=50,
#     height=50,
# )
# bouton.pack(pady=20)
#
# # Lancement de l'application
# root.mainloop()

#***************************************************************
# c=12
# def fichier_button():
#     with open('connection.csv','w',newline='',encoding='utf-8')as f:
#         BUT=csv.writer(f,delimiter=';')
#         BUT.writerow([2,5])
#         BUT.writerow([3,6])
#         BUT.writerow([c,9])
#     with open('connection.csv','r',newline='',encoding='utf-8')as f:
#         l_BUT = list(csv.reader(f, delimiter=';'))
#         cc=random.choice(l_BUT)
#         print(cc)
# fichier_button()
#********************************************************************
# import customtkinter as ctk
#
# # Configuration de CustomTkinter
# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("blue")
#
# # Fenêtre principale
# root = ctk.CTk()
# root.geometry("300x200")
# root.title("Activer/Désactiver une entrée")
#
# # Création d'une entrée
# entree = ctk.CTkEntry(root, placeholder_text="Modifiez-moi !")
# entree.pack(pady=20)
#
# # Fonction pour désactiver l'entrée
# def desactiver_entree():
#     entree.configure(state="disabled")  # Rendre l'entrée non éditable
#
# # Fonction pour activer l'entrée
# def activer_entree():
#     entree.configure(state="normal")  # Rendre l'entrée éditable
#
# # Boutons pour contrôler l'état de l'entrée
# bouton_desactiver = ctk.CTkButton(root, text="Désactiver", command=desactiver_entree)
# bouton_desactiver.pack(pady=10)
#
# bouton_activer = ctk.CTkButton(root, text="Activer", command=activer_entree)
# bouton_activer.pack(pady=10)
#
# # Lancement de l'application
# root.mainloop()
#
# dic = {
#     'but1': but1, 'but2': but2, 'but3': but3, 'but4': but4, 'but5': but5,
#     'but6': but6, 'but7': but7, 'but8': but8, 'but9': but9, 'but10': but10,
#     'but11': but11, 'but12': but12, 'but13': but13, 'but14': but14, 'but15': but15,
#     'but16': but16, 'but17': but17, 'but18': but18, 'but19': but19, 'but20': but20,
#     'but21': but21, 'but22': but22, 'but23': but23, 'but24': but24, 'but25': but25
# }
#
# for y in range(1, 26):
#     BUT.writerow([f'but{y}'])
#
# eniter.configure(image=image1, text='')
#***********************************************
# import customtkinter as ctk
# from tkinter import *
#
# # def bouton_clique(nom_bouton):
# #     print(f"Vous avez cliqué sur le bouton : {nom_bouton}")
#
# def bouton_clique_direct(bouton):
#     print(f"Vous avez cliqué sur l'instance bouton : {bouton}")
#     bouton.configure(text="C'est moi !")
#
# window = ctk.CTk()
# window.title("Détection du bouton cliqué")
# window.geometry("500x500")
#
# frame = ctk.CTkFrame(window)
# frame.pack(pady=20)
#
# buttons = []
# for i in range(3):  # 3 lignes
#     for j in range(3):  # 3 colonnes
#         button_name = f"but_{i}_{j}"
#         button = ctk.CTkButton(
#             frame,
#             text=button_name,
#             command=lambda b=button_name: bouton_clique_direct(b),  # Méthode 1 : avec un identifiant
#             width=85,
#             height=85,
#             corner_radius=10,
#             border_width=1,
#             border_color='#2e2e2e',
#             bg_color='#09111e',
#             fg_color='#0c1b2c',
#             hover_color='#043d56',
#         )
#         button.grid(row=i, column=j, padx=10, pady=10)
#         buttons.append(button)
#
# window.mainloop()
#************************** IMPORTER LES FICHIERS **********************************
# import customtkinter as ctk
# from tkinter import filedialog
# from PIL import Image
#
# # Créer une fenêtre principale
# window = ctk.CTk()
# window.title("Sélection d'une image")
#
# # Fonction pour demander une image
# def choisir_image():
#     # Ouvrir une boîte de dialogue pour choisir un fichier image
#     chemin_image = filedialog.askopenfilename(
#         title="Choisir une image",
#         filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
#     )
#     if chemin_image:  # Vérifier si un fichier a été sélectionné
#         img = ctk.CTkImage(light_image=Image.open(chemin_image), size=(50, 50))
#         button.configure(image=img)  # Ajouter l'image au bouton
#         button.image = img  # Préserver la référence pour éviter le ramasse-miettes
#
# # Créer un bouton initial sans image
# button = ctk.CTkButton(window, text="Cliquez pour ajouter une image", command=choisir_image, width=200, height=100)
# button.pack(pady=20)
#
# # Lancer la fenêtre
# window.mainloop()
#***************************************************************************************
# def import_info():
#     wlu=''
#     with open('connection.csv', 'r', newline='', encoding='utf-8') as fc:
#         login =list (csv.reader(fc, delimiter=';'))
#         for i in login:
#             for y in i:
#                 wlu+=y
#     return  wlu
# print(import_info())
# #*******************************************************************
# def fichier_button(but):
#     # dic = {'IMG1':image1 , 'IMG2': image2 }
#     c = nb_coeur.get()
#     c = int(c)
#     if c==5:
#         img_rand = random.choice(list(retoure().values()))
#         a = 0
#         if img_rand==image2:
#             a=0
#             but.configure(image=img_rand, text='', state='disabled')
#             messagebox.showinfo('Go|Bet','tousit awlaydi')
#             for i in [but1, but2, but3, but4, but5, but6, but7,
#                       but8, but9, but10, but11, but12, but13, but14, but15, but16,
#                       but17, but18, but19, but20, but21, but22, but23, but24, but25]:
#                  i.configure(image=None,text='',state='disabled',border_color="#2e2e2e")
#                  bet.configure(state="normal")
#                  nb_coeur.configure(state="normal")
#                  a+=1
#         if a==0 :
#              but.configure(image=img_rand, text='',state='disabled',border_color="#14a714")
#**************************************  CHOIS D'IMAGE ET LA RENDRE CERCLE ********************************************************
# import customtkinter as ctk
# from tkinter import filedialog
# from PIL import Image, ImageDraw
#
#
# def round_corners(image):
#     """Retourne une image avec des coins arrondis."""
#     # Créer une image de même taille que l'image d'origine
#     mask = Image.new('L', image.size, 0)
#     draw = ImageDraw.Draw(mask)
#     # Dessiner des coins arrondis
#     draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
#
#     # Appliquer le masque
#     rounded_image = Image.new('RGBA', image.size)
#     rounded_image.paste(image, (0, 0), mask)
#
#     return rounded_image
#
#
# def choisir_image():
#     chemin_image = filedialog.askopenfilename(
#         title="Choisir une image",
#         filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
#     )
#
#     if chemin_image:
#         try:
#             # Charger l'image
#             image = Image.open(chemin_image).convert("RGBA")
#             # Arrondir les coins de l'image
#             rounded_image = round_corners(image)  # Ajustez le rayon ici
#             img = ctk.CTkImage(light_image=rounded_image, size=(160, 160))
#             pic.configure(image=img, text='')  # Ajouter l'image au bouton sans texte
#             pic.image = img  # Préserver la référence pour éviter le ramasse-miettes
#             pic.update()  # Mettre à jour le widget pour afficher l'image
#         except Exception as e:
#             print(f"Erreur lors de l'ouverture de l'image : {e}")
#     else:
#         print("Aucun fichier sélectionné.")
#
#
# # Créer la fenêtre principale
# window = ctk.CTk()
# window.title("Image avec Coins Arrondis")
#
# # Créer le bouton avec dimensions fixes
# pic = ctk.CTkButton(window, text='', command=choisir_image, width=160, height=160, corner_radius=80)
# pic.pack(pady=20)
#
# # Lancer la boucle principale
# window.mainloop()
#**********************************************************************************************
# import customtkinter as ctk
#
# # Classe pour le jeu 1
# class Game1:
#     def __init__(self, master):
#         self.frame = ctk.CTkFrame(master)
#         self.frame.pack(fill='both', expand=True)
#
#         # Ajouter un label pour indiquer que c'est le jeu 1
#         self.label = ctk.CTkLabel(self.frame, text="Bienvenue dans le Jeu 1!", font=("Arial", 24))
#         self.label.pack(pady=20)
#
#         # Bouton pour revenir à l'écran principal
#         self.back_button = ctk.CTkButton(self.frame, text="Retour", command=self.back_to_main)
#         self.back_button.pack(pady=10)
#
#     def back_to_main(self):
#         self.frame.pack_forget()  # Cache la frame du jeu
#         main_app.frame.pack(fill='both', expand=True)  # Montre la frame principale
#
# # Classe pour l'application principale
# class MainApp:
#     def __init__(self, master):
#         self.master = master
#         self.frame = ctk.CTkFrame(master)
#         self.frame.pack(fill='both', expand=True)
#
#         # Titre de l'application
#         self.title_label = ctk.CTkLabel(self.frame, text="Application de Jeu", font=("Arial", 24))
#         self.title_label.pack(pady=20)
#
#         # Bouton pour lancer le jeu 1
#         self.start_button = ctk.CTkButton(self.frame, text="Lancer Jeu 1", command=self.launch_game1)
#         self.start_button.pack(pady=10)
#
#     def launch_game1(self):
#         self.frame.pack_forget()  # Cache la frame actuelle
#         game1 = Game1(self.master)  # Crée une nouvelle instance de Game1
#
# # Démarrage de l'application
# if __name__ == "__main__":
#     root = ctk.CTk()
#     root.title("Mon Application de Jeu")  # Titre de la fenêtre
#     root.geometry("400x300")  # Dimensions de la fenêtre
#     main_app = MainApp(root)  # Crée l'instance de l'application principale
#     root.mainloop()  # Démarre la boucle principale de l'application
#********************************************************************************************************
# import customtkinter as ctk
#
# # Créer une fenêtre principale
# window = ctk.CTk()
# window.title("Sélection de l'âge")
#
# # Fonction pour afficher l'âge sélectionné
# def afficher_age():
#     age_selectionne = age_scale.get()
#     print(f"Âge sélectionné: {age_selectionne}")
#
# # Créer un Scale pour sélectionner l'âge
# age_scale = ctk.CTkSlider(window, from_=18, to=100, command=lambda value: age_label.configure(text=f"Âge: {int(float(value))}"))
# age_scale.set(18)  # Valeur par défaut
#
# # Label pour afficher l'âge sélectionné
# age_label = ctk.CTkLabel(window, text="Âge: 18")
#
# # Créer un bouton pour afficher l'âge sélectionné
# button = ctk.CTkButton(window, text="Afficher l'âge", command=afficher_age)
#
# # Positionner les éléments
# age_scale.pack(pady=20)
# age_label.pack(pady=10)
# button.pack(pady=10)
#
# # Lancer la fenêtre
# window.mainloop()
#***************************************************************************************************************************
# utilisateur=''
# with open('connection.csv','r',newline='',encoding='utf-8') as  fc:
#                 con= list(csv.reader(fc, delimiter=';'))
#                 for i in con:
#                     for y in i:
#                         utilisateur+=y
#                 print(utilisateur)
#***************************************************************************************************************************
# for i in range(4):
#         for j in range(4):
#             random_couleur=random.randint(0,len(liste_couleur)-1)
#             color=liste_couleur[random_couleur]
#             label_button=Button(button_frame,text="###",background='silver',fg="white",width=10,height=3,activebackground=color)
#             label_button.grid(row=i, column=j, padx=10, pady=10)
#             buttons.append(label_button)
#             buttons[-1]['command'] = partial(active, label_button, color)
#             liste_couleur.pop(random_couleur)
#***************************************************************************************************************************
import tkinter as tk
from tkinter import Button
from functools import partial
import random


# Fonction active à appeler lors du clic sur le bouton
def active(button, image):
    # Change l'image du bouton lorsque cliqué
    button['image'] = image
    print(f"Button clicked with image: {image}")


# Créer la fenêtre principale
root = tk.Tk()
root.title("Boutons avec Images")

# Cadre pour les boutons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Charger les images (assurez-vous que les images sont dans le bon format)
image1 = tk.PhotoImage(file='IMG/Boom02.png')  # Remplacez par le chemin de votre image
image2 = tk.PhotoImage(file='IMG/Diamonde01.png')  # Remplacez par le chemin de votre image
  # Remplacez par le chemin de votre image
  # Remplacez par le chemin de votre image

# Liste d'images
liste_images = [image1, image2,]

# Liste pour stocker les boutons
buttons = []

# Créer une grille de boutons avec des images
for i in range(4):
    for j in range(4):
        # Sélectionner une image aléatoire
        random_image = random.choice(liste_images)

        # Créer le bouton avec l'image
        label_button = Button(button_frame, image=random_image, width=100, height=100)
        label_button.grid(row=i, column=j, padx=10, pady=10)

        # Définir la commande du bouton après sa création
        label_button['command'] = partial(active, label_button, random_image)

        # Ajouter le bouton à la liste
        buttons.append(label_button)
r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# Lancer la boucle principale
root.mainloop()
#************************************************************************************
# def seter_les_donner():
#     #exception pour le jour
#     try:
#         if not jour.get().strip().isdigit():
#             jour.configure(border_color='red',border_width=2)
#             messagebox.showinfo('Erreur', 'Veuillez entrer un jour valide entre 1 et 31')
#             raise ValueError("Année invalide.")
#         nhar = jour.get().strip()
#         if nhar > 31 or nhar <1:
#             messagebox.showinfo('Erreur','Veuillez entrer un jour valide entre 1 et 31')
#         raise ValueError("")
#     except Exception as e:
#         print(f'Exception pr le jour est : {e}')
#
#     # exception pour le mois
#     try:
#         if not mois.get().strip().isdigit():
#             mois.configure(border_color='red', border_width=2)
#             raise ValueError("Année invalide.")
#         chher = mois.get().strip()
#         if chher > 12 or chher <1:
#             messagebox.showinfo('Erreur','Veuillez entrer un mois valide entre 1 et 12')
#     except Exception as e:
#         print(f'Exception pr le mois est : {e}')
#     # exception pour l'anner
#     try:
#         anner_actuelle = datetime.now().year
#         if not anner.get().strip().isdigit():
#             anner.configure(border_color='red',border_width=2)
#             raise ValueError("Année invalide.")
#         eam = int(anner.get().strip())
#         if anner_actuelle - eam < 18:
#             messagebox.showinfo('Erreur', "L'utilisateur doit avoir au moins 18 ans.")
#             raise ValueError("")
#     except Exception as e:
#         print(f'Exception pr anner est : {e}')
#     # exception globl
#     try:
#         user = pseudo.get()
#         NOM_COMPLET = fullname.get()
#         KOUD_KDIM = r
#         koud = new_Password.get()
#         conf_koud = conf_password.get()
#         tabrat = mail.get()
#         tele = phone.get()
#         ladrisa = adresse.get()
#         mdina = ville.get()
#         postal = code_postal.get()
#         if koud != conf_koud:
#             messagebox.showinfo('Erreur', 'Les mots de passe ne correspondent pas !')
#         elif not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", tabrat):
#             mail.configure(border_color='red', border_width=2)
#         else:
#             with open('Gobet_data.csv', 'r', newline='', encoding='utf-8') as f:
#                 red = list(csv.reader(f, delimiter=';'))
#                 for i in red:
#                     if i[0] == user:
#                         red.remove(i)
#                         break
#             with open('Gobet_data.csv', 'w', newline='', encoding='utf-8') as fa:
#                 ecr = csv.writer(fa, delimiter=';')
#                 ecr.writerow(['pseudo', 'email', 'old_password', 'new_password', 'real_name', 'jour', 'mois', 'anner',
#                               'telephone', 'adresse', 'ville', 'code_postal', 'chemin_image'])
#                 ecr.writerows(red)
#                 ecr.writerow(
#                     [user, tabrat, KOUD_KDIM, koud, NOM_COMPLET, nhar, chher, eam, tele, ladrisa, mdina, postal,
#                      chemin_image])
#     except Exception as e:
#         print(f'Exception est : {e}')
#*********************************************************
