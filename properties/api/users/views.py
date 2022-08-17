from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework import permissions
from rest_framework import status
from django.http import Http404

from properties.api.users.serializers import ( 
                                                UserSerializer, 
                                                #ProfileSerializer,
                                               # UserUpdateSerializer
                                                )
from properties.api.users.models import  User, Profile
from properties.api.users.permissions import IsOwnerOrReadOnly



class SignupView(CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer

    
    def post(self, request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = {
                'success' : 'True',
                'message': 'User registered  successfully',
                }
                return Response(response, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk=None, format=None):
        user = User.objects.all()  
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(user, context=serializer_context, many=True)    
        return Response(serializer.data)
    

class UserRetrieveView(RetrieveAPIView):
    #lookup_field = "user_id"
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, ):
        return User.objects.get(id=self.kwargs.get("uuid"))


class UpdateUserView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer

    def get_object(self):
        return User.objects.get(id=self.kwargs.get("uuid"))
