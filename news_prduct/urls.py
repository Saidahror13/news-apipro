from django.urls import path

from news_prduct.views import ProductDetailView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>', ProductDetailView.as_view(), name='products-detail')
]
