from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from logistics.models import Driver


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    template_name = 'drivers/driver.html'
    context_object_name = 'driver'
    pk_url_kwarg = 'driver_id'  # Set the URL keyword to 'driver_id'

class DriverCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Driver
    fields = ['name', 'driver_number', 'phone_number' ,'email' ,'vehicle']
    success_url = reverse_lazy('drivers') # sugeneruoja URL dinaminiu budu
    template_name = 'drivers/driver_form.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class DriverUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Driver
    fields = ['name', 'driver_number', 'phone_number', 'email', 'vehicle']
    success_url = reverse_lazy('drivers')
    template_name = 'drivers/driver_form.html'
    pk_url_kwarg = 'driver_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden


class DriverDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Driver
    success_url = reverse_lazy('drivers')  # sugeneruoja URL dinaminiu budu
    template_name = 'drivers/driver_delete.html'
    pk_url_kwarg = 'driver_id'

    def test_func(self):
        return self.request.user.is_superuser