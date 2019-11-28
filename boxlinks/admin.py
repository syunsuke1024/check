from django.contrib import admin

# Register your models here.
from .models import User,Links
class LinksAdmin(admin.ModelAdmin):
    list_display = ("priority","link","memo","user")

admin.site.register(User)
admin.site.register(Links,LinksAdmin)
