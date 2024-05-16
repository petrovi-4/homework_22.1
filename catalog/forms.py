from django import forms

from catalog.models import Product, Version
from config.settings import FORBIDDEN_WORDS


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if set(product_name.lower().split()).intersection(set(FORBIDDEN_WORDS)):
            raise forms.ValidationError('Нельзя использовать запрещенные слова')
        return product_name


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
