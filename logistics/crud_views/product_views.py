from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from logistics.models import Product


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Product
    fields = ['name', 'unit_price']
    success_url = reverse_lazy('products') # sugeneruoja URL dinaminiu budu
    template_name = 'products/product_form.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Product
    fields = ['name', 'unit_price']
    success_url = reverse_lazy('products')  # sugeneruoja URL dinaminiu budu
    template_name = 'products/product_form.html'
    pk_url_kwarg = 'product_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('products')  # sugeneruoja URL dinaminiu budu
    template_name = 'products/product_delete.html'
    pk_url_kwarg = 'product_id'

    def test_func(self):
        return self.request.user.is_superuser
