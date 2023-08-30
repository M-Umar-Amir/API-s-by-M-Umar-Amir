from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UsersSerializer, GroupsSerializer
# Create your views here.


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupsView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [permissions.IsAuthenticated]
