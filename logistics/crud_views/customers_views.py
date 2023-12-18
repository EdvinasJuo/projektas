from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from logistics.models import Customer

class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    template_name = 'customers/customer.html'
    context_object_name = 'customer'
    pk_url_kwarg = 'customer_id'  # Set the URL keyword to 'driver_id'

class CustomerCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Customer
    fields = ['name', 'email', 'location' ,'phone_number']
    success_url = reverse_lazy('customers') # sugeneruoja URL dinaminiu budu
    template_name = 'customers/customer_form.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class CustomerUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Customer
    fields = ['name', 'email', 'location', 'phone_number']
    success_url = reverse_lazy('customers')  # sugeneruoja URL dinaminiu budu
    template_name = 'customers/customer_form.html'
    pk_url_kwarg = 'customer_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden

class CustomerDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Customer
    success_url = reverse_lazy('customers')  # sugeneruoja URL dinaminiu budu
    template_name = 'customers/customer_delete.html'
    pk_url_kwarg = 'customer_id'

    def test_func(self):
        return self.request.user.is_superuser