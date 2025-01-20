from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Consorcio

def verificar_consorcio(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        consorcio_id = kwargs.get('pk')  # Obtén el ID del consorcio desde la URL
        consorcio = get_object_or_404(Consorcio, pk=consorcio_id)
        if request.user.consorcio != consorcio:
            return HttpResponseForbidden("No tienes permiso para acceder a este consorcio.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
