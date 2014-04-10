from shop.models import Product
from django.shortcuts import render_to_response
from django.template import RequestContext


def index_view(request):
    products = Product.objects.all()
    return render_to_response("cuescience_shop/index.html", RequestContext(request, {"products": products}))






