from django import forms
from .models import data
# #DataFlair #File_Upload
class dataForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ('accountnumber','branch','phonenumber','aadharcard','pancard','salaryslips','photo')
        