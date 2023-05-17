from httplib2 import Response
from rest_framework import generics
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from news_prduct.models import Product
from news_prduct.serializer import *
from rest_framework import exceptions
from rest_framework.filters import OrderingFilter
from paginations import CustomPageNumberPagination


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('-id')
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('category', 'brand')
    ordering_fields = ('id', 'title')
    search_fields = ('title', 'category_title', 'brand_title')
    pagination_class = CustomPageNumberPagination
    serializer_class = ProductListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductListSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProductCreateSerializer
        return ProductListSerializer
   