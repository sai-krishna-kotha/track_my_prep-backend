from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserView, ProblemViewSet

router = DefaultRouter()
router.register(r'problems', ProblemViewSet, basename='problem')

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('', include(router.urls)),
]