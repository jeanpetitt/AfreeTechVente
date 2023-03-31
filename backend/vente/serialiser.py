from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.http.response import Http404

class UserSerialiser(serializers.Serializer):

	model = Utilisateur
	fields = '__all__'

class FruitSerialiser(serializers.Serializer):

	model = Fruit
	fields = '__all__'



# user login serializer
class UserLoginSerialiser(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):

        user = authenticate(username=clean_data['email'], password=clean_data['password'])

        if not user:
            raise Http404

        return user
