from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

    def __str__(self) -> str:
        return super().__str__()


class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

    def __str__(self) -> str:
        return super().__str__()
