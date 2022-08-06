from django.contrib import admin
from .models import Document

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('subject_id','doc')

admin.site.register(Document, DocumentAdmin)