from django.db import models

# Create your models here.
class Product(models.Model):
    product_Id = models.AutoField
    product_Name = models.CharField(max_length=100)
    product_Desc = models.CharField(max_length=2000)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=200, default="")
    published_date = models.DateField()
    price = models.IntegerField(default=0)
    image =models.ImageField(upload_to="shop/images", default="")
    


    def __str__(self):
        return self.product_Name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."