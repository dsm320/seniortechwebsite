from django.contrib import admin
from blog.models import Post, Category, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'last_modified')
    inlines = [
        CommentInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

    def name(self, obj):
        return (obj.name)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)