from django.urls import path

from . import views 

app_name = "tienda"
urlpatterns = [
    path("", views.index , name ="index"),
    path("about/", views.about , name ="about"),
    path("consorcio/list/", views.consorcio_list  , name ="consorcio_list"),
    path("consorcio/create/", views.consorcio_create  , name ="consorcio_create"),
    path("consorcio/update/<int:pk>/", views.consorcio_update, name ="consorcio_update"),
    path("consorcio/detail/<int:pk>/", views.consorcio_detail, name ="consorcio_detail"),
    path("consorcio/delete/<int:pk>/", views.consorcio_delete, name ="consorcio_confirm_delete"),
    path("liquidacion/list/", views.Liquidacion_list , name ="liquidacion_list"),
    path("liquidacion/create/", views.Liquidacion_create , name ="liquidacion_create"),
    path("unidades/list/", views.Unidades_list , name ="unidades_list"),
    path("unidades/create/", views.Unidades_create , name ="unidades_create"),
    
]