
from products.models import *

def add_variable_to_context(request):
    products = Product.objects.all()
    populars = Product.objects.order_by('votes_total')[0:3]
    categories = Category.objects.all()

    return {
        'Categories': categories,
        'populars': populars,
    }
