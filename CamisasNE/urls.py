
from django.contrib import admin
from django.urls import path, include 
from usuarios import views as usuarios_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', usuarios_views.home, name='home'),

    
]
