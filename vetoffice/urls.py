from django.urls import path
from django.contrib import admin

from vetoffice.views import home, register_owner

app_name = 'vetoffice'

urlpatterns = [
    path('', home, name='home'),
    path('owner/register/', register_owner, name='register_owner'),
    path('admin/', admin.site.urls),
]
