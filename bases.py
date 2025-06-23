#creado en el shell

"""from django.contrib.auth.models import User
"""

from mysapp.models import modulo

"""user=User.objects.get(username="general")
user.set_password("contrasena")
user.save()
"""

modulo=modulo.objects.create(id_capitulo_id=1, orden=2, ruta_modulo="educacion/templates/mod2")
