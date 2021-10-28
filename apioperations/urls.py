from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
app_name='app'

urlpatterns = [
    path('product_list/',product_list,name='product_list'),
    path('product_details/<int:pk>',product_detail,name='product_details'),

    
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)