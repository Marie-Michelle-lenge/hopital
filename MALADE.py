import random

def enregistrer_un_patient(nom_patient, postnom_patient, prenom_patient,
                            telephone_patient, poid_patient, taille_patient,
                            genre_patient, age_patient, numero_dossier):

#Enregistrement d'un patient

    patient = [nom_patient, postnom_patient, prenom_patient, telephone_patient, poid_patient,
               taille_patient, genre_patient, age_patient, numero_dossier]
    return patient


def generer_un_code(dossier):

#Generer un code dossier du patient 

    chiffres = "0123456789"
    num = random.sample(chiffres,8)
    num = "".join(num)
    while num in dossier:
        chiffres = "0123456789"
        num= random.sample(chiffres,8)
        num = "".join(num)
    return num
#MARIE MICHELLE

def enregistrer_plaintes(plainte, patient):
    plaintes = ""
    if len(plainte) > 1:
        if len(patient) == 9:
            plaintes += plainte
            patient.insert(8, plaintes)
        else:
            patient[8] += ", "+plainte



