from rest_framework import serializers
from .models import Company


class CompanyRegisterSeralizer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'
  def create(self, validated_data):
    return Company.objects.create(**validated_data)

class SendDataSeralizer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = ['company_name', 'logo', 'location']
    
class UserSeralizer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = ['username', 'password']
