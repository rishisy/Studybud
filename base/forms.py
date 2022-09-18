from django import forms  


class UploadFileForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input  



from .models import *
  
class UploadForm(forms.ModelForm):
  
    class Meta:
        model  = UploadImage
        fields = ['keywords', 'image']
        


