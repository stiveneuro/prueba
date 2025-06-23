from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from mysapp.models import *
import json
import random

# Create your views here.

def saludo(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

c=0
def ingresar(request):
    if request.method=="POST":
        try:
            data = json.loads(request.body)
            email = data.get("correo")
            contrasena=data.get("contraseña")

            user=authenticate(request, username=f"{email}o{contrasena}", password=contrasena)
            print(user)
        
            global c
            c+=0
            print(f"comida{c}")
            if user is not None:
                print("amigo")
                login(request, user)
                return JsonResponse({"success":True, "message":"Bienvenido"})
            else:
                return JsonResponse({"success":False, "message": "credenciales incorrectas"})
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Error en el formato JSON"}, status=400)
    return JsonResponse({"error": "Método no permitido"},status=400)

def cerrar(request):
    logout(request)
    return redirect("login")

def registra(request):
    #crear usuario en base de datos
    if request.method=="POST":

        data=json.loads(request.body)
        correos=data.get("correo")
        contrasenas=data.get("contraseña")
        print("amigo")

        user=User.objects.create_user(username=f"{correos}o{contrasenas}",email=correos,password=contrasenas)
        user.save()
        print("estamo aqui")
        capitulos=capitulo.objects.all()
        progreso=colorProgreso.objects.get(progreso=0)
        for cap in capitulos:
            pro_cap=ProgresoCapitulo.objects.create(id_capitulo=cap, id_usuario=user, progreso=progreso )
            pro_cap.save()
            print("pase for falta uno")
            modulos=modulo.objects.filter(id_capitulo=cap.id)         
            for mod in modulos:
                resu_cap =resulatadoPrueba.objects.create(id_usuario=user, id_modulo=mod, resultado=0)
                resu_cap.save()
        print("amix")
        #loguearlo
        ingresar(request)
    return JsonResponse({"resp":"listo"})

@login_required
def veri(request):
    print("comida")
    if request.method=="GET":
        data={"res":"True"}
    return JsonResponse(data)