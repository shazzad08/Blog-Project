from django.contrib.auth.views import LoginView

# ...existing code...

class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
from django.shortcuts import render,redirect
from .import forms
from .forms import ChangeUserData
from post.models import Post
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.utils.decorators import method_decorator
# Create your views here.
# def add_author(request):

#     if request.method == 'POST':  #user post req korese
#      author_form = forms.Author_form(request.POST) # user er post req er data eikhane capture krlm

#      if author_form.is_valid():
#         author_form.save()  # jdi data valid hoy database a save krbo
#         return redirect('add_author') # sob thik thkle etake add_author a pathai dibo

#     else:
#        author_form = forms.Author_form()

#     return render(request,'add_author.html', {'form':author_form})



def register(request):
   if request.method == 'POST':  #user post req korese
     register_form = forms.Registrationform(request.POST) # user er post req er data eikhane capture krlm

     if register_form.is_valid():
        user = register_form.save()  # jdi data valid hoy database a save krbo
        login(request,user)
        messages.success(request,'Account Created Successfully')
        return redirect('profile') # sob thik thkle etake add_author a pathai dibo

   else:
       register_form = forms.Registrationform()

   return render(request,'register.html', {'form':register_form,'type': 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']

            user = authenticate(username=user_name, password=user_pass)

            if user is not None:
                messages.success(request, 'Login Successfully')
                login(request, user)
                return redirect('profile')
        else:
            messages.warning(request, 'Information is incorrect')
            return redirect('user_login')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type': 'Login'})
  

    


@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)  # type: ignore

    return render(request,'profile.html',{'data': data})







    

def pass_change(request):
    if request.method == 'POST':  #user post req korese
        form = PasswordChangeForm(user=request.user, data=request.POST) # user er post req er data eikhane capture krlm

        if form.is_valid():
            user = form.save()  # jdi data valid hoy database a save krbo
            login(request,user)
            update_session_auth_hash(request,user)
            messages.success(request,'Password Updated Successfully')
            return redirect('profile') # sob thik thkle etake add_author a pathai dibo

    else:
        form = PasswordChangeForm(user=request.user)

    return render(request,'pass_change.html', {'form':form, 'type':'Password Change' })

@login_required
def edit_profile(request):

    if request.method == 'POST':  #user post req korese
      profile_form = forms.ChangeUserData(request.POST, instance=request.user) # user er post req er data eikhane capture krlm

      if  profile_form.is_valid():
         profile_form.save()  # jdi data valid hoy database a save krbo
         messages.success(request,'Profile Updated Successfully')
         return redirect('profile') # sob thik thkle etake add_author a pathai dibo

    else:
        profile_form = forms.ChangeUserData(instance = request.user)

    return render(request,'update_profile.html', {'form': profile_form,'type':'Profile'})
