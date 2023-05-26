from rest_framework import serializers
from comment.models import LikeDislike


class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = ("id", "blog", "user", "type")


class LikeDislikeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = ("id", "blog", "user", "type")
        read_only_fields = ("id",)
        
