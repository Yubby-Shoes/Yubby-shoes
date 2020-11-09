from django.db import models
from accounts.models import Customer


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    category_initials = models.CharField(max_length=3)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_initials = models.CharField(max_length=5)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.00)
    discounted_price = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to='media/products')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_new_arrival = models.BooleanField(default=False)
    in_stock = models.IntegerField(default=0)
    product_model = models.CharField(max_length=10, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_model + '-' + self.name

    def save(self, *args, **kwargs):
        super().save()
        from PIL import Image
        original_img = Image.open(self.image.path)
        width, height = original_img.size
        if (width < height):
            x = 0
            y = (height - width) / 2
            cropped_img = original_img.crop((x, y, width + x, width + y))
        else:
            x = (width - height) / 2
            y = 0
            cropped_img = original_img.crop((x, y, height + x, height + y))
        cropped_img.save(self.image.path)


class OrderItem(models.Model):
    STATUS_CHOICES = (
        ('PR', 'Processing'),
        ('SH', 'Shipping'),
        ('DE', 'Delivered'),
    )
    ordered_on = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='orders')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_email = models.CharField(max_length=255, blank=True, null=True)
    order_quantity = models.IntegerField()
    order_status = models.CharField(max_length=3, choices=STATUS_CHOICES,
                                    default='PR')

    def __str__(self):
        return f"{self.product.name}"
