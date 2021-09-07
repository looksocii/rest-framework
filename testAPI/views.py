from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from testAPI.serializers import UseraccountSerializer, BooklistSerializer, AllbookSerializer
from testAPI.models import Booklist, Useraccount, Category

class UseraccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Useraccount.objects.all()
    serializer_class = UseraccountSerializer
    # permission_classes = [permissions.IsAuthenticated]

class BooklistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Booklist.objects.all()
    serializer_class = BooklistSerializer
    permission_classes = [permissions.IsAuthenticated]

# ---------------------------------------------------------------------------------------

@api_view(['GET'])
def allbook_list(request, format=None):
    if request.method == 'GET':
        allbook = Booklist.objects.filter(category_id=2)
        serializer = BooklistSerializer(allbook, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def user_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = Useraccount.objects.all()
        serializer = UseraccountSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UseraccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        users = Useraccount.objects.get(pk=id)
    except users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UseraccountSerializer(users)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UseraccountSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
