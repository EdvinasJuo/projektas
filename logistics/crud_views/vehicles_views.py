from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from logistics.models import Vehicle


class VehicleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Vehicle
    template_name = 'vehicles/vehicle.html'
    context_object_name = 'vehicle'
    pk_url_kwarg = 'vehicle_id'


class VehicleCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Vehicle
    fields = ['type', 'make', 'model', 'year', 'plate_number', 'status']
    success_url = reverse_lazy('vehicles') # sugeneruoja URL dinaminiu budu
    template_name = 'vehicles/vehicle_form.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class VehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Vehicle
    fields = ['type', 'make', 'model', 'year', 'plate_number', 'status']
    success_url = reverse_lazy('vehicles')  # sugeneruoja URL dinaminiu budu
    template_name = 'vehicles/vehicle_form.html'
    pk_url_kwarg = 'vehicle_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden

class VehicleDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicles')  # sugeneruoja URL dinaminiu budu
    template_name = 'vehicles/vehicle_delete.html'
    pk_url_kwarg = 'vehicle_id'

    def test_func(self):
        return self.request.user.is_superuser