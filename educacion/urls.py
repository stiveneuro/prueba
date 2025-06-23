from django.urls import path
from . import views

urlpatterns=[
    path("", views.silabo),
    path("capitulos/", views.respuesta),
    path("capcon/",views.cap_con),
    path("modulos/", views.modulo_contenido),
]