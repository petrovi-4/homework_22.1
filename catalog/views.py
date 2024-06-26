from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class IndexView(TemplateView):
    template_name = 'catalog/catalog_list.html'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all().order_by('-id')[:5]
        return context_data


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Новое сообщение от пользователя {name}({email}): {message}')
        return self.render_to_response({'title': 'Контакты'})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = product_item.product_name
        if product_item.version_set.filter(is_active=True):
            context_data['version'] = product_item.version_set.filter(is_active=True).last()
        else:
            context_data['version'] = None
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list_product')


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Список товаров'
    }


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list_product')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list_product')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'  # добавлено
    success_url = reverse_lazy('catalog:list_product')

    # def form_valid(self, form):
    #     product = form.cleaned_data['product']
    #     form.instance.product = product
    #     return super().form_valid(form)
        # product_id = self.kwargs['pk']
        # product = get_object_or_404(Product, id=product_id)
        # form.instance.product = product
        # return super().form_valid(form)


class VersionDetailView(DetailView):
    model = Version


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:list_product')


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:list_product')
