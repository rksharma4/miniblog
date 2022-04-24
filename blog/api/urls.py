from django.urls import path, include
from blog.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blog', views.UserViewSet, basename = 'user')

urlpatterns = [
    path('', include(router.urls))
]