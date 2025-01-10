from rest_framework import serializers
from .models import Customer, Address, ContactNote

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ContactNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNote
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    notes = ContactNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
