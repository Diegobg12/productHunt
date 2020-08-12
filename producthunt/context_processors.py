
from products.models import *

def add_variable_to_context(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return {
        'Categories': categories,
    }
