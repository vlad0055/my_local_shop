
from .models import Product
from django.views.generic import ListView






class Product(ListView):
	model=Product
	template_name='legend_shop_main/main_page.html'
	context_object_name='product'
	



	


	





