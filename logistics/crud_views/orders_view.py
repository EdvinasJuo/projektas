from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from logistics.forms import OrderCreateForm
from logistics.models import Order


class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Order
    success_url = reverse_lazy('orders') # sugeneruoja URL dinaminiu budu
    template_name = 'orders/order_form.html'
    form_class = OrderCreateForm

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Order
    form_class = OrderCreateForm
    success_url = reverse_lazy('orders')  # sugeneruoja URL dinaminiu budu
    template_name = 'orders/order_form.html'
    pk_url_kwarg = 'order_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden\

class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy('orders')  # sugeneruoja URL dinaminiu budu
    template_name = 'orders/order_delete.html'
    pk_url_kwarg = 'order_id'

    def test_func(self):
        return self.request.user.is_superuser