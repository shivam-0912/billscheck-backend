from django.db import models

class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    activation=models.IntegerField(default=0,blank=True)
        
class Item(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
   
    name=models.CharField(max_length=100)
    buy_date=models.DateField()
    expiry_date=models.DateField()
    bill_url=models.URLField(blank=True)
    company=models.CharField(max_length=100)
    contact1=models.CharField(max_length=10)
    contact2=models.CharField(max_length=10,blank=True)
    shop=models.CharField(max_length=100)
    description=models.TextField()
    
    

    
    
    