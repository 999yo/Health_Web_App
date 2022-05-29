from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("user_data_table.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('',include('vital_input.urls')),
    path('',include('vital_log.urls')),
    path('', include('user_json.urls')),
    
]
