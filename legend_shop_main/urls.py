from django.urls import path

from  .views import Product

urlpatterns = [
    path('main_page', Product.as_view(), name='main_page'),
    

]

