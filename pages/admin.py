from django.contrib import admin
from .models import Theory, Sighting, BlogPost

admin.site.register(Theory)
admin.site.register(Sighting)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'author', 'added', 'slug')
	prepopulated_fields = {'slug': ('title',)}
# Register your models here.
