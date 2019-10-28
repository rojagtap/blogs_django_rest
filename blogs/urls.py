from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('posts.urls')),
    path('api/', include('posts.api.urls')),
    path('admin/', admin.site.urls),
]
