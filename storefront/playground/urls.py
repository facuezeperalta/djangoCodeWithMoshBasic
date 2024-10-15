from django.urls import path
from . import views

#URL confg module.
urlpatterns = [
    path('hello/',views.say_hello) #paso una referencia a la función que esta en views no la ejecuto. las rutas siempre terminan con /
    
]
