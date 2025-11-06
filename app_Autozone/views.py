from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from django.urls import reverse
from django.utils import timezone

def inicio_autozone(request):
    # Página de inicio; puedes añadir más contexto si quieres
    return render(request, 'inicio.html')

def agregar_proveedor(request):
    if request.method == 'POST':
        # No validamos según tu instrucción
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        fecha_registro = request.POST.get('fecha_registro')  # formato YYYY-MM-DD
        dias_entrega = request.POST.get('dias_entrega')
        hora_entrega = request.POST.get('hora_entrega')

        Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_registro=fecha_registro,
            dias_entrega=dias_entrega,
            hora_entrega=hora_entrega
        )
        return redirect('ver_proveedores')

    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.fecha_registro = request.POST.get('fecha_registro')
        proveedor.dias_entrega = request.POST.get('dias_entrega')
        proveedor.hora_entrega = request.POST.get('hora_entrega')
        proveedor.save()
        return redirect('ver_proveedores')
    # si no es POST, redirige a la página de edición
    return redirect('actualizar_proveedor', proveedor_id=proveedor.id)

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})