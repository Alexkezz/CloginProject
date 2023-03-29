from tkinter import *
import socket
import threading
from tkinter import ttk

validator_ventana_ajustes_generales = 0
def destory_ventana_ajustes_generales():
    global validator_ventana_ajustes_generales
    validator_ventana_ajustes_generales = 0
    menu_configuracio.destroy()

def modificacio_estats_usuari(valor):
    global estat_usuari
    estat_usuari.config(text=valor)

def ventana_configuracio_general_usuari():
    global estat_usuari
    global menu_configuracio
    global validator_ventana_ajustes_generales
    if validator_ventana_ajustes_generales == 0:
        validator_ventana_ajustes_generales = 1
        menu_configuracio = Toplevel()
        menu_configuracio.geometry("500x600")
        menu_configuracio.resizable(0,0)
        menu_configuracio.title("Configuració General")
        menu_configuracio.config(bg="#8cb3ff")
        imatge_menu_configuracio = PhotoImage(file="contactes.png")
        imatge_menu_configuracio = imatge_menu_configuracio.subsample(3)
        menu_imatge_configuracio = Label(menu_configuracio, image=imatge_menu_configuracio, bg="#8cb3ff")
        menu_imatge_configuracio.place(x=0, y=50)
        espai_titol_configuracio = Frame(menu_configuracio, width=500, height=55, relief="solid", borderwidth=2, bg="#4682B4",)
        espai_titol_configuracio.place(x=0, y=0)
        ajustes = PhotoImage(file="botoajustes.png")
        ajustes = ajustes.subsample(23)
        imatge_ajustes_menu_usuari = Label(espai_titol_configuracio, image=ajustes, bg="#4682b4")
        imatge_ajustes_menu_usuari.place(x=70, y=12)
        nom_titol_configuracio = Label(espai_titol_configuracio, text="CONFIGURACIÓ GENERAL", font=("THIN", 18, "bold"), bg="#4682b4", fg="white")
        nom_titol_configuracio.place(x=100, y=7)
        nom_usuari_configuracio = Label(menu_configuracio, text="Usuari", font=("THIN", 18, "bold"), bg="#8cb3ff")
        nom_usuari_configuracio.place(x=200, y=80)
        canviar_estat = Menubutton(menu_configuracio, text="Canviar estat", font=("THIN", 12, "bold"), bg="#606fff", cursor="hand2", fg="#ffee04", activebackground="#ffff98", activeforeground="#606fff")
        canviar_estat.place(x=200, y=150)
        estat_usuari = Label(menu_configuracio, bg="#8cb3ff", fg="white", font=("THIN", 14, "bold"), cursor="hand2")
        estat_usuari.place(x=335, y=150)
        menu_estat = Menu(canviar_estat, tearoff=False, bg="#606fff", fg="white")
        menu_estat.add_radiobutton(label="Desconnectat", font=("THIN", 12, "bold"), command= lambda:modificacio_estats_usuari("Desconnectat"))
        menu_estat.add_radiobutton(label="Connectat", font=("THIN", 12, "bold"),command= lambda:modificacio_estats_usuari("Connectat"))
        menu_estat.add_radiobutton(label="Treballant", font=("THIN", 12, "bold"), command= lambda:modificacio_estats_usuari("Treballant"))
        menu_estat.add_radiobutton(label="Estic en l'escola", font=("THIN", 12, "bold"), command= lambda:modificacio_estats_usuari("Estic a l'escola"))
        menu_estat.add_radiobutton(label="No molestis", font=("THIN", 12, "bold"), command= lambda:modificacio_estats_usuari("No molestis"))
        canviar_estat["menu"] = menu_estat
        titol_canviar_tema = Label(menu_configuracio, text="Canviar tema", font=("THIN", 12, "bold"), bg="#8cb3ff")
        titol_canviar_tema.place(x=45, y=250)
        canviar_nom_usuari = Label(menu_configuracio, text="Canviar el teu nom", font=("THIN", 12, "bold"), bg="#8cb3ff")
        canviar_nom_usuari.place(x=45, y=320)
        entry_canviar_nom = Entry(menu_configuracio, width=20, borderwidth=1, relief="solid", font=("THIN", 14))
        entry_canviar_nom.place(x=230, y=323)
        boto_canviar_nom_usuari = Button(menu_configuracio, text=">>", font=("THIN", 10, "bold"), borderwidth=0, cursor="hand2", activebackground="#ffff98",fg="#ffee04", bg="#606fff", activeforeground="#606fff")
        boto_canviar_nom_usuari.place(x=465, y=323)
        canviar_contrasenya = Label(menu_configuracio, text="Canviar contrasenya", font=("THIN", 12, "bold"), bg="#8cb3ff")
        canviar_contrasenya.place(x=45, y=390)
        clau = PhotoImage(file="clau.png")
        clau = clau.subsample(20)
        imatge_clau = Label(menu_configuracio, image=clau, bg="#8cb3ff")
        imatge_clau.place(x=2, y=390)
        imatge_usuaris = PhotoImage(file="usuari.png")
        imatge_usuaris = imatge_usuaris.subsample(22)
        foto_usuaris = Label(menu_configuracio, image=imatge_usuaris, bg="#8cb3ff")
        foto_usuaris.place(x=2, y=316)
        entry_canviar_contrasenya = Entry(menu_configuracio, width=20, borderwidth=1, relief="solid", font=("THIN", 14))
        entry_canviar_contrasenya.place(x=230, y=392)
        entry_canviar_contrasenya.config(show="*")
        boto_canviar_contrasenya = Button(menu_configuracio, text=">>", font=("THIN", 10, "bold"), borderwidth=0, cursor="hand2", activebackground="#ffff98",fg="#ffee04", bg="#606fff", activeforeground="#606fff")
        boto_canviar_contrasenya.place(x=465, y=393)
        llista_usuaris_bloquejats = Button(menu_configuracio, text= " Usuaris Bloquejats", font=("THIN", 16, "bold"), borderwidth=0, cursor="hand2", activebackground="#ffff98",fg="#ffee04", bg="#606fff", activeforeground="#606fff", bitmap="error", compound="left")
        llista_usuaris_bloquejats.place(x=150, y=500)
        linia_separar_ajustes = Frame(menu_configuracio, width=500, height=2, relief="solid", bg="black")
        linia_separar_ajustes.place(x=0, y=220)
        camera = PhotoImage(file="camera.png")
        camera = camera.subsample(45)
        imatge_camera = Label(menu_configuracio, image=camera, bg="#8cb3ff")
        imatge_camera.place(x=2, y=245)
        boto_clar_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1)
        boto_clar_tema.place(x=230, y=250)
        boto_blau_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="blue")
        boto_blau_tema.place(x=258, y=250)
        boto_verd_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="green")
        boto_verd_tema.place(x=287, y=250)
        boto_fosc_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="black")
        boto_fosc_tema.place(x=316, y=250)
        boto_vermell_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="red")
        boto_vermell_tema.place(x=345, y=250)
        boto_groc_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="yellow")
        boto_groc_tema.place(x=374, y=250)
        boto_lila_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="purple")
        boto_lila_tema.place(x=403, y=250)
        boto_taronja_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="orange")
        boto_taronja_tema.place(x=432, y=250)
        menu_configuracio.protocol("WM_DELETE_WINDOW",destory_ventana_ajustes_generales)
        menu_configuracio.mainloop()

validator_ventana_afegir_usuaris = 0
def destory_ventana_afegir_usuaris():
    global validator_ventana_afegir_usuaris
    validator_ventana_afegir_usuaris = 0
    ventana_afegir_usuaris.destroy()

def nom_conversa_usuari(nombre):
    name_user = nombre
    nom_usuari.config(text=name_user)

filas_contactos = 0
def boto_nou_usuari(nom_del_usuari):
    global filas_contactos
    nom_del_usuari = nom_del_usuari.strip()
    if nom_del_usuari != "":
        lletres_vermelles = Label(ventana_afegir_usuaris, text="Contacte afegit!", font=("THIN", 12, "bold"), fg="black", bg="#8cb3ff")
        lletres_vermelles.place(x=80, y=180)
        Button(sframe, text=nom_del_usuari, width=20, font=("Calibri", 13, "bold"), borderwidth=1, relief="solid", bg="#606fff", cursor="hand2",fg="#ffee04", command=lambda nom_del_usuari=nom_del_usuari:nom_conversa_usuari(nom_del_usuari)).grid(row=filas_contactos, column=1, pady=15, padx=(5, 0))
        Label(sframe, image=foto_usuari_perfil_lateral_2, borderwidth=0, bg="#84C4F4").grid(row=filas_contactos, column=0, pady=15)
        filas_contactos += 1

def finestra_afegir_usuaris():
    global ventana_afegir_usuaris
    global validator_ventana_afegir_usuaris
    if validator_ventana_afegir_usuaris == 0:
        validator_ventana_afegir_usuaris = 1
        ventana_afegir_usuaris = Toplevel()
        ventana_afegir_usuaris.geometry("600x300")
        ventana_afegir_usuaris.config(bg="#8cb3ff")
        ventana_afegir_usuaris.title("Afegir usuaris")
        ventana_afegir_usuaris.resizable(0,0)
        ventana_afegir_usuaris.geometry("+375+125")
        titol_usuaris = Label(ventana_afegir_usuaris, text="Afegir usuaris", font=("THIN", 18, "bold"), bg="#8cb3ff")
        titol_usuaris.place(x=62, y=45)
        introduir_nom_usuari = Label(ventana_afegir_usuaris, text="Introdueix el nom de l'usuari", font=("THIN", 16), bg="#8cb3ff")
        introduir_nom_usuari.place(x=17, y= 100)
        nom_afegir_usuari = Entry(ventana_afegir_usuaris, font=("Calibri", 16), borderwidth=1, relief="solid", bg="#ffffff")
        nom_afegir_usuari.place(x=35, y=150)
        boto_afegir_usuaris = Button(ventana_afegir_usuaris, text="Afegeix", fg="#ffee04",bg="#606fff", cursor="hand2",font=("Calibri", 13, "bold"),width=14, borderwidth=0, activebackground="#ffff98", activeforeground="#606fff", command=lambda:boto_nou_usuari(nom_afegir_usuari.get()))
        boto_afegir_usuaris.place(x=78,y=210 )
        imatge_usuari = PhotoImage(file="contactes.png")
        tamany_imatge = imatge_usuari.subsample(2)
        imatge_ventana = Label(ventana_afegir_usuaris, image=tamany_imatge, bg="#8cb3ff")
        imatge_ventana.place(x=330, y=10)
        ventana_afegir_usuaris.protocol("WM_DELETE_WINDOW", destory_ventana_afegir_usuaris)
        ventana_afegir_usuaris.mainloop()
    
def validacio_conta(name, password):
    name = name.strip()
    password = password.strip()
    if name != "" and password != "":
        nom_tretze = confirmacio_nom_usuari_tretze()
        if nom_tretze == False:
            root.destroy()
            ventana_chat_principal(name.capitalize())

def validacio_conta_registre_sessio(name_registre, password_registre, validator):
    name_registre = name_registre.strip()
    password_registre = password_registre.strip()
    if name_registre != "" and password_registre != "":
        if validator == False:
            try:
                ventana.destroy()
            except:
                pass
            ventana_chat_principal(name_registre.capitalize())

def ventana_chat_principal(nom_usuari_lateral):
    global nom_usuari
    global widget_text_conversa
    global chat_ventana
    global name_user
    global inp_chat
    global sframe
    global foto_usuari_perfil_lateral_2

    name_user = "Usuari"
    chat_ventana = Tk()
    chat_ventana.title("Clogin")
    chat_ventana.geometry("1131x668")
    chat_ventana.resizable(0, 0)

    # Frame Lateral --------------------------------------------------------------------------------------------

    frame_lateral = Frame(chat_ventana, bg="#84C4F4", width=270, height=668, borderwidth=2, relief="solid")
    frame_lateral.place(x=0)

    photo_logo_clogin = PhotoImage(file="logo.png")
    photo_logo_clogin = photo_logo_clogin.subsample(22)
    logo_clogin = Label(frame_lateral, image=photo_logo_clogin, borderwidth=0, bg="#84C4F4")
    logo_clogin.place(x=0, y=0)

    nom_clogin = Label(frame_lateral, text="CLOGIN", font=("Calibri", 12, "bold"), bg="#84C4F4", fg="#ffffff")
    nom_clogin.place(x=40, y=11)

    line_clogin_sota = Frame(frame_lateral, width=266, height=2, bg="black")
    line_clogin_sota.place(x=0, y=45)

    imagen_ajustes_generales_button = PhotoImage(file="botoajustes.png")
    imagen_ajustes_generales_button = imagen_ajustes_generales_button.subsample(23)
    ajustes_generales_button = Button(frame_lateral, image=imagen_ajustes_generales_button, borderwidth=0, bg="#84C4F4", cursor="hand2", activebackground="#84C4F4", command=ventana_configuracio_general_usuari)
    ajustes_generales_button.place(x=230, y=10)

    foto_afegir_contactes = PhotoImage(file="adduser.png")
    foto_afegir_contactes = foto_afegir_contactes.subsample(23)
    afegir_contactes = Button(frame_lateral, image=foto_afegir_contactes, borderwidth=0, bg="#84C4F4", cursor="hand2", activebackground="#84C4F4", command=finestra_afegir_usuaris)
    afegir_contactes.place(x=195, y=10)

    label_tu_cuenta = Label(frame_lateral, text="Has iniciat sessió amb:", font=("Calibri", 16, "bold"), bg="#84C4F4", fg="black")
    label_tu_cuenta.place(x=35, y=50)

    foto_usuari_perfil_lateral = PhotoImage(file="second_foto.png")
    foto_usuari_perfil_lateral = foto_usuari_perfil_lateral.subsample(13)
    usuari_foto = Label(frame_lateral, image=foto_usuari_perfil_lateral, borderwidth=0, bg="#84C4F4")
    usuari_foto.place(x=25, y=85)

    my_name = Label(frame_lateral, text=nom_usuari_lateral, font=("Calibri", 15, "bold"), bg="#84C4F4")
    my_name.place(x=125, y=110)

    contacts_label = Label(frame_lateral, text="Contactes:", font=("Calibri", 16, "bold"), bg="#84C4F4")
    contacts_label.place(x=85, y=170)

    frame_usuaris_afegits = Frame(frame_lateral, bg="#84C4F4", width=266, height=464, borderwidth=0)
    frame_usuaris_afegits.place(x=0, y=200)

    main_frame = Frame(frame_usuaris_afegits, bg="#84C4F4")
    main_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(main_frame, bg="#84C4F4", width=250, height=464, highlightthickness=0, relief="ridge")
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scroll = ttk.Scrollbar(main_frame, orient=VERTICAL,command=canvas.yview)
    scroll.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scroll.set)
    canvas.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

    sframe = Frame(canvas, bg="#84C4F4")
    canvas.create_window((0, 0), window=sframe, anchor="nw")

    foto_usuari_perfil_lateral_2 = PhotoImage(file="contactes.png")
    foto_usuari_perfil_lateral_2 = foto_usuari_perfil_lateral_2.subsample(11)
    #Button(sframe, text="", width=20, font=("Calibri", 13, "bold"), borderwidth=0, bg="#84C4F4").grid(row=i, column=1, pady=15, padx=(5, 0))

    for i in range(100):
        Label(sframe, text="", font=("Calibri", 13, "bold"), borderwidth=0, bg="#84C4F4").grid(row=i, column=1, pady=15, padx=(5, 0))
    
    # Frame Conversa -------------------------------------------------------------------------------------------

    frame_conversa = Frame(chat_ventana, bg="#ffffff", width=863, height=668, borderwidth=2, relief="solid")
    frame_conversa.place(x=268)

    frame_usuari = Frame(frame_conversa, bg="#4682B4", width=859, height=78, borderwidth=0)
    frame_usuari.place(x=0)

    nom_usuari = Label(frame_usuari, bg="#4682B4", text=name_user, font=("Calibri", 20, "bold"))
    nom_usuari.place(x=70, y=18)

    foto_usuari_perfil = PhotoImage(file="foto_perfil.png")
    foto_usuari_perfil = foto_usuari_perfil.subsample(10)
    usuari_foto = Label(frame_usuari, image=foto_usuari_perfil, borderwidth=0, bg="#4682B4")
    usuari_foto.place(x=12, y=12)

    inp_chat = Entry(frame_conversa, font=("THIN", 19), bg="#2C3E50", fg="#ffffff", width=55, borderwidth=0)
    inp_chat.place(x=0, y=634)

    send_button = Button(frame_conversa, font=("THIN", 13), bg="#1A5276", text=">>", borderwidth=0, width=9)
    send_button.place(x=772, y=634)

    frame_per_omplir_boto = Frame(frame_conversa, bg="#1A5276", borderwidth=3, width=87)
    frame_per_omplir_boto.place(x=772, y=663)

    ajustes_button = PhotoImage(file="tres_punts.png")
    ajustes_button = ajustes_button.subsample(19)
    label_ajustes_button = Menubutton(frame_usuari, image=ajustes_button, borderwidth=0, bg="#4682B4", activebackground="#4682B4", cursor="hand2")
    label_ajustes_button.place(x=810, y=25)
    menu = Menu(label_ajustes_button, tearoff=False, bg="#61758B", fg="#ffffff")
    menu.add_radiobutton(label="Bloquejar", font=("Calibri", 13, "bold"))
    menu.add_radiobutton(label="Arxivar", font=("Calibri", 13, "bold"))
    menu.add_radiobutton(label="Ancorar", font=("Calibri", 13, "bold"))
    label_ajustes_button["menu"] = menu

    frame_conversa_del_chat = Frame(frame_conversa, width=859, height=556, bg="white",borderwidth=0)
    frame_conversa_del_chat.place(x=0, y=78)

    scroll_widget_conversa = Scrollbar(frame_conversa_del_chat)
    scroll_widget_conversa.pack(side=RIGHT, fill=Y)

    widget_text_conversa = Text(frame_conversa_del_chat, width=76, height=24, bg="white", borderwidth=0, font=("THIN", 15))
    widget_text_conversa.pack(side=LEFT, fill=Y)

    scroll_widget_conversa.config(command=widget_text_conversa.yview)
    widget_text_conversa.config(yscrollcommand=scroll_widget_conversa.set)
    # ----------------------------------------------------------------------------------------------------------
    chat_ventana.mainloop()
    
def ventana_registredesessio():
    global ventana
    global inpnom
    root.destroy()
    ventana = Tk()
    ventana.geometry("400x600")
    ventana.geometry("+475+50")
    ventana.resizable(0,0)
    ventana.title("Registra't")
    ventana.config(bg="#FFFFFF")

    logoclogin = PhotoImage(file="logo.png")
    zoom_logo = logoclogin.subsample(7)
    photo = Label(ventana, image=zoom_logo, bg="#FFFFFF")
    photo.place(x=125, y=0)

    nomusuari = Label(ventana, text="Nom d'usuari", font=("THIN", 16), bg="#FFFFFF")
    nomusuari.place(x=135, y=170)

    password = Label(ventana, text="Contrasenya", font=("THIN", 16), bg="#FFFFFF")
    password.place(x=135, y=260)

    inpnom = Entry(ventana, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inpnom.place(x=28, y=205)

    inpcontrasenya = Entry(ventana, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inpcontrasenya.place(x=28, y=295)
    inpcontrasenya.config(show="*")

    confirmaciopassword = Label(ventana, text="Repeteix la contrasenya", font=("THIN", 16), bg="#FFFFFF")
    confirmaciopassword.place(x=80, y=360)

    inpconfirmaciocontrasenya = Entry(ventana, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inpconfirmaciocontrasenya.place(x=28, y=395)
    inpconfirmaciocontrasenya.config(show="*")

    botonsingup = Button(ventana, text="Registra't", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=18, borderwidth=0, command=lambda:confirmacio_nom_usuari_tretze_registre_sessio(inpnom.get(), inpcontrasenya.get(), inpconfirmaciocontrasenya.get()), activebackground="#ffff98", activeforeground="#606fff")
    botonsingup.place(x=108, y=475)

    imatgeenrere = PhotoImage(file="enrere.png")
    imatgeenrere = imatgeenrere.subsample(10)

    enrere = Button(ventana, command=ventana_inicidesessio, image = imatgeenrere, borderwidth=0, bg="#FFFFFF", cursor="hand2")
    enrere.place(x=12, y=20)

    ventana.mainloop()

def ventana_inicidesessio():
    global root
    global inp_nom
    try:
        ventana.destroy()
    except:
        pass
    root = Tk()
    root.geometry("400x600")
    root.geometry("+475+50")
    root.resizable(0,0)
    root.title("Iniciar sessió")
    root.config(bg="#FFFFFF")
    
    logo_clogin = PhotoImage(file="logo.png")
    zoom = logo_clogin.subsample(7)
    foto = Label(root, image=zoom, bg="#FFFFFF")
    foto.place(x=125, y=0)

    nom_usuari = Label(root, text="Nom d'usuari", font=("THIN", 16), bg="#FFFFFF")
    nom_usuari.place(x=135, y=165)

    contrasenya = Label(root, text="Contrasenya", font=("THIN", 16), bg="#FFFFFF")
    contrasenya.place(x=135, y=265)

    inp_nom = Entry(root, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inp_nom.place(x=28, y=200)

    inp_contrasenya = Entry(root, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inp_contrasenya.place(x=28, y=300)
    inp_contrasenya.config(show="*")

    boton_singup = Button(root, text="Entra", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=18, borderwidth=0, activebackground="#ffff98", activeforeground="#606fff", command=lambda:validacio_conta(inp_nom.get(), inp_contrasenya.get()))
    boton_singup.place(x=105, y=370)

    lab_register = Label(root, text="No tens compte?", font=("THIN", 14, "underline"), bg="#FFFFFF")
    lab_register.place(x=35, y=530)

    button_register = Button(root, text="Registra't", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=16, borderwidth=0, command=ventana_registredesessio, activebackground="#ffff98", activeforeground="#606fff")
    button_register.place(x=195, y=525)
    
    root.mainloop()     

def confirmacio_nom_usuari_tretze():
    validator_nom_tretze_usuari = False
    if len(inp_nom.get()) > 13:
        error_nom_usuari = Label(root, text="Hi han més de 13 caràcters", font=("Calibri", 12, "bold"), fg="red", bg="white")
        error_nom_usuari.place(x=100, y=235)
        validator_nom_tretze_usuari = True
    return validator_nom_tretze_usuari

def confirmacio_nom_usuari_tretze_registre_sessio(nom_confirmer, contraseña_confirmer, repeteix_contraseña_confirmer):
    validator_registre = False

    if len(nom_confirmer) > 13:
        error_nom_usuari_registre = Label(ventana, text="Hi han més de 13 caràcters", font=("Calibri", 12, "bold"), fg="red", bg="white")
        error_nom_usuari_registre.place(x=100, y=240)
        validator_registre = True

    if contraseña_confirmer != repeteix_contraseña_confirmer:
        error = Label(ventana, text="Les contrasenyes no coincideixen", font=("Calibri", 12, "bold"), fg="red", bg="#FFFFFF")
        error.place(x= 88, y= 430)
        validator_registre = True

    validacio_conta_registre_sessio(nom_confirmer, contraseña_confirmer, validator_registre)

ventana_inicidesessio()
#------------------------------------------------------------------------------------------------------------------------

