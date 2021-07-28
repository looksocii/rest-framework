from django.contrib.auth.models import User, Group
from testAPI.models import Booklist, Category, Payment, Useraccount
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BooklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booklist
        fields = ['title', 'author', 'price_rent']