from django.shortcuts import render

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})