# notes/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet)  # This automatically creates routes like /api/notes/

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
