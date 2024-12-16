from django.urls import path

from .views import index, about, consorcio_list, alumno_list, comision_list, consorcio_create, Alumno_create, Comision_create 


app_name = "tienda"
urlpatterns = [
    path("", index , name ="index"),
    path("about/", about , name ="about"),
    path("consorcio/list/",consorcio_list  , name ="consorcio_list"),
    path("consorcio/create/",consorcio_create  , name ="consorcio_create"),
    path("comision/list/",comision_list , name ="comision_list"),
    path("comision/create/",Comision_create , name ="comision_create"),
    path("alumno/list/", alumno_list , name ="alumno_list"),
    path("alumno/create/", Alumno_create , name ="alumno_create"),
    
]