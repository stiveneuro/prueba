from django.urls import path
from . import views

urlpatterns=[
    path("", views.saludo, name="login"),
    path("test", views.test),
    path("procesar/", views.ingresar), 
    path("cerrar/",views.cerrar),
    path("registra/",views.registra),
    path("verifica/",views.veri)
]

