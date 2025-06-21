from django.shortcuts import render,redirect
from .import views
from .import forms

# Create your views here.
def add_profiles(request):
    if request.method == "POST":
        profile_form = forms.Profile_form(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profiles')
        
    else:
          profile_form = forms.Profile_form()

    return render(request,'add_profile.html',{'form': profile_form })