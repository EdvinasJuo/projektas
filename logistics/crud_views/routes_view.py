from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from logistics.forms import RouteCreateForm
from logistics.models import Route


class RouteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Route
    template_name = 'routes/route.html'
    context_object_name = 'route'
    pk_url_kwarg = 'route_id'  # Set the URL keyword to 'driver_id'

class RouteCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Route
    success_url = reverse_lazy('routes') # sugeneruoja URL dinaminiu budu
    template_name = 'routes/route_form.html'
    form_class = RouteCreateForm

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class RouteUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Route
    form_class = RouteCreateForm
    success_url = reverse_lazy('routes')  # sugeneruoja URL dinaminiu budu
    template_name = 'routes/route_form.html'
    pk_url_kwarg = 'route_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden

class RouteDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Route
    success_url = reverse_lazy('routes')  # sugeneruoja URL dinaminiu budu
    template_name = 'routes/route_delete.html'
    pk_url_kwarg = 'route_id'

    def test_func(self):
        return self.request.user.is_superuser
