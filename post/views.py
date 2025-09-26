from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
# Create your views here.
@login_required
def add_post(request):
     
    if request.method == 'POST':
          post_form = forms.Post_form(request.POST)

          if  post_form.is_valid():
                
                post_form.instance.author= request.user
                post_form.save()
                return redirect('add_post')
          
    else:
          post_form = forms.Post_form()
         
    return render(request,'add_post.html',{'form': post_form })

# Class based view 
@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.Post_form
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     
     
@login_required
def edit_post(request,id):
      post = models.Post.objects.get(pk=id) #post model er sob obj k primary key diye dhoresi
      post_form = forms.Post_form(instance=post) #edit a click krar por jate ager information gula show kore tar jnno instance use krsi


      if request.method == 'POST':
          post_form = forms.Post_form(request.POST, instance=post) # user form edit a click krar por jdi r edit na kore tarpor o form submit hbe


          if  post_form.is_valid():
                post_form.instance.author= request.user
                post_form.save()
                return redirect('homepage')
          
   
      return render(request,'add_post.html',{'form': post_form })


@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
     model = models.Post
     form_class = forms.Post_form
     template_name = 'add_post.html'
     pk_url_kwarg = 'id'
     success_url =  reverse_lazy('homepage')

      

@login_required
def delete_post(request,id):
     del_post = models.Post.objects.get(pk=id)
     del_post.delete()

     return redirect('homepage')


@method_decorator(login_required, name='dispatch')
class Delete_View(DeleteView):
     model = models.Post
     template_name = 'delete.html'
     pk_url_kwarg = 'id'
     success_url = reverse_lazy('homepage')



class DetailPostView(DetailView):
    model = models.Post
    template_name='post_details.html'
    pk_url_kwarg = 'id'
    

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context