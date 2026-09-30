from django.contrib import admin
from . import models
# Register your models here.
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user','posting')
    ordering = ('user',)
admin.site.register(models.Favorite, FavoriteAdmin)
# Register your models here.
