from django.db import models
import uuid

# Create your models here.
class Etudiant(models.Model):
    nom=models.CharField(max_length=60)
    prenom=models.CharField(max_length=60)
    niveau=models.CharField(max_length=60)
    option=models.CharField(max_length=60)
    adresse=models.CharField(max_length=60)
    tel=models.CharField(max_length=60)
    matricule=models.CharField(max_length=60)
    #courssuivi=models.CharField(max_length=60)
    date_naiss=models.DateField()
    #image=models.ImageField(upload_to='images/')
    secrete_key=models.UUIDField(default=uuid.uuid4)

    def __str__(self):

        return self.nom


class Cours(models.Model):
    code=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    prof=models.CharField(max_length=50)
    nbcredit=models.IntegerField()
    #image=models.ImageField(upload_to='images/')
    secrete_key=models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        
        return self.code