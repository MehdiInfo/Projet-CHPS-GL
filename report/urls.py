from django.urls import path
from .views import homeReportView

urlpatterns = [
    path("",homeReportView,name= "index"),
]
