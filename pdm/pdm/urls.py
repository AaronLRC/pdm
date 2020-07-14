"""pdm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# Heroku
from django.conf import settings
from django.conf.urls.static import static

# Login
from .views import signup

# Pages
from .views import index_view
from .views import dashboard_view
from .views import personal_view
from .views import lista_kits_view
from .views import personal_historial_view
from .views import pdp_view

# Oauth
from .views import login_rest_framework_view
from .views import get_name_rest_framework_view
from .views import get_kit_data_view

# Twilio
from .views import get_grafana_webhook_view
from .views import alarm_by_sms_view


urlpatterns = [

    path('admin/', admin.site.urls),
    # -----------------INICIO LOGIN----------------
    path('accounts/', include('django.contrib.auth.urls')), # No register auth builded
    url(r'^accounts/register/$',signup,name='signup'),
    # -----------------FIN LOGIN----------------

    # -----------------INICIO INDEX----------------
    path('', index_view, name='main-view'),
    path('pdp/', pdp_view, name='pdp'),
    # ------------------FIN INDEX------------------
    # -----------------INICIO DASHBOARD----------------
    path('dashboard/', dashboard_view, name='dashboard-view'),
    path('dashboard/lista_kits/', lista_kits_view, name='lista-de-kits-view'),
    path('dashboard/personal/', personal_historial_view,
         name='personal-historial-view'),


    path('personal/', personal_view, name='personal-view'),
    # ------------------FIN DASHBOARD------------------
    # -----------------INICIO API----------------
    path('api/', include('api.urls')),
    # ------------------FIN API------------------

    # -----------------INICIO OAUTH----------------
    path('auth2/', include('rest_framework_social_oauth2.urls')),
    path('auth/login/', login_rest_framework_view,
         name='login_auth_rest_framework'),
    path('auth/logged/get_data_user/', get_name_rest_framework_view,
         name='get_data_user_rest_framework'),
    path('auth/logged/get_user_kit_data/',
         get_kit_data_view, name='get_user_kit_data'),

    # -----------------FIN OAUTH----------------

    # -----------------INICIO TWILIO----------------
    path('auth/grafana/get_webhook',get_grafana_webhook_view,name='get_grafana_webhook_view'),
    path('auth/logged/send_message/',alarm_by_sms_view,name='alarm_by_sms_view'),
    # -----------------FIN TWILIO----------------

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
