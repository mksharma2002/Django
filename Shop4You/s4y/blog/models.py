from django.db import models


# Create your models here.
class BlogPost(models.Model):
    post_Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Head_0 = models.CharField(max_length=2000)
    Content_Head_0 = models.CharField(max_length=2000)
    Head_1 = models.CharField(max_length=2000)
    Content_Head_1 = models.CharField(max_length=2000)
    Head_2 = models.CharField(max_length=2000)
    Content_Head_2 = models.CharField(max_length=1000)
    published_date = models.DateField()
    thumbnail =models.ImageField(upload_to="shop/images", default="")

    def _str_(self):
        return self.Title
        