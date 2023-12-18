from django.contrib import admin
from .models import Driver, Vehicle, Product, Order, Route, Customer, Warehouse, OrderReview, Profile

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location', 'phone_number')
    search_fields = ('name', 'email', 'phone_number')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('type','make','model','year', 'plate_number', 'status')
    search_fields = ('plate_number','make','model', 'year', 'type', 'status')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'order_code', 'user', 'get_status_display',
                    'get_product_name', 'get_unit_price', 'quantity', 'get_total_price')

    def get_product_name(self, obj):
        return obj.product.name if obj.product else ""

    get_product_name.short_description = 'Produktas'

    def get_unit_price(self, obj):
        return obj.product.unit_price if obj.product else 0.0

    get_unit_price.short_description = 'Vieneto kaina'

    def get_total_price(self, obj):
        return obj.get_total_price()

    get_total_price.short_description = 'Bendra suma'

    search_fields = ('customer__name', 'id', 'product__name')

class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'driver_number', 'phone_number', 'email', 'vehicle')
    search_fields = ('name', 'driver_number', 'phone_number', 'email', 'vehicle__plate_number')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit_price')
    search_fields = ('name', 'id')

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'vehicle', 'departure', 'warehouse', 'arrival', 'get_customer_location')

    def get_customer_location(self, obj):
        return obj.order.customer.location

    get_customer_location.short_description = 'Kliento adresas'

    search_fields = ('order__customer__location', 'id', 'order__customer__name')
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('id', 'name', 'location')

class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ('order', 'date_created', 'reviewer', 'content')


admin.site.register(Profile)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(OrderReview, OrderReviewAdmin)
