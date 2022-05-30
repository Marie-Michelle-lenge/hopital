from Docteur import *
from Patient import *
dossiers = []
liste_patients = [] 
liste_docteurs = []
def liste_vide(patients, docteurs):
    if not patients:
        #raise
        return True
    elif not docteurs:
        #raise
        return True

def main(): 

    while True:
        print("\n BIENVENU DANS NOTRE HOPITAL!! que comptez vous faire??: \n \
            1: Enregistrer un Docteur? \n \
            2: Enregistrer un patient? \n \
            3: Cherchez vous un patient? \n \
            4: Chercher un patient a l'aide de son Numero du dossier \n \
            5: Afficher Tout les patients \n \
            6: Afficher tout les docteurs \n \
            7: Enregistrer plainte \n \
            8: Afficher plainte a l'aide du Numero dossier \n \
            9: Afficher l'IMC a l'aide du Numero dossier \n \
            10: Enregistrer l'horaire de chaque docteur \n \
            11: Vérifié la disponibilité d'un docteur? \n \
            12: Quitter le programme? \n \
                ")

        try:    
            choix = int(input(""))
        except ValueError:
            print("entrer un chiffre Svp !!!")
            continue
        match choix:
            case 1: 

                nom_docteur = (input("nom du Docteur: ")).upper()
                
                postnom_docteur = (input("postnom du docteur: ")).upper()
                
                prenom_docteur = (input("prenom du docteur: ")).upper()
                
                telephone_docteur = input("numero de Telephone du docteur: ")
                
                matricule = generation_matricule(liste_docteurs, nom_docteur, postnom_docteur)
                
                specialisation = (input("specialisiation du docteur: ")).capitalize()
                
                nouveau_docteur = (enregistrer_un_docteur(
                                                        nom_docteur, postnom_docteur,
                                                        prenom_docteur, telephone_docteur,
                                                        matricule, specialisation))

                #MARIE MICHELLE
                vft = 0
                if liste_docteurs:
                    for i in range(len(liste_docteurs)):
                        if nouveau_docteur[:5] == liste_docteurs[i][:5]:
                            print("ce medecin existe ! ")
                            vft+= 1

                if vft == 0:
                    liste_docteurs.append(nouveau_docteur)

            case 2: 

                nom_patient = (input("nom du patient: ")).upper()
                
                postnom_patient = (input("postnom du patient: ")).upper()
                
                prenom_patient = (input("prenom du patient: ")).upper()
                
                telephone_patient = input("numero de Telephone du patient: ")
                
                poid_patient = input("poid du patients(0.00): ")
                
                taille_patient = input(" taille du patient(0.00): ")
                
                genre_patient = (input("genre du patient(M/F): ")).upper()
                
                age_patient = input("l'age du patient: ")
                
                numero_dossier = generer_un_code(dossiers)
                nouveau_patient = (enregistrer_un_patient(
                                                        nom_patient, postnom_patient,
                                                        prenom_patient, telephone_patient,
                                                        poid_patient, taille_patient,
                                                        genre_patient, age_patient, numero_dossier))
                vft = 0
                if liste_patients:
                    for i in range(len(liste_patients)):
                        if nouveau_patient[:8] == liste_patients[i][:8]:
                            print("ce patient existe! ")
                            vft += 1
                if vft == 0:
                    liste_patients.append(nouveau_patient)

            case 3:
                
                if not liste_vide(liste_patients, liste_docteurs):
                    nom = (input("Entrez le nom du patient cherché: ")).upper()
                    vft = 0 
                    for patient in liste_patients:
                        if (nom in patient[0] 
                            or nom in patient[1] 
                            or nom in patient[2]):

                            print(f"\
                                    Nom           : {patient[0]} \n \
                                    Post-nom      : {patient[1]} \n \
                                    Prenom        : {patient[2]} \n \
                                    Telephone     : {patient[3]} \n \
                                    Poid          : {patient[4]} kg \n \
                                    Taille        : {patient[5]} cm \n \
                                    Genre         : {patient[6]} \n \
                                    Age           : {patient[7]} ans \n \
                                    Numero Dossier: {patient[8]}  \n")

                            vft+= 1
                    if vft == 0: print(f"{nom} non repertorié! ")            

            case 4: 
                if not liste_vide(liste_patients, liste_docteurs):
                    numero = input("Entrez le numero de dossier du malade: ")
                    for patient in liste_patients:
                        if numero == patient[-1]:
                            print(f"\
                                        Nom           : {patient[0]} \n \
                                        Post-nom      : {patient[1]} \n \
                                        Prenom        : {patient[2]} \n \
                                        Telephone     : {patient[3]} \n \
                                        Poid          : {patient[4]} kg \n \
                                        Taille        : {patient[5]} m \n \
                                        Genre         : {patient[6]} \n \
                                        Age           : {patient[7]} ans \n \
                                        Numero Dossier: {patient[8]}  \n \
                                    ")

            case 5:     #marie michelle
                if not liste_vide(liste_patients, liste_docteurs):
                    for patient in liste_patients:
                        if len(patient) == 9:
                            print(f"\
                            Nom           : {patient[0]} \n \
                        Post-nom      : {patient[1]} \n \
                        Prenom        : {patient[2]} \n \
                        Telephone     : {patient[3]} \n \
                        Poid          : {patient[4]} kg \n \
                        Taille        : {patient[5]} m \n \
                        Genre         : {patient[6]} \n \
                        Age           : {patient[7]} ans \n \
                        Numero Dossier: {patient[8]}  \n \
                        ____________________________ \
                    ")
                        else:
                            print(f"\
                                        Nom           : {patient[0]} \n \
                                        Post-nom      : {patient[1]} \n \
                                        Prenom        : {patient[2]} \n \
                                        Telephone     : {patient[3]} \n \
                                        Poid          : {patient[4]} kg \n \
                                        Taille        : {patient[5]} m \n \
                                        Genre         : {patient[6]} \n \
                                        Age           : {patient[7]} ans \n \
                                        Plaintes      : {patient[8]} \n \
                                        Numero Dossier: {patient[9]}  \n \
                                        ____________________________ \
                                    ")

            case 6:        
                if not liste_vide(liste_patients, liste_docteurs):
                    for docteur in liste_docteurs:
                        print(f"\
                        Nom            : {docteur[0]} \n \
                    Post-nom       : {docteur[1]} \n \
                    Prenom         : {docteur[2]} \n \
                    Telephone      : {docteur[3]} \n \
                    Matricule      : {docteur[4]} \n \
                    Specialisation : {docteur[5]} \n \
                    ____________________________ \
                ")

            case 7:      
                if not liste_vide(liste_patients, liste_docteurs):
                    vft = 0
                    nom_patient = (input("nom du patient: ")).upper()

                    for patient in liste_patients:
                        if nom_patient in patient:
                            plainte = (input(f"Entrez la plainte de {patient[0]} {patient[1]} {patient[2]}: ")).lower()
                            enregistrer_plaintes(plainte, patient)
                            vft += 1

                    if vft == 0:
                       raise

            case 8:     
                if not liste_vide(liste_patients, liste_docteurs):
                    numero_dossier = input("numero de dossier du patient: ")
                    for patient in liste_patients:
                        if (numero_dossier == patient[-1] and
                            len(patient) == 10):

                            for plainte in patient[8]:
                                print(f"{patient[0]} {patient[1]} {patient[2]} souffre de {plainte}")

                        elif numero_dossier == patient[-1]:
                            print(f"{patient[0]} {patient[1]} {patient[2]} n'a pas de plainte")

            case 9:     

                if not liste_vide(liste_patients, liste_docteurs):
                    numero_dossier = input("numero de dossier: ")
                    vft = 0         
                    
                    for patient in liste_patients:
                        if numero_dossier == patient[-1]:
                            try:
                                poid_patient = float(patient[4])
                                taille = float(patient[5])
                            except TypeError:
                                print("La taille ou le poid, n'est pas bien inscrit!")
                                continue

                            taille = taille ** 2
                            imc = poid_patient / taille

                            if imc < 18.5:
                                print("Insuffisance normale")
                            elif (imc >= 18.5) and (imc <= 25):
                                print("Corpulence normale")
                            elif (imc > 25) and (imc <=30):
                                print("Surpoids")
                            elif (imc > 30) and (imc <= 35):
                                print("Obéisité modéréé ")
                            elif (imc > 35) and (imc <= 40):
                                print("Obésité sévère")
                            else:
                                print("Obésité ,orbite ou massive")

                        vft += 1

                    if vft == 0:
                       raise

            case 10:
                if not liste_vide(liste_patients, liste_docteurs):
                    jours = ["lundi", "Mardi", 
                            "Mercredi", "Jeudi",
                            "Vendredi", "Samedi",
                            "Dimanche"]

                    for docteur in liste_docteurs:
                        horaire = [] 
                        print(f"\t Enregistrement pour le Dr {docteur[0]}!")

                        for jour in jours:
                            answers = input(f"Etes-vous occupé le {jour}?: ")
                            if answers.lower() == "oui": horaire.append(jour)
                                
                        docteur.append(horaire)

            case 11:
                if not liste_vide(liste_patients, liste_docteurs):   
                    nom_docteur = (input("nom du medecin: ")).upper()
                    for docteur in liste_docteurs:
                        if (nom_docteur == docteur[0]
                            or nom_docteur == docteur[1]
                            or nom_docteur == docteur[2]):

                                if len(docteur) < 7:
                                    print("pas d'horaire  !")

                                else:
                                    if len(docteur[-1] < 7):
                                        print("jour non disponible ")

                                        for jour in docteur[-1]:
                                            print(f"{jour}", end=" ")

                                        rdv = input("\n prenez rendez-vous un des jours non mentionné: ")
                                        if rdv in docteur[-1]:
                                            print("occupé")

                                        elif rdv not in ["lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]:
                                            print(f"{rdv} n'est pas un jour de la semaine!")

                                        else:    
                                            docteur[-1].append(rdv)

                                    else:
                                        print(f"{docteur[0]} n'est pas disponible cette semaine!")
                        else:
                            print(f"{nomocteur} n'appartient pas de cet hopital!")

            case 12:
               raise
        
main()


