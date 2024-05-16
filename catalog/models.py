from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Нименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(
        upload_to='products/', **NULLABLE,
        verbose_name='Изображение'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name='Цена за покупку'
    )
    date_create = models.DateField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    last_modified_date = models.DateField(
        auto_now=True, verbose_name='Дата последнего изменения'
    )
    # manufactured_at = models.DateField(
    #     **NULLABLE,
    #     verbose_name='Дата производства продукта')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
