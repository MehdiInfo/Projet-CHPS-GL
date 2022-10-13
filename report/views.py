from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Report_data
from .forms import ReportForm
# Create your views here.


def homeReportView(request):
    #return HttpResponse("HELLO WORLD")
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Classement')
    context = {'form':form}
    return render(request, 'index.html',context)