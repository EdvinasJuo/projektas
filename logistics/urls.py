from django.urls import path
from . import views
from .crud_views.customers_views import CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView
from .crud_views.drivers_views import DriverDetailView, DriverCreateView, DriverUpdateView, DriverDeleteView
from .crud_views.orders_view import OrderCreateView, OrderUpdateView, OrderDeleteView
from .crud_views.product_views import ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .crud_views.routes_view import RouteDetailView, RouteCreateView, RouteUpdateView, RouteDeleteView
from .crud_views.vehicles_views import VehicleDetailView, VehicleCreateView, VehicleUpdateView, VehicleDeleteView
from .crud_views.warehouse_views import WarehouseCreateView, WarehouseDetailView, WarehouseUpdateView, \
    WarehouseDeleteView

# ATVAIZDUOJA IS VIEWS FAILO NURODZIOJ NAME = ''
# PIRMOSE KABUTESE NURODOMAS PATH PAVADINIMAS pvz http://127.0.0.1:8000/test

urlpatterns = [
    path('', views.index, name='index'),
    path('drivers/', views.drivers, name='drivers'),
    path('drivers/<int:driver_id>/', DriverDetailView.as_view(), name='driver'),
    path('drivers/new', DriverCreateView.as_view(), name='driver-new'),
    path('drivers/<int:driver_id>/update', DriverUpdateView.as_view(), name='driver-update'),
    path('drivers/<int:driver_id>/delete', DriverDeleteView.as_view(), name='driver-delete'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:order_id>', views.order, name='order'),
    path('order/new', OrderCreateView.as_view(), name='order-new'),
    path('order/<int:order_id>/update', OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:order_id>/delete', OrderDeleteView.as_view(), name='order-delete'),
    path('customers/', views.customers, name='customers'),
    path('customers/<int:customer_id>/', CustomerDetailView.as_view(), name='customer'),
    path('customers/new', CustomerCreateView.as_view(), name='customer-new'),
    path('customers/<int:customer_id>/update', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<int:customer_id>/delete', CustomerDeleteView.as_view(), name='customer-delete'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product'),
    path('products/new', ProductCreateView.as_view(), name='product-new'),
    path('products/<int:product_id>/update', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:product_id>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('routes/', views.routes, name='routes'),
    path('routes/<int:route_id>/', RouteDetailView.as_view(), name='route'),
    path('routes/new', RouteCreateView.as_view(), name='route-new'),
    path('routes/<int:route_id>/update', RouteUpdateView.as_view(), name='route-update'),
    path('routes/<int:route_id>/delete', RouteDeleteView.as_view(), name='route-delete'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/<int:vehicle_id>/', VehicleDetailView.as_view(), name='vehicle'),
    path('vehicles/new', VehicleCreateView.as_view(), name='vehicle-new'),
    path('vehicles/<int:vehicle_id>/update', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicles/<int:vehicle_id>/delete', VehicleDeleteView.as_view(), name='vehicle-delete'),
    path('warehouses/', views.warehouses, name='warehouses'),
    path('warehouses/<int:warehouse_id>/', WarehouseDetailView.as_view(), name='warehouse'),
    path('warehouses/new', WarehouseCreateView.as_view(), name='warehouse-new'),
    path('warehouses/<int:warehouse_id>/update', WarehouseUpdateView.as_view(), name='warehouse-update'),
    path('warehouses/<int:warehouse_id>/delete', WarehouseDeleteView.as_view(), name='warehouse-delete'),
    path('user_orders/', views.user_orders, name='my-orders'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
