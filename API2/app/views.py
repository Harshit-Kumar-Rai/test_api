from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from.serializer import CompanyRegisterSeralizer, SendDataSeralizer
from .models import Company

@api_view(['GET', 'POST'])

def validate_user(request, username, password):
  if request.method == 'GET':
    try:
      data = Company.objects.get(username=username, password = password)
    except:
      return Response({'error':'Invalid user data'},status=status.HTTP_400_BAD_REQUEST)
    
    serializer = SendDataSeralizer(data)
    return Response(serializer.data)