from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Proveedor
from .forms import ProveedorForm

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'tienda/lista_proveedores.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor creado exitosamente.")
            return redirect('tienda:lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'tienda/crear_proveedor.html', {'form': form})

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor actualizado exitosamente.")
            return redirect('tienda:lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'tienda/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, "Proveedor eliminado exitosamente.")
        return redirect('tienda:lista_proveedores')
    return render(request, 'tienda/eliminar_proveedor.html', {'proveedor': proveedor})
