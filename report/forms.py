from django.forms import ModelForm
from .models import  BetaTester, Application

class BTform(ModelForm):
    class Meta:
        model = BetaTester
        fields = {'nom','prenom'}
class Appform(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        
