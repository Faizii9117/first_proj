from rest_framework import serializers
from api_app.models import login_api

class loginserializer(serializers.ModelSerializer):
    class Meta:
        model = login_api
        fields = ['Email', 'password']  # Ensure all fields are listed
