import django
from django.urls import include, re_path
from django.contrib import admin


admin_urls = admin.site.urls

urlpatterns = [
    re_path(r'^admin/', admin_urls),
]
