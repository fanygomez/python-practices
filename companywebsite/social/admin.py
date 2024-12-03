from django.contrib import admin
from .models import Link
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists(): #Si el usuario en sesion, pertenece al grupo personal
            return ('key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)  