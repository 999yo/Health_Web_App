from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('',include('vital_input.urls')),
    path('',include('vital_log.urls')),
    path('',include('data_tables_view.urls')),
    
]
