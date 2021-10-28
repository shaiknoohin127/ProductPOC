from django.db import models

# Create your models here.
class Product(models.Model):
    def nameFile(instance,filename):
        return '/'.join(['images',str(instance.Name),filename])


    Name=models.CharField(max_length=255)
    Picture=models.ImageField(upload_to=nameFile,blank=True)
    Description=models.CharField(max_length=100)
    Price=models.IntegerField()
    Quantity=models.IntegerField()       
    
    
    def __str__(self):
        return self.Name