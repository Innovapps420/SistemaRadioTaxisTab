"""plantilla URL Configuration

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
from django.urls import path
from django.conf import settings
from rest_framework.authtoken import views as vista
from app_bus.views import *
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView 
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', vista.obtain_auth_token, name='api-token-auth'),
    path('rest-auth/login/', LoginView.as_view(), name='rest_login'),
    path('rest-auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('',TemplateView.as_view(template_name="index.html"),name='index'),
    path('adminTaxi',TemplateView.as_view(template_name="index2.html"),name='index'),
    path('api/solicitud/',solicitudViewSet.as_view({'post': 'create','get': 'list'}), name='crear_solicutud_app'),
    path('api/user',userViewSet.as_view({'post':'create','get':'list'}), name='crear_usuario'),
    path('panel/',TemplateView.as_view(template_name="views/solFormPendientes.html"),name='nuevo'),
    path('list/solicitudFormulario/',solicitudFormularioViewSet.as_view({'post': 'create'}), name='crear_solicutud_formulario'),
    path('estatus/solicitudFormulario/',solicitudFormularioViewSet.as_view({'get': 'solicitudFiltro'}), name='crear_solicutud_formulario'),
    path('solicitudHistorial/',solicitudFormularioViewSet.as_view({'get': 'solicitudHistorial'}), name='historial_formulario'),
    path('estatusSolicitudes/',solicitudFormularioViewSet.as_view({'get': 'estatusdHistorial'}), name='estatus_formulario'),
    path('solFormPen/',TemplateView.as_view(template_name="views/solFormPendientes.html"),name='nuevo'),
    path('histSolicitus/',TemplateView.as_view(template_name="views/historialSolicitudes.html"),name='nuevo'),
    path('api/solicitudFormulario/<int:pk>',solicitudFormularioViewSet.as_view({'get': 'retrieve','put':'update','patch':'partial_update'}), name='modificar_solicutud_formulario'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
