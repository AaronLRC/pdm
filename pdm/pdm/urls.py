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

# Heroku
from django.conf import settings
from django.conf.urls.static import static

# Pages
from pdm.views import index_view
from pdm.views import dashboard_view
from pdm.views import personal_view
from pdm.views import lista_kits_view
from pdm.views import personal_historial_view



urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # -----------------INICIO INDEX----------------
    path('', index_view, name='main-view'),
    # ------------------FIN INDEX------------------
    # -----------------INICIO DASHBOARD----------------
    path('dashboard/', dashboard_view, name='dashboard-view'),
    path('dashboard/lista_kits/', lista_kits_view, name='lista-de-kits-view'),
    path('dashboard/personal/', personal_historial_view, name='personal-historial-view'),

    
    path('personal/', personal_view, name='personal-view'),
    # ------------------FIN DASHBOARD------------------
    # -----------------INICIO API----------------
    path('api/', include('api.urls')),
    # ------------------FIN API------------------

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
