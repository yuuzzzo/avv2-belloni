from django.contrib import admin
from django.urls import path
from product.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, ProdutoDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('' , ProdutoListView.as_view(), name='produto-list'),
    path('produto/add/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produto/<int:pk>/update/', ProdutoUpdateView.as_view(), name='produto-update'),
    path('produto/<int:pk>/delete/', ProdutoDeleteView.as_view(), name='produto-delete'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto-detail'),
]