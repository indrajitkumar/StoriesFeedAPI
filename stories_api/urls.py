from django.urls import path, include
from rest_framework.routers import DefaultRouter

from stories_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
