from rest_framework import viewsets
from .models import Customer, Address, ContactNote
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import CustomerSerializer, AddressSerializer, ContactNoteSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True 
        return request.user and request.user.is_staff 
    
class StandardResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['date_created', 'last_name']
    authentication_classes = [SessionAuthentication, BasicAuthentication]  
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]  


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = StandardResultsPagination 
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ContactNoteViewSet(viewsets.ModelViewSet):
    queryset = ContactNote.objects.all()
    serializer_class = ContactNoteSerializer
    pagination_class = StandardResultsPagination  
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated] 
