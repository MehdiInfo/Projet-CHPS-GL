from django.shortcuts import render
from report.models import Report_data,BetaTester
# Create your views here.
def ClassementReport(request):
    #je récupère mes données je les mets dans une variable que je vais ensuite passer à ma vue
    mes_data = BetaTester.objects.all().order_by('-score_bug')
    return render(request, 'classementReport.html',{'mes_data':mes_data})
def ClassementNormal(request):
    mes_data = BetaTester.objects.all().order_by('-score')
    return render(request, 'classementNormal.html',{'mes_data':mes_data})