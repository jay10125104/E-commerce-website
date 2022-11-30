from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
STATE_CHOICES = (
    ('gujarat','gujarat'),
    ('goa','goa'),
    ('rajasthan','rajasthan'),
    ('kerela','kerela'),
    ('jharkhand','jharkhand'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length = 50)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES,max_length = 50)
    def __str__(self):
        return str(self.id)
CATAGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)
class Product(models.Model):
    title = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices = CATAGORY_CHOICES,max_length = 2)
    product_image = models.ImageField(upload_to='producting')
    
    def __str__(self):
        return self.title
    
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    def __str__(self):
        return str(self.id)
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Cancel','Cancel')
) 
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 50,choices=STATUS_CHOICES,default='Pending')