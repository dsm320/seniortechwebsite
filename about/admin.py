from django.contrib import admin
from about.models import About, Biography

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('short_text', )
    
    def short_text(self, obj):
        return (obj.text[:50] + '...')

class BioAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'short_text')

    def name(self, obj):
        return (obj.name)

    def short_text(self, obj):
        return (obj.bio[:50] + '...')

admin.site.register(About, AboutAdmin)
admin.site.register(Biography, BioAdmin)