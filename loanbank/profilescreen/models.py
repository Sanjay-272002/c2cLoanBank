from django.db import models

# Create your models here
class data(models.Model):
    accountnumber = models.CharField(max_length=200)
    branch = models.CharField(max_length = 200)
    CTC = models.CharField(max_length = 200)
    aadharcard = models.FileField(upload_to='datas/pdfs')
    pancard = models.FileField(upload_to='datas/pdfs')
    salaryslips = models.FileField(upload_to='datas/pdfs')
    photo = models.FileField(upload_to='datas/pdfs')


    def __str__(self):
        return self.accountnumber

