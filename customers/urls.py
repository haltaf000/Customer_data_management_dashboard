from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, AddressViewSet, ContactNoteViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'notes', ContactNoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
