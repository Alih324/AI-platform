from django import forms

from .models import Product, Product_Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'details', 'found', 'category', 'image', 'price']
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product name',
            }),
            'details': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Product details',
            }),
            'found': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category',
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
            }),
        }

    def clean_product_name(self):
        product_name = self.cleaned_data['product_name'].strip()
        if len(product_name) < 2:
            raise forms.ValidationError('Product name must be at least 2 characters long.')
        return product_name


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Product_Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '5',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write a short review...',
            }),
        }

    def clean_content(self):
        content = self.cleaned_data['content'].strip()
        if len(content) < 3:
            raise forms.ValidationError('Review must be at least 3 characters long.')
        return content
