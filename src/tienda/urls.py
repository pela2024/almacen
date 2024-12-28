from django.urls import path

from tienda.views_models import consorcio, liquidacion  
from . import views 

app_name = "tienda"
urlpatterns = [
    path("", views.index , name ="index"),
    path("about/", views.about , name ="about"),
    path("login/", views.CustomLoginView.as_view(), name = "login"),
]

urlpatterns += [
    path("consorcio/list/", consorcio.consorcio_list  , name ="consorcio_list"),
    path("consorcio/create/", consorcio.consorcio_create  , name ="consorcio_create"),
    path("consorcio/update/<int:pk>/", consorcio.consorcio_update, name ="consorcio_update"),
    path("consorcio/detail/<int:pk>/", consorcio.consorcio_detail, name ="consorcio_detail"),
    path("consorcio/delete/<int:pk>/", consorcio.consorcio_delete, name ="consorcio_confirm_delete"),
]
urlpatterns += [    
    path("liquidacion/list/", liquidacion.LiquidacionListView.as_view(), name ="liquidacion_list"),
    path("liquidacion/create/", liquidacion.LiquidacionCreateView.as_view(), name ="liquidacion_create"),
    path("liquidacion/update/<int:pk>", liquidacion.LiquidacionUpdateView.as_view(), name ="liquidacion_update"),
    path("liquidacion/detail/<int:pk>", liquidacion.LiquidacionDetailView.as_view(), name ="liquidacion_detail"),
]

urlpatterns += [
    path("unidades/list/", views.Unidades_list , name ="unidades_list"),
    path("unidades/create/", views.Unidades_create , name ="unidades_create"),
]