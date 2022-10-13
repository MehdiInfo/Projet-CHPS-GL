from django.db import models

# Create your models here.

class Report_data(models.Model):
    id_bt = models.IntegerField()
    pseudo_bt = models.CharField(max_length = 50)
    id_game = models.IntegerField()
    bug_type = models.CharField(max_length = 50)
