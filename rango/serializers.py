from django.contrib.auth.models import User, Group
from rango.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = User
		fields = ('id', 'username', 'snippets', 'owner')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')
				
class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
