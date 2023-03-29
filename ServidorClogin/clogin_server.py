import socket
import threading

ip = "172.21.233.33"
port = 8432

srv_clogin = socket.socket()
srv_clogin.bind((ip, port))
srv_clogin.listen(100)
socket_id_clientes = []
nombre_clientes = []

def recibir_mensajes(conn, addr):
    while True:
        try:
            missatge = conn.recv(1024)
            if missatge:
                missatge_val = missatge.decode()
                if "+" in missatge_val:
                    index_eliminar_client = missatge_val.index("+")
                    eliminar_client(missatge_val[index_eliminar_client+1:])
                else:
                    enviar_mensajes(missatge)  
        except:
            pass

def eliminar_client(nom):
    global nombre_clientes
    global socket_id_clientes
    index_si = nombre_clientes.index(nom)
    socket_id_clientes.pop(index_si)
    print("{} a marxat del xat".format(nom))
    nombre_clientes.pop(index_si)

def client_fallido_inici_sessio(conn):
    global socket_id_clientes
    global nombre_clientes
    while True:
        try:
            missatge = conn.recv(1024)
            if missatge:
                if "$" in missatge.decode():
                    missatge = nom_client.decode()
                    index_mes = missatge.index("$")
                    index_dos_punts = missatge.index("¿")
                    nom_client_registrar = missatge[index_mes+1:index_dos_punts]
                    contrasenya_registre_usuari = missatge[index_dos_punts+1:]

                    verificar_nom_registre_existent = open("basedades.txt", "r")
                    llegir_verificar_nom_registre_existent = verificar_nom_registre_existent.read()
                    llista_verificar_nom_registre_existent = llegir_verificar_nom_registre_existent.split(",")
                    verificar_nom_registre_existent.close()
                    if "{}:{}".format(nom_client_registrar,contrasenya_registre_usuari) in llista_verificar_nom_registre_existent:
                        conn.send("Error".encode())
                    else:
                        base_dades = open("basedades.txt", "a")
                        base_dades.write(",{}:{}".format(nom_client_registrar,contrasenya_registre_usuari))
                        print("S'ha registrar l'usuari {}".format(nom_client_registrar))
                        base_dades.close()
                        conn.send("Correct".encode())
                else :
                    base_dades_inici = open("basedades.txt", "r")
                    llegir_base_dades_inici = base_dades_inici.read()
                    llista_verificadora_usuari = llegir_base_dades_inici.split(",")
                    nom_verifer_inici_sessio = missatge.decode()
                    index_protocol_inici_sessio = nom_verifer_inici_sessio.index("&")
                    nom_usuari_inci_sessio = nom_verifer_inici_sessio[0:index_protocol_inici_sessio]
                    contrasenya_inici_sessio = nom_verifer_inici_sessio[index_protocol_inici_sessio+1:]
                    base_dades_inici.close()
                    print("{}:{}".format(nom_usuari_inci_sessio, contrasenya_inici_sessio))
                    if "{}:{}".format(nom_usuari_inci_sessio,contrasenya_inici_sessio) in llista_verificadora_usuari and nom_verifer_inici_sessio not in nombre_clientes:
                    #if nom_client.decode() not in nombre_clientes:
                        socket_id_clientes.append(conn)
                        nombre_clientes.append(nom_usuari_inci_sessio)
                        print("S'ha connectat l'usuari {} amb la IP --> {}".format(nom_usuari_inci_sessio, "ip"))
                        conn.send("Correct".encode())  
                        ejecutar_funcio2 = threading.Thread(target=recibir_mensajes, args=(conn, "ip"))
                        ejecutar_funcio2.daemon = True
                        ejecutar_funcio2.start()
                        break
                    else:
                        conn.send("Error".encode())
        except:
            pass

def client_fallido_registre_sessio(conn):
    while True:
        try:
            missatge_registre = conn.recv(1024)
            if missatge_registre:
                if "&" in missatge_registre.decode():
                    base_dades_inici = open("basedades.txt", "r")
                    llegir_base_dades_inici = base_dades_inici.read()
                    llista_verificadora_usuari = llegir_base_dades_inici.split(",")
                    nom_verifer_inici_sessio = missatge_registre.decode()
                    index_protocol_inici_sessio = nom_verifer_inici_sessio.index("&")
                    nom_usuari_inci_sessio = nom_verifer_inici_sessio[0:index_protocol_inici_sessio]
                    contrasenya_inici_sessio = nom_verifer_inici_sessio[index_protocol_inici_sessio+1:]
                    base_dades_inici.close()
                    print("{}:{}".format(nom_usuari_inci_sessio, contrasenya_inici_sessio))
                    if "{}:{}".format(nom_usuari_inci_sessio,contrasenya_inici_sessio) in llista_verificadora_usuari and nom_verifer_inici_sessio not in nombre_clientes:
                    #if nom_client.decode() not in nombre_clientes:
                        socket_id_clientes.append(conn)
                        nombre_clientes.append(nom_usuari_inci_sessio)
                        print("S'ha connectat l'usuari {} amb la IP --> {}".format(nom_usuari_inci_sessio, "ip"))
                        conn.send("Correct".encode())  
                        ejecutar_funcio2 = threading.Thread(target=recibir_mensajes, args=(conn, "ip"))
                        ejecutar_funcio2.daemon = True
                        ejecutar_funcio2.start()
                        break
                    else:
                        conn.send("Error".encode())
                else:
                    missatge_registre = nom_client.decode()
                    index_mes = missatge_registre.index("$")
                    index_dos_punts = missatge_registre.index("¿")
                    nom_client_registrar = missatge_registre[index_mes+1:index_dos_punts]
                    contrasenya_registre_usuari = missatge_registre[index_dos_punts+1:]

                    verificar_nom_registre_existent = open("basedades.txt", "r")
                    llegir_verificar_nom_registre_existent = verificar_nom_registre_existent.read()
                    llista_verificar_nom_registre_existent = llegir_verificar_nom_registre_existent.split(",")
                    verificar_nom_registre_existent.close()
                    if "{}:{}".format(nom_client_registrar,contrasenya_registre_usuari) in llista_verificar_nom_registre_existent:
                        conn.send("Error".encode())
                    else:
                        base_dades = open("basedades.txt", "a")
                        base_dades.write(",{}:{}".format(nom_client_registrar,contrasenya_registre_usuari))
                        print("S'ha registrar l'usuari {}".format(nom_client_registrar))
                        base_dades.close()
                        conn.send("Correct".encode()) 
        except:
            pass

def enviar_mensajes(mss):
    mss = mss.decode()
    index_nom_a_enviar = mss.index("-")
    nom_a_enviar = mss[0:index_nom_a_enviar]
    index_nom_verificacio_user = mss.index("_")
    nom_verificacio_user = mss[index_nom_verificacio_user+1:]
    missatge_enviar = mss[index_nom_a_enviar+1:index_nom_verificacio_user]
    indice_nombre_cliente = nombre_clientes.index(nom_a_enviar)
    connexion_enviar_mensaje = socket_id_clientes[indice_nombre_cliente]
    try:
        connexion_enviar_mensaje.send("{},{}".format(nom_verificacio_user,missatge_enviar).encode())
    except:
        pass 
        
while True:
    connexio, address = srv_clogin.accept()
    nom_client = connexio.recv(1024)
    if "$" in nom_client.decode():
        missatge_registre = nom_client.decode()
        index_mes = missatge_registre.index("$")
        index_dos_punts = missatge_registre.index("¿")
        nom_client_registrar = missatge_registre[index_mes+1:index_dos_punts]
        contrasenya_registre_usuari = missatge_registre[index_dos_punts+1:]

        verificar_nom_registre_existent = open("basedades.txt", "r")
        llegir_verificar_nom_registre_existent = verificar_nom_registre_existent.read()
        llista_verificar_nom_registre_existent = llegir_verificar_nom_registre_existent.split(",")
        verificar_nom_registre_existent.close()
        if "{}:{}".format(nom_client_registrar,contrasenya_registre_usuari) in llista_verificar_nom_registre_existent:
            connexio.send("Error".encode())
            print("L'usuari ja existeix")
            ejecutar_funcio_client_en_espera_registre = threading.Thread(target=client_fallido_registre_sessio, args=(connexio,))
            ejecutar_funcio_client_en_espera_registre.daemon = True
            ejecutar_funcio_client_en_espera_registre.start()
        else:
            base_dades = open("basedades.txt", "a")
            base_dades.write(",{}:{}".format(nom_client_registrar,contrasenya_registre_usuari))
            print("S'ha registrar l'usuari {}".format(nom_client_registrar))
            base_dades.close()
            connexio.send("Correct".encode())
            ejecutar_funcio_client_en_espera4 = threading.Thread(target=client_fallido_inici_sessio, args=(connexio,))
            ejecutar_funcio_client_en_espera4.daemon = True
            ejecutar_funcio_client_en_espera4.start()  
    else: 
        base_dades_inici = open("basedades.txt", "r")
        llegir_base_dades_inici = base_dades_inici.read()
        llista_verificadora_usuari = llegir_base_dades_inici.split(",")
        nom_verifer_inici_sessio = nom_client.decode()
        index_protocol_inici_sessio = nom_verifer_inici_sessio.index("&")
        nom_usuari_inci_sessio = nom_verifer_inici_sessio[0:index_protocol_inici_sessio]
        contrasenya_inici_sessio = nom_verifer_inici_sessio[index_protocol_inici_sessio+1:]
        base_dades_inici.close()
        print("{}:{}".format(nom_usuari_inci_sessio, contrasenya_inici_sessio))
        if "{}:{}".format(nom_usuari_inci_sessio,contrasenya_inici_sessio) in llista_verificadora_usuari and nom_usuari_inci_sessio not in nombre_clientes:
        #if nom_client.decode() not in nombre_clientes:
            socket_id_clientes.append(connexio)
            nombre_clientes.append(nom_usuari_inci_sessio)
            print("S'ha connectat l'usuari {} amb la IP --> {}".format(nom_usuari_inci_sessio, address))
            connexio.send("Correct".encode())  
            ejecutar_funcio = threading.Thread(target=recibir_mensajes, args=(connexio, address))
            ejecutar_funcio.daemon = True
            ejecutar_funcio.start()
        else:
            connexio.send("Error".encode())
            ejecutar_funcio_client_en_espera = threading.Thread(target=client_fallido_inici_sessio, args=(connexio,))
            ejecutar_funcio_client_en_espera.daemon = True
            ejecutar_funcio_client_en_espera.start()
            #connexio.close()
            #srv_clogin = socket.socket()

        
