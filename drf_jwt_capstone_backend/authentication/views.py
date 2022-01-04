from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, BusinessSerializer, MessageSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Business, Message, User
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

class GetUser(APIView):  

    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)    
        except:
            raise status.HTTP_404_NOT_FOUND

    def patch(self, request, pk):
        user = self.get_object(pk)
        serializer = RegistrationSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)            

class GetBusiness(APIView):

    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Business.objects.get(pk=pk)
        except:
            raise status.HTTP_404_NOT_FOUND    

    def get(self, request):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        business = self.get_object(pk)
        serializer = BusinessSerializer(business, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk):
        business = self.get_object(pk)
        business.delete()       
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetMessage(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
