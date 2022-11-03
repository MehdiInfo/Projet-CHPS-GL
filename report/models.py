from django.db import models

# Create your models here.

class Report_data(models.Model):
    id_bt = models.ForeignKey(BetaTester)
    id_bug = models.ForeignKey(Bug)
    id_game = models.ForeignKey(Application)

class BetaTester(models.Model):
    nom = models.CharField(max_length = 30)
    prenom = models.CharField(max_length = 30)
    score = models.IntegerField()
    score_bug = models.IntegerField()

class Application(models.Model):
    nom_app = models.CharField(max_length=30)

class Bug(models.Model):
    bug_type = models.CharField(max_length = 50)


# pour la classement visible que par les béta testeur
# rajout d'une table béta testeur
# rajout d'une table game