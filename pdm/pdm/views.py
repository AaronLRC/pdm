from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
###########################################################
from django.shortcuts import redirect, render
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

##########################################################
# Allow iFrame
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin

##########################################################
# ALLOW REST_FRAMEWORK LOGIN
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from .models import AuthtokenToken
from .models import AuthUser
from .models import ApiMedicKitPerUser
from .forms import SignUpForm
from django.contrib import messages

##########################################################
# ALLOW TWILIO
from twilio.rest import Client


# ------------------------  INICIO LOGIN ------------------
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Nueva cuenta registrada satisfactoriamente.')
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form':form})

# ------------------------  FIN LOGIN ------------------

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
    text_kit_5 = "MediKit"
    text_kit_6 = "Gestiona 2 signos vitales elementales de forma inalámbrica: frecuencia respiratoria y temperatura corporal. Duración de hasta 12 horas por carga. Seguimiento en tiempo real."

    text_kit_7 = "MediBand"
    text_kit_8 = "Gestiona el sensado de presión cardíaca."
    text_kit_9 = "Sensado no-invasivo"
    text_kit_10 = "Funciona con sensado no-invasivo con una duración de hasta 12 horas."

    vista_3d_medikit = 'https://a360.co/2Z5LKM0'
    vista_3d_mediband = '#'

    text_cel = "Cel: 900000000"
    text_cel_2 = "900000000"
    text_email = "administrador@medicpucp.com"
    text_address = "Dirección: - "
    text_days = "Lun-Vie: 10:00 - 18:00 "
    text_days_2 = "Sábado-Dom: 11:00 - 13:00"

    return render(request, 'index/index.html', locals())


def pdp_view(request):

    return render(request, 'index/pdp.html', locals())

# -------------------------- FIN INDEX -------------------

# -------------------- INICIO DASHBOARD -----------------
@login_required(login_url='/accounts/login')
def dashboard_view(request):

    page_title = "MedicPUCP v1 - D"
    platform = "MedicPUCP"
    nombre_vista = 'Dashboard | Resumen general'
    ruta_vista = ['Dashboard', 'Resumen general']
    year = 2020

    indicador1 = "17%"
    indicador1_porcentaje = "150"
    indicador2 = "10%"
    indicador2_porcentaje = "76"
    indicador3 = "20%"
    indicador3_porcentaje = "7 momentos"
    indicador4 = "18%"
    indicador4_porcentaje = "15"

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

    return render(request, 'dashboard/kits/lista_kits.html', locals())


@login_required(login_url='/accounts/login')
@xframe_options_exempt
def personal_historial_view(request):

    nombre_vista = 'Dashboard | Personal'
    ruta_vista = ['Dashboard', 'Personal']

    return render(request, 'dashboard/personal/personal.html', locals())


# ----------------------- FIN DASHBOARD -----------------


# -------------------- INICIO PERSONAL -----------------
@login_required(login_url='/accounts/login')
def personal_view(request):

    page_title = "MedicPUCP v1 - P"
    platform = "MedicPUCP"
    nombre_vista = 'Dashboard'
    ruta_vista = ['Dashboard']
    year = 2020

    return render(request, 'personal/personal.html', locals())

# -------------------- FIN PERSONAL  -----------------

# -------------------- INICIO LOGIN REST_FRAMEWORK -----------------
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_rest_framework_view(request):

    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Proporcione nombre de usuario y contraseña'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_name_rest_framework_view(request):

    # current_user = request.user
    # print(current_user)
    # return Response({'id':current_user.id,
    #                 'username':current_user.username,
    #                 'first_name':current_user.first_name,
    #                 'last_name':current_user.last_name,
    #                 'email':current_user.email,
    #                     },status=HTTP_200_OK)
    token = request.data.get("token")
    if token is None:
        return Response({'error': 'Porfavor envia un token válido'}, status=HTTP_400_BAD_REQUEST)
    user_by_token = AuthtokenToken.objects.get(pk=token)
    id_user_by_token = user_by_token.user_id
    if int(id_user_by_token) > 1:
        user_data = AuthUser.objects.get(pk=id_user_by_token)
        return Response({'id': user_data.id,
                         'first_name': user_data.first_name,
                         'last_name': user_data.last_name,
                         'email': user_data.email,
                         }, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_kit_data_view(request):

    token = request.data.get("token")
    if token is None:
        return Response({'error': 'Porfavor envia un token válido'}, status=HTTP_400_BAD_REQUEST)
    user_by_token = AuthtokenToken.objects.get(pk=token)
    id_user_by_token = user_by_token.user_id
    if int(id_user_by_token) > 1:
        user_kit_data = ApiMedicKitPerUser.objects.get(
            user_id=id_user_by_token)
        return Response({'kit_id': user_kit_data.kit_id,
                         'user_id': user_kit_data.user_id,
                         'estado_comunicacion': user_kit_data.estado_comunicacion,
                         'estado_baterias': user_kit_data.estado_baterias,
                         'tiempo_muestreo': user_kit_data.tiempo_muestreo,
                         }, status=HTTP_200_OK)

# -------------------- FIN LOGIN REST_FRAMEWORK -----------------





# -------------------- INICIO TWILIO REST API -----------------
                         
account_sid = "AC0d88ed0fdcad0a394549af4fb6e99b3e"
auth_token = "1a32ae905f5c7208fed6819822df7436"
client = Client(account_sid, auth_token)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_grafana_webhook_view(request):

    token = request.data.get("token")
    if token is None:
        return Response({'error': 'Porfavor envia un token válido'}, status=HTTP_400_BAD_REQUEST)
    user_by_token = AuthtokenToken.objects.get(pk=token)
    id_user_by_token = user_by_token.user_id
    if int(id_user_by_token) > 1:
        user_kit_data = ApiMedicKitPerUser.objects.get(
            user_id=id_user_by_token)
    return Response({'0':0}, status=HTTP_200_OK)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def alarm_by_sms_view(request):

    num_cel_servidor=11465185860+564340692
    num_cel_verificado=51898256060+40182029
    message = client.messages.create(
         body='MedicPUCP: [TEXTO] ',
         from_='+'+str(num_cel_servidor),
         to='+'+str(num_cel_verificado)
     )    

    return Response({'response':message.sid},status=HTTP_200_OK)
    # token = request.data.get("token")
    # if token is None:
    #     return Response({'error': 'Porfavor envia un token válido'}, status=HTTP_400_BAD_REQUEST)
    # user_by_token = AuthtokenToken.objects.get(pk=token)
    # id_user_by_token = user_by_token.user_id
    # if int(id_user_by_token) > 1:
    #     user_kit_data = ApiMedicKitPerUser.objects.get(
    #         user_id=id_user_by_token)


    #     return Response({'kit_id': user_kit_data.kit_id,
    #                      'user_id': user_kit_data.user_id,
    #                      'estado_comunicacion': user_kit_data.estado_comunicacion,
    #                      'estado_baterias': user_kit_data.estado_baterias,
    #                      'tiempo_muestreo': user_kit_data.tiempo_muestreo,
    #                      }, status=HTTP_200_OK)

# -------------------- FIN TWILIO REST API -----------------