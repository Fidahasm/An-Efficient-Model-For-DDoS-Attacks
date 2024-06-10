from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class user(models.Model):
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    signature=models.FileField()
    place=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=100)
    dob=models.DateField()
    idproof=models.FileField()



class branch(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    IFSC=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class complaint(models.Model):
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)

class feedback(models.Model):
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    date=models.DateField()
    feedback=models.CharField(max_length=100)

class report_table(models.Model):
    BRANCH=models.ForeignKey(branch,on_delete=models.CASCADE)
    report=models.TextField()
    date = models.DateField()

class Account_details(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    Account_No=models.IntegerField()
    BRANCH= models.ForeignKey(branch, on_delete=models.CASCADE)
    Balance=models.FloatField()
    pin_num=models.IntegerField()


class transaction(models.Model):
   ACC_NO= models.ForeignKey(Account_details, on_delete=models.CASCADE)
   Type = models.CharField(max_length=100)
   date = models.DateField()
   Amount=models.FloatField()
   Transaction_type=models.CharField(max_length=100)


class request_table(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    BRANCH= models.ForeignKey(branch, on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    date=models.DateField()
class log_tb(models.Model):

    ip=models.CharField(max_length=20)
    date=models.DateTimeField()
class block_list(models.Model):
    ip=models.CharField(max_length=20)