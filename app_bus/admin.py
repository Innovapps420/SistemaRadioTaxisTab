from django.contrib import admin
from app_bus.models import *
from django.contrib.sites.models import Site
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', )
    list_select_related = ('profile', )

   # def get_cuenta_facebook(self, instance):
   #     return instance.profile.cuenta_facebook
   # get_cuenta_facebook.short_description = 'cuenta_facebook'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(chofer)
admin.site.register(contratos)
admin.site.register(ruta)
admin.site.register(solicitud)
admin.site.register(seguiminento)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

