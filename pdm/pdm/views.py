from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
###########################################################
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
###########################################################


# from .models import ProductoHijoCompra
# from .models import ProductoPadre
# from .models import Proveedor
# from .models import BoletaCompra
# ###########################################################
# from .models import ProductoPlato
# from .models import PlatoPadre
# from .models import PlatoHijoVenta
# from .models import BoletaVentaRestaurante
# from .models import ProductoHijoTransaccion


###########################################################
from django.utils.timezone import get_current_timezone
import datetime
##########################################################
from django.db.models import Count
from django.db.models import Sum
from django.db.models import F

# ------------------------ INICIO INDEX ------------------


def index_view(request):

    # Variables de reporte mensual
    text1 = "Bienvenido a la plataforma virtual"
    text2 = "Conoce "
    text3 = "MedicPUCP"

    text_kit_1 = "Ajustes unisex"
    text_kit_2 = "Nuestro kit cuenta con correas que se ajustan a la anatomía tanto en el caso de los hombres como para las mujeres."
    text_kit_3 = "Sensado no-invasivo"
    text_kit_4 = "Los kits están diseñados para no ser invasivos y poder ser usados por el personal operativo."
    text_kit_5 = "MedicSensor1"
    text_kit_6 = "Gestiona 3 signos vitales elementales de forma inalámbrica: frecuencia respiratoria, presión cardíaca y temperatura corporal. Duración de hasta 12 horas por carga. Seguimiento en tiempo real."

    text_cel = "Cel: 900000000"
    text_cel_2 = "900000000"
    text_email = "administrador@medicpucp.com"
    text_address = "Dirección: - "
    text_days = "Lun-Vie: 10:00 - 18:00 "
    text_days_2 = "Sábado-Dom: 11:00 - 13:00"

    return render(request, 'index/index.html', locals())

# -------------------------- FIN INDEX -------------------

# -------------------- INICIO DASHBOARD -----------------
@login_required(login_url='/accounts/login')
def dashboard_view(request):

    page_title = "MedicPUCP v1 - D"
    platform="MedicPUCP"
    nombre_vista = 'Dashboard | Resumen general'
    ruta_vista = ['Dashboard', 'Resumen general']
    year=2020

    indicador1="17%"
    indicador1_porcentaje="150"
    indicador2="10%"
    indicador2_porcentaje="76"
    indicador3="20%"
    indicador3_porcentaje="7 momentos"
    indicador4="18%"
    indicador4_porcentaje="15"


    # Para mostrar en tabla vamos a usar GROUPBY
    # tutorial sacado de https://stackoverflow.com/a/629600/10491422
    # tablaBoletasCompra = ProductoHijoCompra.objects.raw(
    #     'SELECT MIN(id) AS id,MAX(id_boleta_compra) AS id_boleta_compra, SUM(precio) AS precio_total, COUNT(*) AS nro_productos FROM producto_hijo_compra GROUP BY id_boleta_compra ORDER BY id_boleta_compra DESC;')
    # tablaBoletasVenta = PlatoHijoVenta.objects.raw(
    #     'SELECT MIN(id) AS id, MAX(id_boleta_venta_restaurante) AS id_boleta_venta_restaurante, SUM(precio_venta) AS precio_total,  COUNT(*) AS nro_productos  FROM plato_hijo_venta GROUP BY id_boleta_venta_restaurante ORDER BY id_boleta_venta_restaurante DESC;')
    # sumaBoletasVentasMes=
    # sumaBoletasComprasMes=PlatoHijoVenta.objects.raw('SELECT MIN(id) AS id, MAX(id_boleta_venta_restaurante) AS id_boleta_venta_restaurante, SUM(precio_venta) AS precio_total,  COUNT(*) AS nro_productos  FROM plato_hijo_venta GROUP BY id_boleta_venta_restaurante ORDER BY id_boleta_venta_restaurante DESC;')
    maxItemTabla = 5

    return render(request, 'dashboard/estadisticas/dashboard.html', locals())


@login_required(login_url='/accounts/login')
def lista_kits_view(request):

    nombre_vista = 'Dashboard | Lista de kits'
    ruta_vista = ['Dashboard', 'Lista de kits']

    return render(request,'dashboard/kits/lista_kits.html',locals())

@login_required(login_url='/accounts/login')
def personal_historial_view(request):

    nombre_vista = 'Dashboard | Personal'
    ruta_vista = ['Dashboard', 'Personal']

    return render(request,'dashboard/personal/personal.html',locals())


# ----------------------- FIN DASHBOARD -----------------


# -------------------- INICIO PERSONAL -----------------
@login_required(login_url='/accounts/login')
def personal_view(request):

    page_title = "MedicPUCP v1 - P"
    platform="MedicPUCP"
    nombre_vista = 'Dashboard'
    ruta_vista = ['Dashboard']
    year=2020

    return render(request, 'personal/personal.html', locals())

# -------------------- FIN PERSONAL  -----------------
