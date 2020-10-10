from django.shortcuts import render
from .forms import UrlForm
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.
def Thanks(request):
    return render(request, 'Home/thanks.html')


def home(request):
    if request.method == 'POST':
        st = UrlForm(request.POST)
        if st.is_valid():
            print('valid')
            ur = st.cleaned_data['url']
            mx = st.cleaned_data['max_price']
            mn = st.cleaned_data['min_price']
            reg = User( url=ur, max_price=mx, min_price=mn)
            reg.save()
            return HttpResponseRedirect('/th/thanks')
            
        else:
            st = UrlForm()
    else:
        st = UrlForm()
    return render(request, 'Home/home.html', {'form':st})