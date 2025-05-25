
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Reg import views as v


urlpatterns = [
    path("register/", v.register, name="register"),
    path('Legacy/', include('Legacy.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('Competitive/', include('Competitive.urls')),
    path('Coaches/', include('Coaches.urls')),
    path('MastersBAC/', include('MastersBAC.urls')),
    path('Lessons/', include('Lessons.urls')),
    path('AquaAerobic/', include('AquaAerobic.urls')),
    path('summProgram/', include('summProgram.urls')),
    path('Recswim/', include('Recswim.urls')),
    path('Lapswim/', include('Lapswim.urls')),
    path('Home/', include('Home.urls')),
    path('holiday/', include('holiday.urls')),
    path('', include('Home.urls')),
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
