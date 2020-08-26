"""
Project URL configuration
"""
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # API specific paths are set by the 'urls.py' file in the 'api' directory
    path("bccapi/", include("student_profile.urls")),
    path("admin/", admin.site.urls),

    # Path for the Vue Single-Page Application (SPA)
    re_path(r'^app/(.*)$', 
            TemplateView.as_view(
                template_name="spa.html",
                extra_context={ "ENV_NAME": settings.ENV_NAME }),
            name="app"),
    path('', 
            TemplateView.as_view(
                template_name="spa.html",
                extra_context={ "ENV_NAME": settings.ENV_NAME }),
            name="app")



]
if settings.DEBUG:      
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
