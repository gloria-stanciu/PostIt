#render Python class to JSON

from rest_framework import serializers
from .models import PostIt

class PostItSeralizer(serializers.ModelSerializer):
    class Meta:
        model = PostIt
        fields = ('title', 'noteText', 'completed', 'created')
