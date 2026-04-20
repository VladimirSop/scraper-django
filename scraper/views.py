from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def product_list(request):
    query = request.GET.get("q", "")

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    paginator = Paginator(products, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "scraper/index.html", {
        "page_obj": page_obj,
        "query": query
    })