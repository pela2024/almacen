from django.urls import path

from .views import index, about, curso_list, alumno_list, comision_list, curso_create, Alumno_create, Comision_create 


app_name = "tienda"
urlpatterns = [
    path("", index , name ="index"),
    path("about/", about , name ="about"),
    path("curso/list/",curso_list  , name ="curso_list"),
    path("curso/create/",curso_create  , name ="curso_create"),
    path("comision/list/",comision_list , name ="comision_list"),
    path("comision/create/",Comision_create , name ="comision_create"),
    path("alumno/list/", alumno_list , name ="alumno_list"),
    path("alumno/create/", Alumno_create , name ="alumno_create"),
    
]