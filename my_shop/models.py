from django.db import models

class Iteam(models.Model):
    name=models.CharField(max_length=50,default="")

    price=models.IntegerField()
    description=models.CharField(max_length=300,default="")
    category=models.CharField(max_length=300,default="")
    image=models.ImageField(upload_to="my_shop/images",default="")

    def __str__(self):
        return self.name
