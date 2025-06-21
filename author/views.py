from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def add_author(request):

    if request.method == 'POST':  #user post req korese
     author_form = forms.Author_form(request.POST) # user er post req er data eikhane capture krlm

     if author_form.is_valid():
        author_form.save()  # jdi data valid hoy database a save krbo
        return redirect('add_author') # sob thik thkle etake add_author a pathai dibo

    else:
       author_form = forms.Author_form()

    return render(request,'add_author.html', {'form':author_form})

