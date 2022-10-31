from django.shortcuts import render
from report.models import Report_data
# Create your views here.
def ClassementReport(request):
    #je récupère mes données je les mets dans une variable que je vais ensuite passer à ma vue
    mes_data = Report_data.objects.all()
    return render(request, 'classementReport.html',{'mes_data':mes_data})
def ClassementNormal(request):
    return render(request, 'classementNormal.html')