from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.http import FileResponse, HttpResponse

from enquiry.views import EnquiryViewSet


def serve_auth_file(request):
    file_path = "./media/F58E1676425A461D94963EF59B90FE4E.txt"

    try:
        return FileResponse(open(file_path, "rb"), as_attachment=True)
    except FileNotFoundError:
        return HttpResponse("File not found.", status=404)

router = DefaultRouter()
router.register("enquiries", EnquiryViewSet, basename="enquiries")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path(
        ".well-known/pki-validation/F58E1676425A461D94963EF59B90FE4E.txt/",
        serve_auth_file,
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
