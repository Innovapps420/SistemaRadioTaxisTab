from rest_framework.serializers import ModelSerializer
from app_bus.models import *
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ["id","first_name","last_name"]

class ProfileSerializer(ModelSerializer):
	user = UserSerializer(read_only=True)
	class Meta:
		model = Profile
		fields = "__all__"

class TokenSerializer(ModelSerializer):
	#fk_usuario = UserLSerializer(read_only=True)
	class Meta:
		model = Token
		fields = "__all__"

class solicitudSererializer(ModelSerializer):
    class Meta:
        model = solicitud
        fields = "__all__"
    
    def create(self,validated_data):
        request = self._context.get("request")
        usuario = Token.objects.get(key=request.POST['fk_usuario'])
        perfil= Profile.objects.get(user_id=usuario.user_id)
        #print(perfil.id)
        nuevaSolicitud = solicitud.objects.create(fk_usuario=perfil.id,direccionInicial=validated_data['direccionInicial'])#(**validated_data,fk_usuario=perfil.id)
        #nuevaSolicitud.save()
        return nuevaSolicitud

class userSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]

    def create(self,validated_data):
        nuevoUsuario = User.objects.create(username=validated_data["username"])
        nuevoUsuario.set_password(validated_data["password"])
        return nuevoUsuario

class solicitudFormularioSererializer(ModelSerializer):
    class Meta:
        model = solicitudFormulario
        fields = "__all__"
			
			
