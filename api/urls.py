from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from .views import MyTokenObtainPairView

urlpatterns = [
    path('hello/', views.hello_world),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
