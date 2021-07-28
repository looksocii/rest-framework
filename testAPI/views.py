from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from testAPI.serializers import UserSerializer, GroupSerializer, BooklistSerializer
from testAPI.models import Booklist

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class BooklistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Booklist.objects.all()
    serializer_class = BooklistSerializer
    permission_classes = [permissions.IsAuthenticated]
