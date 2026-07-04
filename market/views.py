from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm, ProductReviewForm
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'market/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    review_form = ProductReviewForm()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_to_cart':
            cart = request.session.get('cart', {})
            product_id = str(product.pk)
            cart[product_id] = cart.get(product_id, 0) + 1
            request.session['cart'] = cart
            messages.success(request, f'{product.product_name} was added to your cart.')
            return redirect('cart')

        if action == 'review':
            if not request.user.is_authenticated:
                messages.error(request, 'Please log in to add a review.')
                return redirect('login')
            review_form = ProductReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = product
                review.author = request.user
                review.save()
                messages.success(request, 'Your review was added.')
                return redirect('product_detail', pk=product.pk)

    reviews = product.reviews.select_related('author')
    return render(request, 'market/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
    })


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'market/add_product.html', {'form': form})


def cart(request):
    cart_data = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart_data.keys())
    cart_items = []
    total = Decimal('0.00')

    for product in products:
        quantity = cart_data.get(str(product.pk), 0)
        line_total = product.price * quantity
        total += line_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'line_total': line_total,
        })

    return render(request, 'market/cart.html', {'cart_items': cart_items, 'total': total})


def checkout(request):
    cart_data = request.session.get('cart', {})
    if request.method == 'POST':
        if not cart_data:
            messages.error(request, 'Your cart is empty.')
            return redirect('product_list')
        request.session['cart'] = {}
        messages.success(request, 'Order placed successfully. Thank you!')
        return redirect('product_list')
    return render(request, 'market/checkout.html', {'has_items': bool(cart_data)})
