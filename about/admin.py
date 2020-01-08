from django.contrib import admin
from about.models import About

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('short_text', )
    
    def short_text(self, obj):
        return (obj.text[:50] + '...')

admin.site.register(About, AboutAdmin)