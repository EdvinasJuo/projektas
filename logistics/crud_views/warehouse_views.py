from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from logistics.models import Warehouse


class WarehouseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Warehouse
    template_name = 'warehouses/warehouse.html'
    context_object_name = 'warehouse'
    pk_url_kwarg = 'warehouse_id'

class WarehouseCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Warehouse
    fields = ['name', 'location']
    success_url = reverse_lazy('warehouses') # sugeneruoja URL dinaminiu budu
    template_name = 'warehouses/warehouse_form.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class WarehouseUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Warehouse
    fields = ['name', 'location']
    success_url = reverse_lazy('warehouses')  # sugeneruoja URL dinaminiu budu
    template_name = 'warehouses/warehouse_form.html'
    pk_url_kwarg = 'warehouse_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden

class WarehouseDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Warehouse
    success_url = reverse_lazy('warehouses')  # sugeneruoja URL dinaminiu budu
    template_name = 'warehouses/warehouse_delete.html'
    pk_url_kwarg = 'warehouse_id'

    def test_func(self):
        return self.request.user.is_superuser
