from django.db.models import fields
from rest_framework import serializers
from .models import *

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = "__all__"

class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username'
            'first_name'
            'last_name'
        ]