from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin, CreateView
from .forms import OrderReviewForm, UserUpdateForm, ProfileUpdateForm

from .models import Order, Driver, Product, Route, Vehicle, Warehouse, Customer


# Create your views here.

# Kuriamos funkcijos kurios bus atvaizduojamos urls.py

def index(request):
    orders_count = Order.objects.all().count()
    user_orders = Order.objects.filter(user=request.user)
    user_orders_count = user_orders.count()
    total_sum = sum(order.get_total_price() for order in user_orders)

    drivers_count = Driver.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'orders_count': orders_count,
        'user_orders_count': user_orders_count,
        'drivers_count': drivers_count,
        'total_sum': total_sum,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


def drivers(request):
    all_drivers = Driver.objects.all()

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_drivers = Driver.objects.filter(
            Q(name__icontains=query) |
            Q(driver_number__icontains=query) |
            Q(email__icontains=query)
        )
        all_drivers = search_drivers

    # PUSLAPIAVIMAS
    page = request.GET.get('page', 1)
    paginator = Paginator(all_drivers, 5)

    try:
        all_drivers = paginator.page(page)
    except PageNotAnInteger:
        all_drivers = paginator.page(1)
    except EmptyPage:
        all_drivers = paginator.page(paginator.num_pages)

    context = {
        'all_drivers': all_drivers
    }

    return render(request, 'drivers/drivers.html', context=context)


def driver(request, driver_id):
    single_driver = get_object_or_404(Driver, pk=driver_id)
    return render(request, 'drivers/driver.html', {'driver': single_driver})


def orders(request):
    all_orders = Order.objects.all()

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_orders = Order.objects.filter(
            Q(customer__name__icontains=query) |
            Q(status__icontains=query) |
            Q(order_date__icontains=query) |
            Q(order_code__icontains=query)
        )
        all_orders = search_orders

    # PUSLAPIAVIMAS
    page = request.GET.get('page', 1)
    paginator = Paginator(all_orders, 5)

    try:
        all_orders = paginator.page(page)
    except PageNotAnInteger:
        all_orders = paginator.page(1)
    except EmptyPage:
        all_orders = paginator.page(paginator.num_pages)

    context = {
        'all_orders': all_orders
    }

    return render(request, 'orders/orders.html', context=context)


@csrf_protect
def order(request, order_id):
    single_order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        form = OrderReviewForm(request.POST)
        if form.is_valid():
            form.instance.order = single_order
            form.instance.reviewer = request.user
            form.save()

    form = OrderReviewForm
    order_reviews = single_order.orderreview_set.all()
    context = {
        'order': single_order,
        'order_reviews': order_reviews,
        'form': form
    }
    return render(request, 'orders/order.html', context=context)


def customers(request):
    all_customers = Customer.objects.all()
    all_users = User.objects.all()

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_customers = Customer.objects.filter(
            Q(name__icontains=query)
        )
        all_customers = search_customers

    # PUSLAPIAVIMAS
    page = request.GET.get('page', 1)
    paginator = Paginator(all_customers, 5)

    try:
        all_customers = paginator.page(page)
    except PageNotAnInteger:
        all_customers = paginator.page(1)
    except EmptyPage:
        all_customers = paginator.page(paginator.num_pages)

    context = {
        'all_customers': all_customers,
        'all_users': all_users
    }

    return render(request, 'customers/customers.html', context=context)


def products(request):
    all_products = Product.objects.all()

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(unit_price__icontains=query)
        )
        all_products = search_products

    # PUSLAPIAVIMAS
    page = request.GET.get('page', 1)
    paginator = Paginator(all_products, 5)

    try:
        all_products = paginator.page(page)
    except PageNotAnInteger:
        all_products = paginator.page(1)
    except EmptyPage:
        all_products = paginator.page(paginator.num_pages)

    context = {
        'all_products': all_products
    }

    return render(request, 'products/products.html', context=context)


def routes(request):
    all_routes = Route.objects.all()

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_routes = Route.objects.filter(
            Q(order__customer__name__icontains=query) |
            Q(vehicle__plate_number__icontains=query)
        )
        all_routes = search_routes

    # PUSLAPIAVIMAS
    page = request.GET.get('page', 1)
    paginator = Paginator(all_routes, 5)

    try:
        all_routes = paginator.page(page)
    except PageNotAnInteger:
        all_routes = paginator.page(1)
    except EmptyPage:
        all_routes = paginator.page(paginator.num_pages)

    context = {
        'all_routes': all_routes
    }

    return render(request, 'routes/routes.html', context=context)


def route(request, route_id):
    single_route = get_object_or_404(Route, pk=route_id)
    return render(request, 'routes/route.html', {'route': single_route})


def vehicles(request):
    all_vehicles = Vehicle.objects.all()

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_vehicles = Vehicle.objects.filter(
            Q(type__icontains=query) |
            Q(plate_number__icontains=query)
        )
        all_vehicles = search_vehicles

    # PUSLAPIAVIMAS
    page = request.GET.get('page', 1)
    paginator = Paginator(all_vehicles, 5)

    try:
        all_vehicles = paginator.page(page)
    except PageNotAnInteger:
        all_vehicles = paginator.page(1)
    except EmptyPage:
        all_vehicles = paginator.page(paginator.num_pages)

    context = {
        'all_vehicles': all_vehicles
    }

    return render(request, 'vehicles/vehicles.html', context=context)


def vehicle(request, vehicle_id):
    single_vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'vehicles/vehicle.html', {'vehicle': single_vehicle})


def warehouses(request):
    all_warehouses = Warehouse.objects.all()

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_warehouses = Warehouse.objects.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query)
        )
        all_warehouses = search_warehouses

    # PUSLAPIAVIMAS
    page = request.GET.get('page', 1)
    paginator = Paginator(all_warehouses, 5)

    try:
        all_warehouses = paginator.page(page)
    except PageNotAnInteger:
        all_warehouses = paginator.page(1)
    except EmptyPage:
        all_warehouses = paginator.page(paginator.num_pages)

    context = {
        'all_warehouses': all_warehouses
    }

    return render(request, 'warehouses/warehouses.html', context=context)


# GAUNAMOS USER GRUPES
def my_view(request):
    user_group = None
    if request.user.is_authenticated:
        user_group = request.user.groups.first()
    return render(request, 'base.html', {'user_group': user_group})


# ATVAIZDUOJAMI TAM TIKRO USER ORDERIAI
@login_required
def user_orders(request):
    user_orders_list = Order.objects.filter(user=request.user)
    # gaunama visu uzsakymu bendra suma
    total_sum = sum(order.get_total_price() for order in user_orders_list)

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        # searc_conditions skirtas, kad paieska butu tik is USER uzsakymu o ne bendru.
        search_conditions = Q(user=request.user) & (
                Q(customer__name__icontains=query) |
                Q(status__icontains=query) |
                Q(order_date__icontains=query) |
                Q(order_code__icontains=query)
        )
        user_orders_list = Order.objects.filter(search_conditions).order_by('status')

    # RIKIAVIMAS PAGAL STATUS
    sort_by = request.GET.get('sort_by', 'status')
    user_orders_list = user_orders_list.order_by(sort_by)

    # PUSLAPIAVIMAS
    paginator = Paginator(user_orders_list, 5)
    page = request.GET.get('page')

    try:
        user_orders = paginator.page(page)
    except PageNotAnInteger:
        user_orders = paginator.page(1)
    except EmptyPage:
        user_orders = paginator.page(paginator.num_pages)

    context = {
        'user_orders': user_orders,
        'sort_by': sort_by,
        'total_sum': total_sum,
    }

    return render(request, 'user/user_orders.html', context)


@csrf_protect
def register(request):
    if request.method == "POST":
        # Gauti reiksmes is formos
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Patkrinti ar sutampa slaptazodziai
        if password == password2:
            # patikrinti ar toks username nera uzimtas
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} jau užimtas!')
                return redirect('register')
            else:
                # patikrinti ar toks gmail nera uzimtas
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # sukurti nauju user kuriant uzsakova
                    user = User.objects.create_user(username=username, email=email, password=password)

                    messages.success(request, f'Vartotojas {username} sėkmingai užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')

    return render(request, 'registration/register.html')


class UserOrderDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order.html'
    form_class = OrderReviewForm

    def get_success_url(self):
        return reverse('order', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # nurodome, kad order bus būtent ta, po kuria komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.order = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(UserOrderDetailView, self).form_valid(form)


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile/profile.html', context)
