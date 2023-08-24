from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone')
    list_filter = ('phone',) 
    search_fields = ('phone', '')
