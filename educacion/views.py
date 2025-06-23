import markdown as md
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from mysapp.models import *      
from django.db.models import F      
import json
from django.conf import settings
import os


def silabo(request): 
    ruta_cp =os.path.join(settings.BASE_DIR,"educacion","templates","cap1.md")
    with open(ruta_cp, "r", encoding="utf-8") as cap:
        capitulo=cap.read()
    md_capitulo=md.markdown(capitulo)
    return render(request,"silabo.html", {"capitulo1": md_capitulo} )

@login_required
def cap_prog_color(request):
    users=request.user.id 
    print("amix")
    progreso_usuario=ProgresoCapitulo.objects.filter(id_usuario=users).select_related("progreso","id_capitulo").order_by("id_capitulo__orden").values_list("id_capitulo","progreso","progreso__color")
    return list(progreso_usuario)

def respuesta(request):
    if request.method=="GET":
        lista_capitulo=cap_prog_color(request) if isinstance(cap_prog_color(request), list) else list(capitulo.objects.values_list("id").order_by("orden"))
        return JsonResponse({"lis_cap":lista_capitulo })

def cap_con(request):
    if request.method=="POST":
        data=json.loads(request.body)
        id_capi=data.get("id_cap")
        print(id_capi, data)    
        idModulo=list(modulo.objects.filter(id_capitulo=id_capi).values_list("id").order_by("orden"))
        ruta=capitulo.objects.get(id=id_capi).ruta_contenido
        print(ruta,"hola")
        ruta=rf"{ruta}"
        ruta2=ruta.replace("/",os.sep)
        ruta =os.path.join(settings.BASE_DIR,ruta2)
        with open(ruta, "r", encoding="utf-8") as con:
            contenido=md.markdown(con.read())
        return JsonResponse({"con_cap" : contenido, "id_mod" : idModulo  })
    return JsonResponse({"error": "Método no permitido"}, status=405)

def modulo_contenido(request):
    if request.method=="POST":
        data=json.loads(request.body).get("id_mod")
        print(data)
        ruta_md=modulo.objects.get(id=data).ruta_modulo
        ruta=rf"{ruta_md}"
        ruta2=ruta.replace("/",os.sep)
        ruta =os.path.join(settings.BASE_DIR,ruta2)
        print(ruta,"hola2")
        with open(ruta,"r",encoding="utf-8") as mod:
            conte_mod=mod.read()
        md_modulo=md.markdown(conte_mod)
        print("llegue", type(md_modulo))
        return JsonResponse({"modulo": md_modulo })
    return JsonResponse({"error": "Método no permitido"}, status=405)


