from email import message
from rest_framework import serializers
from properties.api.contacts.models import ContactModel



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ('id', 'name', 'email', 'subject', 'message')




   