#from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf.urls.static import static
from django.db import models
from django.contrib.auth.models import User

#fs_fotos = FileSystemStorage(location=settings.STATICFILES_DIRS[0] +'/fotos')                                                           



# Create your models here.
class chofer(models.Model):
    id = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=200,blank=True,null=True)
    apellidos = models.CharField(max_length=400,blank=True,null=True)
    fechNacimiento = models.TextField(max_length=100, blank=True,null=True)
    direccion = models.TextField(max_length=100, blank=True,null=True)
    correo = models.TextField(max_length=100, blank=True,null=True)
    telCasa = models.TextField(max_length=100, blank=True,null=True)
    telCelular = models.TextField(max_length=100, blank=True,null=True)
    urlQr= models.TextField(max_length=100, blank=True,null=True)
    #foto = models.FileField(verbose_name='Orchivo', #storage=fs_fotos, help_text='Forografía', null=True, blank=True)
    foto = models.FileField(verbose_name='Orchivo',  help_text='Forografía', null=True, blank=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        db_table = 'chofer'
        verbose_name = 'chofer'
        verbose_name_plural = 'choferes'

class contratos(models.Model):
    id = models.AutoField(primary_key=True)
    fechaInicio = models.CharField(max_length=50,blank=True, null=True)
    fechaFinal = models.CharField(max_length=50,blank=True, null=True)
    observaciones = models.CharField(max_length=50,blank=True, null=True)
    fk_chofer = models.ForeignKey(chofer, on_delete=models.PROTECT,verbose_name="fk_chofer",db_column='fk_chofer', null=True, blank=False)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        db_table = 'contrato'
        verbose_name = 'contrato'
        verbose_name_plural = 'contratos'

class Profile(models.Model):
    #fk_clues = models.ForeignKey(catalogos, on_delete=models.PROTECT,verbose_name="Clues",related_name='fk_clues',db_column='fk_clues', null=True, blank=False)
    #fk_localidades = models.ForeignKey(catalogos, on_delete=models.PROTECT,verbose_name="Localidad",related_name='fk_localidades',db_column='fk_localidades', null=True, blank=False)
    cp = models.CharField(max_length=50,blank=True, null=True)
    telefono = models.CharField(max_length=50,blank=True, null=True)
    correo = models.CharField(max_length=200,blank=True, null=True)
    nombre = models.CharField(max_length=200,blank=True, null=True)
    apellidos = models.CharField(max_length=200,blank=True, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self): 
        return self.user.username

class ruta(models.Model):
    id =  models.AutoField(primary_key=True)
    latitud  = models.CharField(max_length=200, blank=True, null=True)
    longitud = models.CharField(max_length=200, blank=True, null=True)
    calificacion = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.CharField(max_length=50, blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        db_table = 'ruta'
        verbose_name = 'ruta'
        verbose_name_plural = 'rutas'

class solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    fk_usuario = models.CharField(max_length=400, blank=True, null=True)#models.ForeignKey(Profile, on_delete=models.PROTECT,verbose_name="fk_usuario",db_column='fk_usuario', null=True, blank=False)
    direccionInicial = models.CharField(max_length=400, blank=True, null=True)
    latitudInicial  = models.CharField(max_length=200, blank=True, null=True)
    longitudInicial = models.CharField(max_length=200, blank=True, null=True)
    direccionFinal = models.CharField(max_length=400, blank=True, null=True)
    latitudFinal  = models.CharField(max_length=200, blank=True, null=True)
    longitudFinal = models.CharField(max_length=200, blank=True, null=True)
    solicitudEspecial = models.CharField(max_length=200, blank=True, null=True)
    programacionViaje = models.CharField(max_length=200, blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True, default=1, editable=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        db_table = 'solicitud'
        verbose_name = 'solicitud'
        verbose_name_plural = 'solicitudes'

class seguiminento(models.Model):
    id = models.AutoField(primary_key= True)
    fk_solicitud = models.ForeignKey(solicitud, verbose_name="fk_solicitud", on_delete=models.CASCADE, null=True, blank=False)
    fk_chofer = models.ForeignKey(chofer, verbose_name="fk_chofer", on_delete=models.CASCADE, null=True, blank=False)
    fk_ruta = models.ForeignKey(ruta, verbose_name="fk_ruta", on_delete=models.CASCADE, null=True, blank=False)
    estatus = models.IntegerField(blank=True, null=True)    

    class Meta:
        verbose_name = "seguimiento"
        verbose_name_plural = "seguimientos"

    def __str__(self):
        return '%s' % self.id

class solicitudFormulario(models.Model):
    id = models.AutoField(primary_key= True)
    nombreCompleto = models.CharField(max_length=400, blank=True, null=True)
    direccionActual = models.CharField(max_length=600, blank=True, null=True)
    direccionFinal = models.CharField(max_length=600, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    horaSolicitud = models.DateTimeField(auto_now=False, auto_now_add=False)#(null=True, blank=True)
    horaAtencion = models.DateTimeField(null=True, blank=True)
    requerimientosAdicionales = models.CharField(max_length=600, blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True,default=2,editable=True)#2 pendiente, 1 atendidio, 3 cancelado    

    class Meta:
        db_table = 'solicitudFormulario'
        verbose_name = "solicitudFormulario"
        verbose_name_plural = "solicitudesFormulario"

    def __str__(self):
        return '%s' % self.id

