from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Report_data
from .forms import ReportForm

# Create your views here.


def homeReportView(request):
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {'form':form}
    return render(request, 'index.html',context)

def ClassementView(request):
        return render(request, 'classement.html')