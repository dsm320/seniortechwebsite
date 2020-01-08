from django.contrib import admin
from home.models import Welcome, Testimonial

# Register your models here.

class TestimonialInline(admin.TabularInline):
    model = Testimonial

class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('short_text', )
    inlines = [
        TestimonialInline
    ]
    
    def short_text(self, obj):
        return (obj.text[:50] + '...')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_text')

    def short_text(self, obj):
        return (obj.text[:50] + '...')

admin.site.register(Welcome, WelcomeAdmin)
admin.site.register(Testimonial, TestimonialAdmin)