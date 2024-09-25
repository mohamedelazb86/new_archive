from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Document_Type,Sector,Contractor

class ContractorAdmin(SummernoteModelAdmin):
    list_display=['code','name','item','sector']
    list_filter=['sector']
    search_fields=['name','notes','item']
    summernote_fields = ('notes',)



admin.site.register(Document_Type)
admin.site.register(Sector)
admin.site.register(Contractor,ContractorAdmin)
