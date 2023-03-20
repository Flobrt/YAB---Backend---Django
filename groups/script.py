import mysql.connector
import random
import string


mydb = mysql.connector.connect(
  host="localhost",
  user="florian",
  password="florian038",
  database="namesDB",
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE apprenantgroupe")
mycursor.execute("DROP TABLE groupe")
mycursor.execute("CREATE TABLE IF NOT EXISTS groupe (id_groupe INT AUTO_INCREMENT PRIMARY KEY, nom_groupe VARCHAR(80) not null, id_brief int, CONSTRAINT id_brief FOREIGN KEY (id_brief) REFERENCES brief (id_brief) ON DELETE CASCADE)")
mycursor.execute("CREATE TABLE IF NOT EXISTS apprenantgroupe (id_apprenant INT, id_groupe INT , PRIMARY KEY (id_apprenant, id_groupe), FOREIGN KEY (id_apprenant) REFERENCES apprenant (id_apprenant), FOREIGN KEY (id_groupe) REFERENCES groupe (id_groupe))")

mydb.commit()



mycursor = mydb.cursor()

mycursor.execute("SELECT id_brief, nom_brief, n_omes FROM brief")
brief_list = mycursor.fetchall()

mycursor.execute("SELECT prenom, nom FROM apprenant")

groups_list = mycursor.fetchall()

### fonction qui génère les n-binômes pour une liste d'élèves et n en paramètres.
def creategroupe(groups_lis, nbr_by_groupe):
    newlist = []
    for i in range(1, len(groups_lis)//nbr_by_groupe):
        binome = random.sample(groups_lis, nbr_by_groupe)
        for j in binome:
            groups_lis.remove(j)
        newlist.append(binome) 
    newlist.append(groups_lis)
    return newlist 
#creategroupe(groups_list, 4)

### fonction qui génère une chaîne aléatoire pour générés des noms de groupe
def namealeatoire():
    """Générer une chaîne aléatoire de longueur fixée ici à 10"""
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(10))
    
print ("La chaine aleatoire est :", namealeatoire() )



######### insertion table groupe et apprenant_groupe   
for brief in brief_list:
     brief_id = brief[0]
     brief_name = brief[1]
     brief_nb = brief[2] 
     mycursor.execute("SELECT prenom, nom FROM apprenant")
     groups_list = mycursor.fetchall()
     newlist = []
     
     for i in range(1, len(groups_list)//brief[2]):
         binome = random.sample(groups_list, brief[2] )
         for j in binome:
             groups_list.remove(j)
         newlist.append(binome) 
     newlist.append(groups_list)
    
     print(f"  Pour le brief {brief_id},   les groupes sont les suivants: {newlist} ")


#### parcours les briefs pour créer les groupes selon les nomes
for brief in brief_list:
     brief_id = brief[0]
     brief_name = brief[1]
     brief_nb = brief[2] 
     mycursor.execute("SELECT id_apprenant, prenom, nom FROM apprenant")
     groups_list = mycursor.fetchall()
     newlist = []
     newlist = creategroupe(groups_list, brief[2])
     
   
     #### itération sur chaque élément de liste pour chaque brief
     for groupe in newlist:
        print(groupe)
        print(f"  Pour le brief {brief_id},   les groupes sont les suivants: {groupe} ")

        name_groupe = namealeatoire()
        print(name_groupe)

       
    ######Insertion des noms de groupe dans groupe avec l'id brief associé        

        sql_groupe = "INSERT INTO groupe (nom_groupe, id_brief) VALUES (%s, %s)"
        val_groupe = [
        (name_groupe,brief[0]),
        ]
        mycursor.executemany(sql_groupe, val_groupe)
        mydb.commit()

        ###récupération id groupe
        sl3 = "SELECT id_groupe FROM groupe WHERE nom_groupe = %s"
        sl33 = (name_groupe,)                                         ####pourquoi virgule ok, surtout enlever à l'affichage
        mycursor.execute(sl3, sl33)
        idgroup = mycursor.fetchall()
        for idg in idgroup:
             print(idg)
             #print(f"donc pour le groupe {name_groupe}, {id}, {name}")

        ###Insertion des valeurs, table associative id apprenant id groupe
        for name in groupe:
            print(f"{name[0]} fait parti du groupe {idg[0]}")
            sl2 = "INSERT INTO apprenantgroupe (id_apprenant, id_groupe) VALUES (%s, %s)"
            valsl2 = [
                (name[0],idg[0]),
                 ]
            mycursor.executemany(sl2, valsl2)
            mydb.commit()

