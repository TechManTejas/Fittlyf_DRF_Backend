from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from enquiry.views import EnquiryViewSet  

router = DefaultRouter()
router.register('enquiries', EnquiryViewSet, basename='enquiries') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  
]
