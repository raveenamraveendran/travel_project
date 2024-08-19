from django.db import models

# Create your models here.
class places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    descr=models.TextField()


    def __str__(self):
        return self.name


class person(models.Model):
    img=models.ImageField(upload_to='pics')
    names=models.CharField(max_length=250)
    des=models.TextField()

    def __str__(self):
        return self.names