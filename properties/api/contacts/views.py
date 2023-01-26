from django.conf import settings
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from properties.api.contacts.models import ContactModel
from properties.api.contacts.serializers import ContactSerializer

from django.core.mail import send_mail, EmailMessage
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ContactSerializer
    #parser_classes = [MultiPartParser, FormParser]

    
    def post(self, request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                #contact_name = serializer.validated_data["name"]
                #print(contact_name)
               # contact_email = serializer.validated_data["email"]
                #contact_subject = serializer.validated_data["subject"]
                from_email = settings.EMAIL_HOST_USER
                to = settings.RECIPIENT_ADDRESS
                subject = f'New contact {serializer.validated_data["subject"]}: {serializer.validated_data["name"]}: {serializer.validated_data["email"]}'
                plain_message = serializer.validated_data["message"]
                send_mail('subject', 'plain_message', from_email, [to])
                response = {
                'success' : 'True',
                'message': 'Form submitted successfully',
                }
                return Response(response, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


