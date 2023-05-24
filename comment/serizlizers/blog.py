from rest_framework import serializers
from ..models import Blog
from news_category.models import Category
from users.models import User


class BlogAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()
    author = BlogAuthorSerializer()

    class Meta:
        model = Blog
        fields = ("id", "author", "title", "slug", "image", "category", "collab", "body")


class BlogCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    category = BlogCategorySerializer()
    author = BlogAuthorSerializer()

    class Meta:
        model = Blog
        fields = ["id", "author", "title", "slug", "image", "category", "collab", "body"]
