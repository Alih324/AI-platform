from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    details = models.TextField()
    found = models.BooleanField(default=True)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name


class Product_Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'product review'
        verbose_name_plural = 'product reviews'

    def __str__(self):
        return f'{self.author.username} review on {self.product.product_name} - {self.rating}'
