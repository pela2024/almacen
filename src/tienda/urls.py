from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import admin_dashboard_view, propietario_dashboard_view
from tienda.views_models import consorcio, liquidacion
from . import views 
from django.http import HttpResponse
from .views_models.propietario import (
    LiquidacionesPropietarioListView, 
    LiquidacionPropietarioDetailView,
    PropietarioRegistroView,
    PropietarioIndexView,
    AboutPropietarioView,
)

app_name = "tienda"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='tienda:login'), name='logout'),
    path('register/', views.RegistrarseView.as_view(), name='register'),
    path('profile/', views.UpdateProfileView.as_view(), name='profile'),
    path('admin-dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('propietario-dashboard/', propietario_dashboard_view, name='propietario_index'),
    
    # URLs de Consorcio
    path("consorcio/list/", consorcio.consorcio_list, name="consorcio_list"),
    path("consorcio/create/", consorcio.consorcio_create, name="consorcio_create"),
    path("consorcio/update/<int:pk>/", consorcio.consorcio_update, name="consorcio_update"),
    path("consorcio/detail/<int:pk>/", consorcio.consorcio_detail, name="consorcio_detail"),
    path("consorcio/delete/<int:pk>/", consorcio.consorcio_delete, name="consorcio_confirm_delete"),
    path("consorcio/<int:pk>/gastos/", views.listar_gastos, name="listar_gastos"),
    path("consorcio/<int:pk>/gastos/nuevo/", views.crear_gasto, name="crear_gasto"),
    path("consorcio/<int:pk>/datos/pdf/", views.descargar_pdf, name="descargar_pdf"),
    
    # URLs de Liquidación
    path("liquidacion/list/", liquidacion.LiquidacionListView.as_view(), name="liquidacion_list"),
    path("liquidacion/create/", liquidacion.LiquidacionCreateView.as_view(), name="liquidacion_create"),
    path("liquidacion/update/<int:pk>", liquidacion.LiquidacionUpdateView.as_view(), name="liquidacion_update"),
    path("liquidacion/detail/<int:pk>", liquidacion.LiquidacionDetailView.as_view(), name="liquidacion_detail"),
    
    # URLs de Unidades
    path("unidades/list/", views.Unidades_list, name="unidades_list"),
    path("unidades/create/", views.Unidades_create, name="unidades_create"),
    
    # URLs de Propietario
    path('propietario/', PropietarioIndexView.as_view(), name='propietario_index'),
    path('propietario/about/', AboutPropietarioView.as_view(), name='About_propietario'),
    path('propietario/logout/', LogoutView.as_view(), name='propietario_logout'),
    path('propietario/registro/', PropietarioRegistroView.as_view(), name='propietario_registro'),
    path('propietario/liquidaciones/', LiquidacionesPropietarioListView.as_view(), name='liquidaciones_propietario'),
    path('propietario/liquidacion/<int:pk>/', LiquidacionPropietarioDetailView.as_view(), name='liquidacion_propietario_detail'),
    
    # URLs de Proveedores
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]
