from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict = {
        "product1": "Mac",
        "product2": "Windows",
        "product3": "Linux"
    }
    return render(request, 'products_app/products.html', context=product_dict)

def toys(request):
    product_dict = {
        "product1": "Remote Cars",
        "product2": "Rocket",
        "product3": "Drone"
    }
    return render(request, 'products_app/products.html', context=product_dict)

def shoes(request):
    product_dict = {
        "product1": "Nike",
        "product2": "Adidas",
        "product3": "Lofo"
    }
    return render(request, 'products_app/products.html', context=product_dict)

def index(request):
    return render(request, 'products_app/index.html')