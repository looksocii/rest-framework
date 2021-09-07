from testAPI.models import Booklist, Category, Payment, Useraccount
from rest_framework import serializers

class UseraccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Useraccount
        fields = ['id', 'firstname', 'lastname', 'username', 'password', 'email', 'phone', 'imguserurl']

class BooklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booklist
        fields = ['id', 'title', 'author','short_title','img_book', 'price_rent', 'category_id']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'content']

class AllbookSerializer(serializers.HyperlinkedModelSerializer):
    fields = ['title', 'author','short_title','img_book', 'price_rent', 'content']
