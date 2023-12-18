from django.contrib.auth.models import User
from .models import OrderReview, Profile, Order, Route
from django import forms

class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ('content', 'order', 'reviewer')
        widgets = {'order': forms.HiddenInput(), 'reviewer': forms.HiddenInput()} #paslepiami, kad negalima butu redaguot


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nuotrauka']

class DateInput(forms.DateInput):
    input_type = 'date'

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'customer', 'order_date','status' ,'driver', 'product', 'quantity', 'warehouse']
        widgets = {'order_date': DateInput()}

class RouteCreateForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['order', 'vehicle', 'departure', 'arrival', 'warehouse']
        widgets = {'departure': DateInput(), 'arrival':DateInput()}