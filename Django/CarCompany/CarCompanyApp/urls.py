
from django.contrib import admin
from django.urls import path
from CarCompanyApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path("", views.hello,name='CarCompanyApp'),
    # path("",views.indexLogin,name = "indexLogin"),
    path("",views.loginUser,name = "login"),
    path("logout",views.logoutUser,name = "logout"),
    path("about", views.about,name='about'),
    path("home", views.home,name='home'),
    #path("services", views.services,name='services'),
    path("buy/", views.buy,name='buy'),
    path("sell", views.sell,name='sell'),
    path("car_services", views.car_services,name='car_services'),
    path("contact", views.contact,name='contact'),
    # path('add-to-wishlist/<str:car_name>/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('wishlist/', views.view_wishlist, name='wishlist'),
    # path('add-to-cart/<str:car_name>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', views.view_cart, name='cart'),
    # path('wishlist/remove/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    # path('wishlist/move-to-cart/<int:item_id>/', views.move_to_cart, name='move_to_cart'),
    # path('add-to-wishlist/<str:car_name>/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('wishlist/', views.view_wishlist, name='wishlist'),
    # path('remove-from-wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    # path('move-to-cart/<int:item_id>/', views.move_to_cart, name='move_to_cart'),
    
    # path('add-to-cart/<str:car_name>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', views.view_cart, name='cart'),
    # path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('move-to-wishlist/<int:item_id>/', views.move_to_wishlist, name='move_to_wishlist'),
    path('buy/', views.buy, name='buy'),
    path('add-to-wishlist/<int:car_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('add-to-cart/<int:car_id>/', views.add_to_cart, name='add_to_cart'),

    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('wishlist/remove/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/move-to-cart/<int:item_id>/', views.move_to_cart, name='move_to_cart'),

    path('cart/', views.view_cart, name='cart'),
    path('cart/proceed/', views.proceed_payment, name='proceed_payment'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/move-to-wishlist/<int:item_id>/', views.move_to_wishlist, name='move_to_wishlist'),

        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
