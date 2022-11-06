from django.db import models

# Create your models here.

class BetaTester(models.Model):
    nom = models.CharField(max_length = 30)
    prenom = models.CharField(max_length = 30)
    score = models.IntegerField()
    score_bug = models.IntegerField()

class Application(models.Model):
    nom_app = models.CharField(max_length=30)

class Bug(models.Model):
    bug_type = models.CharField(max_length = 50)
    
class Report_data(models.Model):
    id_bt = models.ForeignKey('BetaTester',on_delete=models.DO_NOTHING)
    id_bug = models.ForeignKey('Bug',on_delete=models.DO_NOTHING)
    id_game = models.ForeignKey('Application',on_delete=models.DO_NOTHING)