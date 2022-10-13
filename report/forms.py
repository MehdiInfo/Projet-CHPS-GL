from django.forms import ModelForm
from .models import Report_data

class ReportForm(ModelForm):
    class Meta:
        model = Report_data
        fields = '__all__'