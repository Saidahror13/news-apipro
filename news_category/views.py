from rest_framework import generics
from news_category.models import Category
from news_category.serializer import CategorySerializer


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CategorySerializer
        return CategorySerializer
