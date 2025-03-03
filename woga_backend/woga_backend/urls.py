from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin-woga/', admin.site.urls),
    path("",include("core.urls")),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls'))
]
