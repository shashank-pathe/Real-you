from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from .views import MyTokenObtainPairView

urlpatterns = [
    path('hello/', views.hello_world),
    path('product_Categories', views.ProductCategoryListAPIView.as_view(), name='product-categories'),
    path('product_details/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('categories/<int:category_id>/products/', views.ProductListByCategoryAPIView.as_view(), name='product-list-by-category'),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
