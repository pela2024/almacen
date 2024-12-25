from django.urls import path

from .views import index, about, consorcio_list, Unidades_list, Liquidacion_list, consorcio_create, Unidades_create, Liquidacion_create,consorcio_update 


app_name = "tienda"
urlpatterns = [
    path("", index , name ="index"),
    path("about/", about , name ="about"),
    path("consorcio/list/", consorcio_list  , name ="consorcio_list"),
    path("consorcio/create/",consorcio_create  , name ="consorcio_create"),
    path("consorcio/update/<int:pk>/",consorcio_update, name ="consorcio_update"),
    path("liquidacion/list/", Liquidacion_list , name ="liquidacion_list"),
    path("liquidacion/create/",Liquidacion_create , name ="liquidacion_create"),
    path("unidades/list/", Unidades_list , name ="unidades_list"),
    path("unidades/create/",Unidades_create , name ="unidades_create"),
    
]