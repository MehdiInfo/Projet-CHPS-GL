from django.urls import path
from .views import *

urlpatterns = [
    path("",homeReportView,name= "index"),
    path("classement/",ClassementView, name="classement")
]
