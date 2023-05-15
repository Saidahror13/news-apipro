from rest_framework import generics
from django.shortcuts import render

from news_category.models import Category
from news_category.serializer import CategorySerializer


# Create your views here.

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return CategorySerializer
        return CategorySerializer
