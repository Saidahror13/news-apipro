from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from news_category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'updated_at')


# class ProductCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'title')


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'position', 'parent']

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['category'] = ProductCategorySerializer(instance.category).data
    #     return data

