from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Muda o nome do 
admin.site.site_header = 'Safe Place'

# Muda o nome do titulo
admin.site.site_title = 'Everthings gonna be fine'


