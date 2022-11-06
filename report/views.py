from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BetaTester, Application, Report_data, Bug
from .forms import Appform, BTform
from django.contrib import messages

# Create your views here.


def homeReportView(request):
    # à faire gestion des report à pls reprises ?
    # gestion des majuscules et miniscules ?
    if request.method == 'POST':
        rname = request.POST.get('nom')
        rprenom = request.POST.get('prenom')
        rnom_app = request.POST.get('nom_app')
        try:
            b = BetaTester.objects.get(nom = rname,prenom = rprenom)
            b.score_bug = b.score_bug + 10
        except BetaTester.DoesNotExist:
            b = BetaTester(nom = rname,
                        prenom = rprenom,
                        score = 0,
                        score_bug = 10)
        try:
            a = Application.objects.get(nom_app = rnom_app)
        except Application.DoesNotExist: 
            a = Application(nom_app = rnom_app)
        new_bug = Bug(bug_type = "True Bug")
        a.save()
        b.save()
        new_bug.save()
        new_report = Report_data(id_bug= new_bug ,id_bt= b, id_game= a)
        
        
        new_report.save()
        return redirect("index")
    else:
        Bform = BTform()
        AForm = Appform()
        return render(request, 'index.html',{'App_form' : AForm, 'BetaTester_form' : Bform})

def ClassementView(request):
        mes_data = BetaTester.objects.all().order_by('-score')
        return render(request, 'classement.html',{'mes_data':mes_data})