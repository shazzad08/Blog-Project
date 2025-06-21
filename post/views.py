from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.

def add_post(request):
     
    if request.method == 'POST':
          post_form = forms.Post_form(request.POST)

          if  post_form.is_valid():
                post_form.save()
                return redirect('add_post')
          
    else:
          post_form = forms.Post_form()
         
    return render(request,'add_post.html',{'form': post_form })




def edit_post(request,id):
      post = models.Post.objects.get(pk=id) #post model er sob obj k primary key diye dhoresi
      post_form = forms.Post_form(instance=post) #edit a click krar por jate ager information gula show kore tar jnno instance use krsi


      if request.method == 'POST':
          post_form = forms.Post_form(request.POST, instance=post) # user form edit a click krar por jdi r edit na kore tarpor o form submit hbe


          if  post_form.is_valid():
                post_form.save()
                return redirect('homepage')
          
   
      return render(request,'add_post.html',{'form': post_form })


def delete_post(request,id):
     del_post = models.Post.objects.get(pk=id)
     del_post.delete()

     return redirect('homepage')