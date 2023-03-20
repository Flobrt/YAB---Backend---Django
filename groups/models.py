from django.db import models


# Create your models here.
class Brief(models.Model):
    titre_brief = models.CharField(max_length = 35)
    url_brief = models.URLField(max_length = 100)
    nb_appr_par_nome = models.IntegerField(default = 2)

    def __str__(self):
        return self.titre_brief 
        
class Apprenant(models.Model):
    nom_apprenant = models.CharField(max_length = 30)
    prenom_apprenant = models.CharField(max_length = 30)
            
    def __str__(self):
        return self.nom_apprenant + ' ' + self.prenom_apprenant

class Nome(models.Model):
    id_brief = models.ForeignKey('Brief', on_delete=models.CASCADE)
    nome_nom = models.CharField(max_length = 100)
    apprenants = models.ManyToManyField('Apprenant')

    def __str__(self):
        return str(self.id_brief) + ' ' + self.nome_nom 

