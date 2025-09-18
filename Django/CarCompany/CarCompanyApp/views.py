# from django.shortcuts import render
# from django.http import HttpResponse
from CarCompanyApp.models import Contact
from CarCompanyApp.models import Sell,CarService
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login as auth_login
from CarCompanyApp.models import Wishlist, Cart,Car
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("home") 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username =username ,password = password)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            return render(request,'login.html',{"error": "Invalid username or password"})
    return render(request, "login.html")
def logoutUser(request):
    logout(request)
    return redirect("login")

# @login_required(login_url="login") 
def home(request):
    return render(request, "index.html")
   
def about(request):
    return render(request,'about.html')

def buy(request):
    return render(request,'buy.html')
    #return HttpResponse("Services Page!")
def sell(request):
    if request.method == "POST":
        
        owner_name = request.POST.get('owner_name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        address = request.POST.get('address')
        car_name = request.POST.get('car_name')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        condition = request.POST.get('condition')
        image = request.FILES.get('image')
        
        detail = Sell(owner_name = owner_name,
                        contact_no = contact_no,
                        email = email,
                        address = address,
                        car_name = car_name,
                        model = model,
                        year = year,
                        price = price,
                        condition = condition,
                        image = image
                        )
                            
        detail.save()
        messages.success(request,'Your message has been sent!')
    return render(request,'sell.html')

    # return render(request,'sell.html')
    #return HttpResponse("Services Page!")
def car_services(request):
    if request.method == "POST":
    
        owner_name = request.POST.get('owner_name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        address = request.POST.get('address')
        car_name = request.POST.get('car_name')
        model = request.POST.get('model')
        year = request.POST.get('year')
        services = request.POST.getlist("services")
        services_str = ", ".join(services)

        
        detail = CarService(owner_name = owner_name,
                        contact_no = contact_no,
                        email = email,
                        address = address,
                        car_name = car_name,
                        model = model,
                        year = year,
                        services = services_str                   
                        )
                            
        detail.save()
        messages.success(request,'Your message has been sent!')
    return render(request,'car_services.html')
    #return HttpResponse("Services Page!")
def contact(request):
    if request.method == "POST":
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Email = request.POST.get('Email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        #date = datetime.today()
        contact = Contact(First_Name = First_Name,
                          Last_Name = Last_Name,
                          Email = Email,
                          phone_number = phone_number,
                          message = message)
                          
        contact.save()
        messages.success(request,'Your message has been sent!')
    return render(request,'contact.html')
    #return HttpResponse("Contact Page!")




def buy(request):
    cars = Car.objects.all()  # Only cars for buying
    return render(request, "buy.html", {"cars": cars})

@login_required
def add_to_wishlist(request, car_id):
    car = Car.objects.get(id=car_id)
    Wishlist.objects.create(
        user=request.user,
        car_name=car.name,
        car_image=car.image,
        price=car.price
    )
    messages.success(request, f"{car.name} added to wishlist!")
    return redirect('buy')

@login_required
def add_to_cart(request, car_id):
    car = Car.objects.get(id=car_id)
    Cart.objects.create(
        user=request.user,
        car_name=car.name,
        car_image=car.image,
        price=car.price
    )
    messages.success(request, f"{car.name} added to cart!")
    return redirect('buy')

@login_required
def view_wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, "wishlist.html", {"items": items})

@login_required
def remove_from_wishlist(request, item_id):
    Wishlist.objects.filter(id=item_id, user=request.user).delete()
    messages.success(request, "Item removed from wishlist!")
    return redirect("wishlist")

@login_required
def move_to_cart(request, item_id):
    item = Wishlist.objects.get(id=item_id, user=request.user)
    Cart.objects.create(
        user=request.user,
        car_name=item.car_name,
        car_image=item.car_image,
        price=item.price
    )
    item.delete()
    messages.success(request, f"{item.car_name} moved to cart!")
    return redirect("wishlist")

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_amount = sum(item.price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})


@login_required
def proceed_payment(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_amount = sum(item.price for item in cart_items)
    
    # Here you can integrate payment gateway logic
    
    # For now, clear the cart and show success message
    cart_items.delete()
    messages.success(request, "Payment is Successful")
    
    # Redirect to some page after payment, e.g., order summary or home page
    return render(request, 'payment_success.html', {'total_amount': total_amount})
    
@login_required
def remove_from_cart(request, cart_id):
    item = Cart.objects.filter(id=cart_id, user=request.user).first()
    if item:
        item.delete()
    return redirect('cart')
@login_required
def move_to_wishlist(request, item_id):
    item = Cart.objects.get(id=item_id, user=request.user)
    Wishlist.objects.create(
        user=request.user,
        car_name=item.car_name,
        car_image=item.car_image,
        price=item.price
    )
    item.delete()
    messages.success(request, f"{item.car_name} moved to wishlist!")
    return redirect("cart")