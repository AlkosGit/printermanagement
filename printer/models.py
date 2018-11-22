from django.db import models

# Create your models here.

class Acco(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.name)

class Brand(models.Model):
    printerbrand = models.CharField(max_length=64)
        
    def __str__(self):
        return '{}'.format(self.printerbrand)

class Model(models.Model):
    printermodel = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.printermodel)

class Printer(models.Model):
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='model')
    serial = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)
    lease_start = models.CharField(max_length=64)
    lease_end = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    contract = models.CharField(max_length=64)
    acconame = models.ForeignKey(Acco, on_delete=models.CASCADE, related_name='location')

    def __str__(self):
        return '{}'.format(self.name)

