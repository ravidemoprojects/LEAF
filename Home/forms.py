from django import forms
from .models import User

class UrlForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['url','max_price','min_price' ]
        widgets = {'max_price':forms.TextInput(attrs={'placeholder':'Enter max price range here','class':'form-control'}),
        'min_price':forms.TextInput(attrs={'placeholder':'Enter min price range here','class':'form-control'}),
        'url':forms.URLInput(attrs={'placeholder':'Enter URL here','class':'form-control'})}
        labels = {'url':'URL:'}
    
        