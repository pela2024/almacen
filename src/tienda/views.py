from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required  # type = ignore
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView 
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404
from .models import Proveedor, Consorcio, Gastos, Unidades, Administracion 
from .forms import ProveedorForm, GastosForm, CustomAuthenticationForm , CustomRegistroUsuarioForm, UserProfileForm, UnidadesForm
from django.template.loader import render_to_string
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Create your views here.
@login_not_required 
def index(request):
    return render(request, "tienda/index.html")

@login_not_required
def about(request):
    return render(request, "tienda/about.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "tienda/login.html"

    def get_success_url(self):
        # Redirige según el tipo de usuario
        if self.request.user.is_superuser:  # Administrador
            return reverse_lazy('admin:index')  # Cambia según tu URL de admin
        elif hasattr(self.request.user, 'propietario'):  # Usuario Propietario
            return reverse_lazy('tienda:propietario_index')  # Cambia según tu URL de propietario
        else:  # Usuario estándar
            return reverse_lazy('tienda:index')  # URL de usuario general

    def form_valid(self, form):
        # Mensaje de éxito al iniciar sesión
        messages.success(
            self.request, f"Inicio de sesión exitoso. ¡Bienvenido {self.request.user.username}!"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        # Mensaje de error si fallan las credenciales
        messages.error(self.request, "Usuario o contraseña incorrectos.")
        return super().form_invalid(form)

@method_decorator(login_not_required, name = "dispatch")
class RegistrarseView(CreateView):
    form_class = CustomRegistroUsuarioForm  # Usa el formulario personalizado
    template_name = 'tienda/register.html'  # Nombre del template
    success_url = reverse_lazy('tienda:login')  # Redirige al login tras el registro

    def form_valid(self, form:BaseModelForm) -> HttpResponse:
        messages.success(self.request, "Registro exitoso. Ahora puedes iniciar sesion ")
        return super().form_valid(form) 

class UpdateProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'tienda/profile.html'  # Nombre del template
    success_url = reverse_lazy('tienda:index') 

    def get_object (self):

        return self.request.user


def Unidades_list(request):
    query = Unidades.objects.all()
    context = {"object_list": query}
    return render(request, "tienda/unidades_list.html", context)

def Unidades_create(request):
    if request.method == "GET":
        form = UnidadesForm()
    elif request.method == "POST":
        form = UnidadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:unidades_list")
    return render(request, "tienda/unidades_form.html", {"form": form})     

@login_required
def admin_dashboard_view(request):
    return render(request, "tienda/admin_dashboard.html")

@login_required
def propietario_dashboard_view(request):
    return render(request, "tienda/propietario_dashboard.html")

def liquidacion_expensas(request, periodo, consorcio_id):
    # Obtener el consorcio y la administración
    consorcio = Consorcio.objects.get(pk=consorcio_id)
    administracion = Administracion.objects.first()  # O ajusta para obtener la administración correspondiente
    
    # Filtrar los gastos del consorcio
    gastos = Gastos.objects.filter(consorcio=consorcio)
    
    return render(request, 'tienda/liquidacion_expensas.html', {
        'periodo': periodo,
        'administracion': administracion,
        'consorcio': consorcio,
        'gastos': gastos,
    })

def lista_proveedores(request):
    try:
        proveedores = Proveedor.objects.all()
        print("Proveedores encontrados:", proveedores.count())
        for p in proveedores:
            print(f"Proveedor: {p.razon_social}")
        return render(request, 'tienda/proveedores/lista_proveedores.html', {'proveedores': proveedores})
    except Exception as e:
        print("Error en lista_proveedores:", str(e))
        return render(request, 'tienda/proveedores/lista_proveedores.html', {'error': str(e)})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor creado exitosamente.")
            return redirect('tienda:lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'tienda/proveedores/crear_proveedor.html', {'form': form})

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
    return render(request, 'tienda/proveedores/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, "Proveedor eliminado exitosamente.")
        return redirect('tienda:lista_proveedores')
    return render(request, 'tienda/proveedores/eliminar_proveedor.html', {'proveedor': proveedor})




def listar_gastos(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    gastos = Gastos.objects.filter(consorcio=consorcio)
    return render(request, 'tienda/datos/listar_gastos.html', {
        'gastos': gastos,
        'consorcio': consorcio
    })


def crear_gasto(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    if request.method == 'POST':
        form = GastosForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.consorcio = consorcio
            gasto.save()
            return redirect('tienda:listar_gastos', pk=consorcio.pk)
    else:
        form = GastosForm()
    return render(request, 'tienda/datos/gastos_form.html', {
        'form': form,
        'consorcio': consorcio
    })


def descargar_pdf(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    gastos = Gastos.objects.filter(consorcio=consorcio).order_by('rubro')

    # Crear respuesta HTTP para el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="gastos_{consorcio.clave_del_consorcio}.pdf"'

    # Crear documento PDF
    pdf = SimpleDocTemplate(response, pagesize=letter)

    # Encabezado del documento
    titulo = f"Liquidacion - Consorcio {consorcio.domicilio}"
    elementos = []

    # Agregar título
    styles = getSampleStyleSheet()
    elementos.append(Paragraph(titulo, styles['Title']))
    elementos.append(Spacer(1, 20))  # Espacio debajo del título

    # Agrupar gastos por rubro
    rubros = {}
    for gasto in gastos:
        if gasto.rubro not in rubros:
            rubros[gasto.rubro] = []
        rubros[gasto.rubro].append(gasto)

    total_general = 0  # Para calcular el total de todos los rubros

    for rubro, lista_gastos in rubros.items():
        # Agregar un subtítulo con el nombre del rubro
        elementos.append(Paragraph(f"Rubro {rubro}", styles['Heading2']))

        # Crear datos de la tabla
        data = [
            [ 'Comprobante', 'Concepto', 'A', 'Importe'],  # Encabezado
        ]
        total_rubro = 0  # Total del rubro
        for gasto in lista_gastos:
            data.append([
                gasto.comprobante,
                gasto.concepto,
                gasto.a,
                f"${gasto.importe}",
            ])
            total_rubro += gasto.importe  # Sumar el importe al total del rubro

        # Agregar fila de total por rubro
        data.append(['', '', '', 'Total', f"${total_rubro}"])

        # Crear la tabla del rubro
        table = Table(data)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.greenyellow),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        table.setStyle(style)

        # Agregar la tabla y un espacio debajo
        elementos.append(table)
        elementos.append(Spacer(1, 20))

        # Sumar el total del rubro al total general
        total_general += total_rubro

    # Agregar total general al final
    elementos.append(Paragraph("Total General", styles['Heading2']))
    elementos.append(Paragraph(f"${total_general}", styles['Normal']))

    # Construir el PDF
    pdf.build(elementos)

    return response



def generar_pdf(request):
    # Configurar la respuesta HTTP como un archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="liquidacion.pdf"'

    # Crear un lienzo PDF
    c = canvas.Canvas(response, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Obtener datos de Administracion
    try:
        administracion = Administracion.objects.first()
        if not administracion:
            raise ValueError("No se encontraron datos de administración")

        # Título
        c.drawString(100, 750, "Liquidación de Expensas")
        
        # Datos de la administración
        c.drawString(50, 700, f"Administración: {administracion.razon_social}")
        c.drawString(50, 680, f"Dirección: {administracion.direccion}")
        c.drawString(50, 660, f"CUIT: {administracion.cuit}")
        c.drawString(50, 640, f"Teléfono: {administracion.telefono or 'N/A'}")
        c.drawString(50, 620, f"Email: {administracion.email or 'N/A'}")
        
        # Resto del código de generación de PDF permanece igual
        c.drawString(300, 700, "Consorcio:")
        c.drawString(300, 680, "Dirección: Calle Falsa 456")
        c.drawString(300, 660, "CUIT: 33-87654321-0")
        
        # Tabla de gastos
        c.drawString(50, 580, "Detalle de Gastos:")
        y = 560
        headers = ["Comprobante", "Concepto", "Importe"]
        for i, header in enumerate(headers):
            c.drawString(50 + (i * 150), y, header)  # Ajustar espaciado según necesidad
        y -= 20
        
        # Agregar datos reales (ejemplo de lista de gastos con proveedor incluido en concepto)
        gastos = [
            {"proveedor": "Proveedor 1", "comprobante": "001", "concepto": "Servicio", "importe": 1000.0},
            {"proveedor": "Proveedor 2", "comprobante": "002", "concepto": "Materiales", "importe": 500.0},
        ]
        for gasto in gastos:
            # Combinar concepto y proveedor
            concepto_con_proveedor = f"{gasto['concepto']} ({gasto['proveedor']})"
            
            # Dibujar los datos en la tabla
            c.drawString(50, y, gasto["comprobante"])
            c.drawString(200, y, concepto_con_proveedor)
            c.drawString(400, y, f"${gasto['importe']}")
            y -= 20

    except Exception as e:
        # Manejar cualquier error de recuperación de datos
        c.drawString(50, 700, f"Error: {str(e)}")

    # Finalizar PDF
    c.save()
    return response
