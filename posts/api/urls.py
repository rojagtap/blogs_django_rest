from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogPostsAPIView.as_view(), name='api-all'),
    path('rud/<int:pk>/', views.BlogPostsRUD.as_view(), name='api-rud'),
]