from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('homepage/', include('homepage.urls')),
    path('admin/', admin.site.urls),
]
