from django.shortcuts import render
from .models import Cart
# Create your views here.


# def cart_home(request):
#     return render(request, "carts/home.html", {})

# CART Session management both Guest and Login user
def cart_home(request):
    # request.session["Cart_id"] = 1
    cart_id = request.session.get("cart_id", None)
    if not cart_id:
        print("New Cart Created!!")
        cart_obj = Cart.objects.create(user=None)
        request.session["cart_id"] = cart_obj.id
    else:
        print("Cart already exist!!")
    return render(request, "carts/home.html", {})
