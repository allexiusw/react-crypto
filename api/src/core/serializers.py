from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Account


class AccountSerializer(serializers.ModelSerializer):
    '''Account serializer'''
    class Meta:
        model = Account
        fields = ('name',)
