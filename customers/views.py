from rest_framework import viewsets
from .models import Customer, Address, ContactNote
from .serializers import CustomerSerializer, AddressSerializer, ContactNoteSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ContactNoteViewSet(viewsets.ModelViewSet):
    queryset = ContactNote.objects.all()
    serializer_class = ContactNoteSerializer
