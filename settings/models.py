from django.db import models
from utils.generate_code import generate_code

class Document_Type(models.Model):
    name=models.CharField(max_length=120)
    code=models.CharField(max_length=75,default=generate_code)
    notes=models.TextField(max_length=1500)

    def __str__(self):
        return self.name

class Sector(models.Model):
    name=models.CharField(max_length=120)
    code=models.CharField(max_length=75,default=generate_code)
    notes=models.TextField(max_length=1500)

    def __str__(self):
        return self.name


class Contractor(models.Model):
    code=models.CharField(max_length=120,default=generate_code)
    name=models.CharField(max_length=120)
    sector=models.ForeignKey(Sector,related_name='contractor_sector',on_delete=models.SET_NULL,null=True,blank=True)
    project=models.CharField(max_length=100)
    item=models.CharField(max_length=150)
    notes=models.TextField(max_length=700)
    code_archive=models.CharField(max_length=120,null=True,blank=True,unique=True)

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.code_archive=self.sector.code +'_'+self.code
        super(Contractor,self).save(*args,**kwargs)

