from .models import Owner, Repo
from rest_framework import serializers


class OwnerHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    repos = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='repo-detail'
    )

    class Meta:
        model = Owner
        fields = ['url', 'id', 'login', 'html_url', 'type', 'repos', 'info']


class RepoHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repo
        fields = ['url', 'id', 'owner', 'full_name',
                  'private', 'html_url', 'created_at', 'info']


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ['id', 'login', 'html_url', 'type', 'info']


class RepoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Repo
        fields = ['id', 'owner', 'full_name',
                  'private', 'html_url', 'created_at', 'info']
