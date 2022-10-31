from django.urls import path
from .views import *

urlpatterns = [
    path("",ClassementReport,name= "clas_Report"),
    path("_normal/",ClassementNormal,name = "clas_Normal")
]
