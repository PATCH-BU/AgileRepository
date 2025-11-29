import re
import customtkinter as ctk
from tkinter import *
from PIL import Image,ImageDraw
from tkinter import filedialog,messagebox
from datetime import datetime
import csv


window=ctk.CTk()
window.title('GoBet | PROFILE')
window.minsize(1160, 720)
window.maxsize(1920, 1080)
window.config(background='#09111e')
#************* frames ***********
frame1=ctk.CTkFrame(
    window,
    width=1105,
    height=599,
    bg_color='#09111e',
    fg_color='#0c1b2c',
    corner_radius=25,
    border_width=0,

)
frame2=ctk.CTkFrame(
    frame1,
    width=720,
    height=590,
    bg_color='#0c1b2c',
    fg_color='#09111e',
    border_color='#0c1b2c',
    corner_radius=15,
    border_width=2

)
chemin_image = ''
#******************* DIC *****************
pays={
    'Maroc':'+212','France':'+33','Egypt':'+20','Espagne':'+34','Algérie':'+213','Potugal':'+351',
}
#*********************** FONCTIONS ************************
def geter_donner():
    wlu=''
    try:
        with open('connection.csv','r',newline='',encoding='utf-8') as f:
            reader = list(csv.reader(f, delimiter=';'))
            for i in reader:
                for y in i:
                    wlu+=y
        with open('Gobet_data.csv','r',newline='',encoding='utf-8') as f:
            lect=list(csv.reader(f,delimiter=';'))
            for i in lect:
                if i[0] == wlu:
                    alism=i[0]
                    albarid=i[1]
                    ra9m_siri=i[2]
                    return alism,albarid,ra9m_siri
        messagebox.showerror("Erreur", "Aucun utilisateur trouvé!! peut etre fichier vide ou fichier n'existe pas")
        return None
    except Exception as e:
        print(f'exception est : {e}')
        messagebox.showerror("Erreur", "Une erreur s'est produite lors de la lecture des fichiers.")
        return None
    # return None
#********* Déstructuration des valeurs ************
p, b, r=geter_donner()

def seter_les_donner():
    #************************* exception pour le jour *************************
    try:
        nhar = jour.get().strip()
        if nhar=='' :
            jour.configure(border_color='#14a714', border_width=2)
        else:
            try:
                n=int(nhar)
                if n < 1 or n > 31  :
                    jour.configure(border_color='red', border_width=2)
                    messagebox.showinfo('Erreur','Veuillez entrer un jour valide entre 1 et 31')
                    return
                jour.configure(border_color='#14a714', border_width=2)
            except ValueError:
                jour.configure(border_color='red', border_width=2)
                messagebox.showinfo('Erreur', 'Veuillez entrer un jour valide (uniquement des chiffres).')
    #************************* exception pour le mois *************************
        chher = mois.get().strip()
        if chher=='' :
            mois.configure(border_color='#14a714', border_width=2)
        else:
            try:
                m = int(chher)
                if m > 31 or m < 1:
                    mois.configure(border_color='red', border_width=2)
                    messagebox.showinfo('Erreur', 'Veuillez entrer un jour valide entre 1 et 12')
                    return
                mois.configure(border_color='#14a714', border_width=2)
            except ValueError:
                mois.configure(border_color='red', border_width=2)
                messagebox.showinfo('Erreur', 'Veuillez entrer un mois valide (uniquement des chiffres).')
    #************************* exception pour l'anner *************************
        eam = anner.get().strip()
        if eam=='':
            anner.configure(border_color='#14a714', border_width=2)
        else:
            try:
                a = int(eam)
                anner_actuelle = datetime.now().year
                age = anner_actuelle - a
                if   age <18 or age > 100:
                    anner.configure(border_color='red', border_width=2)
                    messagebox.showinfo('Erreur', "L'utilisateur doit avoir entre 18 et 100 ans.")
                    return
                anner.configure(border_color='#14a714', border_width=2)
            except ValueError:
                anner.configure(border_color='red', border_width=2)
                messagebox.showinfo('Erreur', 'Veuillez entrer une anner valide (uniquement des chiffres).')
    except Exception as e:
        print(f'Exception pr birthday est : {e}')
    #************************* exception pour le pseudo *************************
    try:
        user = pseudo.get()
        if user== '':
            pseudo.configure(border_color='red',border_width=2)
            messagebox.showinfo('Erreur', 'Veuillez entrer le pseudo !!')
            return
        else:
            pseudo.configure(border_color='#14a714', border_width=2)
    except Exception as e:
        print(f'Exception pr pseudo est : {e}')
    #************************* exception pour le email *************************
    try:
        tabrat = mail.get()
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", tabrat):
            mail.configure(border_color='red', border_width=2)
            messagebox.showinfo('Erreur', 'Veuillez corriger l email !!')
            return
        else:
            mail.configure(border_color='#14a714', border_width=2)
    except Exception as e:
        print(f'Exception pr pseudo est : {e}')
    #************************* exception pour le email *************************
    try:
        tele = phone.get()
        if tele=='':
            phone.configure(border_color='#14a714', border_width=2)
        else:
            caracteres_valides = ['0','1','','2','3','4','5','6','7','8','9','+','-','(',')',' ']
            for i in tele:
                if i not in caracteres_valides:
                    phone.configure(border_color='red', border_width=2)
                    messagebox.showinfo('Erreur','Veuillez corriger le numéro !!')
                    return
        phone.configure(border_color='#14a714', border_width=2)
    except Exception as e:
        print(f'Exception pr TELE est : {e}')
    #************************* exception globl *************************
    try:

        nhar = jour.get().strip()
        chher = mois.get().strip()
        eam = anner.get().strip()
        user = pseudo.get()
        tabrat = mail.get()
        tele = phone.get()
        NOM_COMPLET = fullname.get()
        KOUD_KDIM = r
        koud = new_Password.get()
        conf_koud = conf_password.get()
        ladrisa = adresse.get()
        mdina = ville.get()
        postal = code_postal.get()
        if koud != conf_koud:
            messagebox.showinfo('Erreur', 'Les mots de passe ne correspondent pas !')
            return
        else:
            with open('Gobet_data.csv', 'r', newline='', encoding='utf-8') as f:
                red = list(csv.reader(f, delimiter=';'))
                for i in red:
                    if i[0] == user_name():
                        red.remove(i)
                        break
            with open('Gobet_data.csv', 'w', newline='', encoding='utf-8') as fa:
                ecr = csv.writer(fa, delimiter=';')
                # ecr.writerow(['pseudo', 'email', 'password', 'new_password', 'real_name', 'jour', 'mois', 'anner',
                #               'telephone', 'adresse', 'ville', 'code_postal', 'chemin_image'])
                ecr.writerows(red)
                ecr.writerow(
                    [user, tabrat, KOUD_KDIM, koud, NOM_COMPLET, nhar, chher, eam, tele, ladrisa, mdina, postal,
                     chemin_image])
            messagebox.showinfo('Modification', 'Modification avec succes !!')
    except Exception as e:
        print(f'Exception survenu est : {e}')

def modifier():
    modif_password.place(relx=0.75, rely=0.53, anchor=CENTER)
    Password.configure(
        show='',
        state='readonly',
        border_width=2,

    )
    new_Password.configure(
        state='normal',
        border_width=2,
        placeholder_text='New Password...'
    )
    conf_password.configure(
        state='normal',
        border_width=2,
        placeholder_text='Confirmation Password...'
    )

def dowal():
    return ['Maroc','France','Egypt','Espagne','Algérie','Portugal',]

def user_name():
    utilisateur = ''
    with open('connection.csv', 'r', newline='', encoding='utf-8') as fc:
        con = list(csv.reader(fc, delimiter=';'))
        for i in con:
            for y in i:
                utilisateur += y
    return utilisateur

#fonction qui rend l'image cercle (L3Z ONSEEER L CHATGPT)
def round_corners(image):
    #rendre l'image carrees
    min_side = min(image.size)
    square_image = image.crop((0, 0, min_side, min_side))
    # Créer une image de même taille que l'image d'origine
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    # Dessiner des coins arrondis
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

    # Appliquer le masque
    rounded_image = Image.new('RGBA', image.size)
    rounded_image.paste(image, (0, 0), mask)

    return rounded_image

# Fonction pour demander une image
def choisir_image():
    global chemin_image
    # Ouvrir une boîte de dialogue pour choisir un fichier image
    chemin_image = filedialog.askopenfilename(
        title="Choisir une image",
        filetypes=[("IMG", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if chemin_image:
        try:
            image = Image.open(chemin_image).convert("RGBA")
            # Arrondir les coins de l'image
            rounded_image = round_corners(image)  # Ajustez le rayon ici
            # Vérifier si un fichier a été sélectionné
            img = ctk.CTkImage(
                light_image=rounded_image,
                size=(180,180)
            )
            pic.configure(
                image=img,
                text='',
                border_width=0,
                fg_color='#0c1b2c',
                width=10,
                height=20,
                hover_color='#0c1b2c'
            )
        except Exception as e:
            print(f'erreur de choix dimage{e}')
            return  None
def image_profile():
    try:
        with open('Gobet_data.csv','r',newline='',encoding='utf-8') as f:
            lec=list(csv.reader(f,delimiter=';'))
            for i in lec:
                if i[0]== user_name() :
                    chemin=i[-1]
                    PIC=Image.open(chemin).resize((150, 150)).convert("RGBA")
                    rounded_image = round_corners(PIC)
                    img=ctk.CTkImage(
                        light_image=rounded_image,
                         size=(150, 150)
                    )
                    return img
    except Exception as e:
        print(f'exception est : {e}')

def iwri():
    window.destroy()
    import game1


#***********************************************************************
    # LES LABELS
birthday=ctk.CTkLabel(frame1,text="-------------------BIRTHDAY-------------------", font=("AlterousText", 18), bg_color='#0c1b2c', text_color='white')
Cordonnees=ctk.CTkLabel(frame2,text="-----------------------------------------------LES CORDONNEES-----------------------------------------------", font=("AlterousText", 18), bg_color='#09111e', text_color='white')
Bank=ctk.CTkLabel(frame2,text="---------------------------------------------Methode de paiment---------------------------------------------", font=("AlterousText", 18), bg_color='#09111e', text_color='white')
    # input
fullname=ctk.CTkEntry(frame1,width=300,height=45,placeholder_text='Full Name...',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
#*********
ps=StringVar()
pseudo=ctk.CTkEntry(frame1,textvariable=ps,width=300,height=45,placeholder_text='User Name...',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
ps.set(p)
#*********
jour=ctk.CTkEntry(frame1,width=90,height=45,placeholder_text='Jour...',font=('Nexa Heavy',14),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
mois=ctk.CTkEntry(frame1,width=90,height=45,placeholder_text='Mois...',font=('Nexa Heavy',14),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
anner=ctk.CTkEntry(frame1,width=90,height=45,placeholder_text='Anner...',font=('Nexa Heavy',14),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
#*********
barid=StringVar()
mail=ctk.CTkEntry(frame2,textvariable=barid,width=320,height=45,placeholder_text='E-mail...',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
barid.set(b)
#*********
# telephone=StringVar()
phone=ctk.CTkEntry(frame2,placeholder_text='Phone...',width=320,height=45,font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
# telephone.set('phone...')
adresse=ctk.CTkEntry(frame2,width=320,height=45,placeholder_text='adresse...',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
ville=ctk.CTkEntry(frame2,width=150,height=45,placeholder_text='Ville...',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
code_postal=ctk.CTkEntry(frame2,width=150,height=45,placeholder_text='Code Postal...',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
#*********
code=StringVar()
Password=ctk.CTkEntry(frame2,width=320,height=45,textvariable=code,show='*',state='readonly',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
code.set(r)
#*********
new_Password=ctk.CTkEntry(frame2,width=320,height=45,state='readonly',font=('Nexa Heavy',16),corner_radius=25,border_width=0,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
conf_password=ctk.CTkEntry(frame2,width=320,height=45,state='readonly',font=('Nexa Heavy',16),corner_radius=25,border_width=0,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')

    # button
pic=ctk.CTkButton(frame1,text='',image=image_profile() ,command=lambda :choisir_image(),width=160,height=160,corner_radius=80,border_width=0,fg_color='#0c1b2c',bg_color='#0c1b2c',hover_color='#0c1b2c')
Save=ctk.CTkButton(frame1,text='Enregistrer',command=lambda : seter_les_donner(),width=140,height=45,corner_radius=25,border_width=2,font=('Nexa Heavy',16),fg_color='#14a714',bg_color='#0c1b2c',hover_color='#0d4914',border_color='#14a714')
back=ctk.CTkButton(frame1,text='Retourner',command= lambda : iwri(),width=140,height=45,corner_radius=25,border_width=2,font=('Nexa Heavy',16),fg_color='#0d4914',bg_color='#0c1b2c',hover_color='#14a714',border_color='#0d4914')
modif_password=ctk.CTkButton(frame2,text='Modifier Password',command=lambda :modifier(),width=320,height=45,corner_radius=25,border_width=2,font=('Nexa Heavy',16),fg_color='#0d3112',bg_color='#09111e',hover_color='#0d4914',border_color='#0d3112')
    #combobox
Pays=ctk.CTkComboBox(frame2,values=dowal(),state="readonly",font=('Nexa Heavy',16),width=320,height=45,corner_radius=25,fg_color='#09111e',text_color='white',border_color='#14a714')
Pays.set('Sélectionnez votre payer')

#***************positionnement***************
    #frame
frame1.place(relx=0.5,rely=0.5,anchor=CENTER)
frame2.place(relx=0.666,rely=0.499,anchor=CENTER)
    #labels
birthday.place(relx=0.175,rely=0.620,anchor=CENTER)
Cordonnees.place(relx=0.5,rely=0.05,anchor=CENTER)
Bank.place(relx=0.5,rely=0.62,anchor=CENTER)
    #input
#**f1
fullname.place(relx=0.175,rely=0.45,anchor=CENTER)
pseudo.place(relx=0.175,rely=0.55,anchor=CENTER)
jour.place(relx=0.08,rely=0.7,anchor=CENTER)
mois.place(relx=0.175,rely=0.7,anchor=CENTER)
anner.place(relx=0.27,rely=0.7,anchor=CENTER)
#***f2
mail.place(relx=0.25,rely=0.13,anchor=CENTER)
phone.place(relx=0.25,rely=0.23,anchor=CENTER)
adresse.place(relx=0.25,rely=0.33,anchor=CENTER)
ville.place(relx=0.13,rely=0.53,anchor=CENTER)
code_postal.place(relx=0.37,rely=0.53,anchor=CENTER)
#***
Password.place(relx=0.75,rely=0.13,anchor=CENTER)
new_Password.place(relx=0.75,rely=0.23,anchor=CENTER)
conf_password.place(relx=0.75,rely=0.33,anchor=CENTER)
    # button
pic.place(relx=0.175,rely=0.18,anchor=CENTER)
Save.place(relx=0.1,rely=0.85,anchor=CENTER)
back.place(relx=0.245,rely=0.85,anchor=CENTER)
modif_password.place(relx=0.75,rely=0.23,anchor=CENTER)
    #comcobox
Pays.place(relx=0.25,rely=0.43,anchor=CENTER)

#***************boucler la feneter****************
window.mainloop()