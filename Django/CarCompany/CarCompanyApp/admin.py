from django.contrib import admin
from CarCompanyApp.models import Contact,Sell,CarService,Wishlist,Cart,Car

# Register your models here.
admin.site.register(Contact)
admin.site.register(CarService)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Car)
class SellAdmin(admin.ModelAdmin):
    list_display = ("owner_name", "car_name", "price", "condition")

admin.site.register(Sell, SellAdmin)

