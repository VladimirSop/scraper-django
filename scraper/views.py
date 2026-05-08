from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem

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

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/')


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    total = sum(item.total_price() for item in cart_items)

    return render(request, 'scraper/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def remove_from_cart(request, item_id):
    item = CartItem.objects.get(id=item_id)

    if item.user == request.user:
        item.delete()

    return redirect('cart')