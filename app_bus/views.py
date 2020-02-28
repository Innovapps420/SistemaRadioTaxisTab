from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from app_bus.serializers import *
import datetime
import json
from django.http import JsonResponse

# Create your views here.
class TokenViewSet(ModelViewSet):
	queryset = Token.objects.all()
	serializer_class = TokenSerializer

	def get_perfil(self,request,token):
		
		usuario = Token.objects.get(key=token)
		queryset = Profile.objects.filter(user_id=usuario.user_id)
		serializer = ProfileSerializer(queryset, many=True)
		return Response(serializer.data)

class solicitudViewSet(ModelViewSet):
    queryset = solicitud.objects.all()
    serializer_class = solicitudSererializer

class userViewSet(ModelViewSet):
	queryset= User.objects.all()
	serializer_class = userSerializer

class solicitudFormularioViewSet(ModelViewSet):
	queryset = solicitudFormulario.objects.all()
	serializer_class = solicitudFormularioSererializer

	def solicitudFiltro(self,request):
		"""if(request.GET["estatus"]=="1"):
			queryset = solicitudFormulario.objects.filter(estatus__in=[1,2])
		else:
			queryset = solicitudFormulario.objects.filter(estatus=3)"""
		queryset = solicitudFormulario.objects.filter(estatus=request.GET["estatus"])
		serializers = solicitudFormularioSererializer(queryset,many=True)
		return Response(serializers.data)

	def solicitudHistorial(self,request):
		fechaInicio = request.GET["fechaInicio"]
		fechaFinal = request.GET["fechaFinal"]#.strftime("%Y-%m-%d %H:%M:%S")
		#fechaFinal = fechaFinal + datetime.timedelta(days=1)
		#print(fechaFinal)
		queryset = solicitudFormulario.objects.filter(horaSolicitud__range=[fechaInicio,fechaFinal],estatus=request.GET["estatus"])
		serializers = solicitudFormularioSererializer(queryset,many=True)
		return Response(serializers.data)

	def estatusdHistorial(self,request):
		contador = solicitudFormulario.objects.filter(estatus=2).count()
		return JsonResponse({"pendientes": contador})



"""    def guardar_solicitud(self,request):
        token = request.GET['token']
        usuario = Token.objects.get(key=token)

		fechaInicio = self.request.GET['fechaInicio']
		fechaFinal = self.request.GET['fechaFinal']
		queryset = p_v.objects.filter(fk_proceso__fecha_captura__range=[fechaInicio, fechaFinal])
        """