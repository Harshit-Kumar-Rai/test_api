from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from.serializer import CompanyRegisterSeralizer, SendDataSeralizer, UserSeralizer
from .models import Company

@api_view(['POST'])

def validate_user(request):
  if request.method == 'POST':
    serializer = UserSeralizer(data=request.data)
    if serializer.is_valid():
      validated_data = serializer.validated_data
      username = validated_data.get('username')
      password = validated_data.get('password')
      
      try:
        data = Company.objects.get(username = username, password = password)
      except:
        return Response({'error':'Invalid user data'},status=status.HTTP_400_BAD_REQUEST)
      userdata = SendDataSeralizer(data)
      return Response (userdata.data)
    
