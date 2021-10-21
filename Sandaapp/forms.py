from django import forms
from .models import Customer, Product, OrderDetails, Orders, Addresses, Payment, Category, Cart, Favorite


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_id', 'cust_lastname', 'cust_email', 'city', 'state', 'zipcode', 'phone_number', 'created_date',
                  'updated_date')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_id', 'category_name', 'category_description')


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payment_id', 'order_id', 'payment_method', 'payment_status')


class AddressesForm(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = (
            'name', 'shipping_Addresses', 'billing_Addresses', 'Addresses_line_1', 'Addresses_line_2', 'city', 'country',
            'state',
            'postal_code')


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = (
            'order_id', 'cust_id', 'payment_id', 'shipping_Addresses', 'billing_Addresses', 'status',
            'shipping_total',
            'order_total', 'active', 'date_placed', 'date_shipped')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_id', 'category_id', 'product_name', 'product_description', 'product_price', 'product_category', 'product_catalog', 'remaining_quantity')


class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ('order_details_id', 'order_id', 'product_id', 'total_price', 'quantity')


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('cart_id', 'cust_id', 'product_id', 'cart_total')


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ('product_id', 'cust_id')