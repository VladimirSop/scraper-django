from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def product_list(request):
    query = request.GET.get("q", "").strip()
    sort = request.GET.get("sort", "")

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    # Sorting
    if sort == "price_asc":
        products = products.order_by("price")
    elif sort == "price_desc":
        products = products.order_by("-price")
    elif sort == "name":
        products = products.order_by("name")

    paginator = Paginator(products, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "scraper/index.html", {
        "page_obj": page_obj,
        "query": query,
        "sort": sort
    })
