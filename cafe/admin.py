from django.contrib import admin
from . import models
# Register your models here.
class PostingAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    ordering = ('-pdate',)
admin.site.register(models.Posting, PostingAdmin)
